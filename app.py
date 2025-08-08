import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import PromptTemplate
import base64
import os


with open("knowledge_base.txt", "r", encoding="utf-8") as file:
    SCRIPT = file.read()

# Function to encode the image to base64
def get_base64_of_image(img_file):
    with open(img_file, "rb") as f:
        return base64.b64encode(f.read()).decode()
def assistant_chat_css(logo_file):
    try:
        base64_image = get_base64_of_image(logo_file)
        return f"""
    <style>
        .streamlit-chat-message[data-streamlit-widget="ChatMessage(role='assistant')] div:first-child {{
            background-image: url("data:image/jpeg;base64,{base64_image}") !important; /* Adjust image type if needed */
            background-position: center center !important;
            background-repeat: no-repeat !important;
            background-size: contain !important;
            width: 3em !important;
            height: 3em !important;
            border-radius: 50% !important;
            background-color: #f0f2f6 !important;
        }}
        .streamlit-chat-message[data-streamlit-widget="ChatMessage(role='assistant')] div:first-child img {{
            visibility: hidden !important;
        }}
    </style>
    """
    except FileNotFoundError:
        st.error(f"Error: Logo file not found.")
        return ""
    except Exception as e:
        st.error(f"Error encoding logo: {e}")
        return ""


    st.markdown(assistant_chat_css(logo_path), unsafe_allow_html=True)



def set_background(image_file):
    """Sets the background of the Streamlit app behind the chat area with reduced opacity."""
    try:
        base64_image = get_base64_of_image(image_file)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/jpeg;base64,{base64_image}"); /* Adjust image type if needed */
                background-size: contain;
                background-repeat: no-repeat;
                position: fixed; /* To fix it behind other elements */
                top: 200;
                left: 0;
                right: 200 ;
                bottom: 100;

                width: 100%;
                height: 100%;
                z-index: -1; /* To place it behind other elements */    
                background-position: right 50px center;
                background-position: 75% center;        }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.error(f"Error: Background image file not found.")
    except Exception as e:
        st.error(f"Error encoding background image: {e}")


st.set_page_config(page_title="YSDS - Yashfeen Skills Development Services", layout="wide", page_icon="💡")
st.title("🎓Welcome to **YSDS**")

google_api_key = st.secrets.get("GOOGLE_API_KEY")


logo_path = "icon.jpeg"  
background_path = "bg.png" 


set_background(background_path)

with st.sidebar:
    # Display the logo in the sidebar
    st.image("logo.jpeg", use_container_width=150)

    st.markdown(
        """
        <div style='text-align: center;'>
            <h4><b> 🌟Yashfeen Skills Development🌟 </b>\n\n Services \n\n----------------- \n\n <em>Empowering youth through practical tech skills</em> </h4>
        </div>
        """,
        unsafe_allow_html=True
    )


with st.sidebar:

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

with st.sidebar:
    st.markdown("### ⚙️ Settings")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.success("Chat history cleared!")


if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    st.session_state["has_greeted"] = False 


if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory()



if google_api_key:
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=google_api_key, temperature=0.5)
    prompt_template = PromptTemplate(
        input_variables=["history", "input"],
        template="""
{script}
Conversation History:
{history}

User: {input}
Assistant:""".strip()
    )

    chain = ConversationChain(
        llm=llm,
        memory=st.session_state["memory"],
        prompt=prompt_template.partial(script=SCRIPT),
        verbose=False
    )
else:
    st.error("Google API key not found. Please add it to `.streamlit/secrets.toml` as GOOGLE_API_KEY")
    st.stop()

st.markdown(assistant_chat_css(logo_path), unsafe_allow_html=True)

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
                bot_response = chain.run(user_input)
                st.markdown(bot_response)
                st.session_state["chat_history"].append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.error(f"Error: {e}")

