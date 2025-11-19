import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
import base64
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="YSDS - Yashfeen Skills Development Services", layout="wide", page_icon="💡")
st.title("🎓Welcome to **YSDS**")

# --- ASSETS & STYLING ---
logo_path = "icon.jpeg"  
background_path = "bg.png" 

# Load Knowledge Base
if os.path.exists("knowledge_base.txt"):
    with open("knowledge_base.txt", "r", encoding="utf-8") as file:
        SCRIPT = file.read()
else:
    SCRIPT = "You are a helpful assistant for Yashfeen Skills Development Services."

# Helper: Encode Image
def get_base64_of_image(img_file):
    try:
        with open(img_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except: return ""

# Helper: Assistant Avatar CSS
def assistant_chat_css(logo_file):
    base64_image = get_base64_of_image(logo_file)
    if not base64_image: return ""
    return f"""
    <style>
        .stChatMessage .avatar {{
            background-image: url("data:image/jpeg;base64,{base64_image}");
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
            border-radius: 50%;
        }}
    </style>
    """

# Helper: Background CSS
def set_background(image_file):
    base64_image = get_base64_of_image(image_file)
    if base64_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{base64_image}");
                background-size: cover; 
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Apply Styling
set_background(background_path)
st.markdown(assistant_chat_css(logo_path), unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.image("logo.jpeg", use_container_width=150)
    st.markdown(
        """
        <div style='text-align: center;'>
            <h4><b> 🌟Yashfeen Skills Development🌟 </b>\n\n Services \n\n----------------- \n\n <em>Empowering youth through practical tech skills</em> </h4>
        </div>
        """, unsafe_allow_html=True
    )

    st.markdown("### 📌 Contact Us")
    st.write("📧 Email: info@yes.edu.pk")
    st.write("✆  Whatsapp: [Click here to chat](https://wa.me/923211114937)")
    st.write("📞 Phone: +92 321 1114937")
    st.write("🌐 Website: [www.yes.edu.pk](http://www.yes.edu.pk)")
    st.write("📍  Address: 9-Saeed Park Ravi Road Infront Shahdara Fly-over, Shahdarah Lahore, Pakistan.")
    st.write("🔗 [Facebook](https://www.facebook.com/YashfeenSkills) | [Instagram](https://www.instagram.com/yashfeenskills/) | [LinkedIn](https://www.linkedin.com/company/yashfeen-skills-development-services/)")

    st.header("📋 List of Courses.")
    courses = {
        "E-Commerce": "3 months | HI-End | Free",
        "Graphic Designing": "3 months | HI-End | Free",
        "UI/UX Designing": "3 months | HI-End | Free",
        "Video editing": "3 months | HI-End | Free",
        "Computerized Accounting": "3 months | HI-End | Free",
        "Office Management": "3 months | HI-End | Free",
        "Digital and Social Media Marketing": "3 months | HI-End | Free",
        "Web Development": "3 months | HI-End | Free",
        "Mobile App Development": "3 months | HI-Tech | Free",
        "Advanced Web-App Development": "3 months | HI-Tech | Free",
        "Artificial Intelligence - AI": "3 months | HI-Tech | Free",
        "Cloud Computing Microsoft": "3 months | HI-Tech | Free",
        "Cyber Security": "3 months | HI-Tech | Free",
        "Big Data Analytics Techniques": "3 months | HI-Tech | Free",
        "Cloud Computing AWS": "3 months | HI-Tech | Free",
        "Cloud Computing Networking": "3 months | HI-Tech | Free",
        "Advance Python Programming and Applications": "3 months | HI-Tech | Free",
        "Full Stack Development": "3 months | HI-Tech | Free",
        "Amazon Virtual Assistant": "3 months | HI-Tech| Free",
        "Game Development": "3 months | HI-Tech | Free",
        "Javascript Full Stack Development": "3 months | HI-Tech | Free"
    }

    for name, details in courses.items():
        st.subheader(f"✨ {name}")
        st.caption(details)

    st.markdown("---")
    st.caption("💡 Ask me about syllabus, Eligibility-Criteria or admission process!")

    st.markdown("### ⚙️ Settings")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state["chat_history"] = []
        st.session_state["memory_store"] = {} # Clear AI memory
        st.success("Chat history cleared!")

# --- SESSION STATE INIT ---
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    st.session_state["has_greeted"] = False 

# --- AI LOGIC (MODERN FIX) ---
# Function to manage chat history for the AI
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if "memory_store" not in st.session_state:
        st.session_state["memory_store"] = {}
    if session_id not in st.session_state["memory_store"]:
        st.session_state["memory_store"][session_id] = ChatMessageHistory()
    return st.session_state["memory_store"][session_id]

google_api_key = st.secrets.get("GOOGLE_API_KEY")

if google_api_key:
    # 1. Create LLM
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key, temperature=0.5)
    
    # 2. Create Prompt (Replaces PromptTemplate)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "{script}"),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ])

    # 3. Create Chain (Replaces ConversationChain)
    chain = prompt | llm | StrOutputParser()

    # 4. Wrap with Memory
    conversation_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="input",
        history_messages_key="history",
    )

else:
    st.error("Google API key not found in secrets.")
    st.stop()


# --- CHAT INTERFACE ---

if not st.session_state["has_greeted"]:
    initial_greeting = "👋Hi! I'm Sam, Your informational guide from **Yashfeen Skills Development Services**. Ask me anything about courses, fees, or admissions!☺️"
    st.session_state["chat_history"].append({"role": "assistant", "content": initial_greeting})
    st.session_state["has_greeted"] = True

for msg in st.session_state["chat_history"]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Ask something about Yashfeen Education System...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state["chat_history"].append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Modern method to run the chain
                bot_response = conversation_chain.invoke(
                    {"input": user_input, "script": SCRIPT},
                    config={"configurable": {"session_id": "default_session"}}
                )
                
                st.markdown(bot_response)
                st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Error: {e}")
