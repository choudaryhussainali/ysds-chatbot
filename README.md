# 🎓 YSDS Chatbot – AI-Powered Informational Assistant

This project is an AI-powered chatbot built for **Yashfeen Skills Development Services (YSDS)** using Streamlit and Gemini API. It provides students and visitors      with accurate, human-like responses to questions about courses, admissions, and institute details.
    
---

![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-f06) ![Python](https://img.shields.io/badge/Built%20with-Pyhton-yellow) ![License](https://img.shields.io/badge/License-MIT-green) ![Made with ❤](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red) 

## 🚀 Features

- 💬 Human-like conversation with memory using LangChain
- 📋 Displays complete list of 21 free Hi-End and Hi-Tech courses
- 📝 Guides users through the admission process step-by-step
- 📌 Shares contact details, location, and social media links
- 🧠 Follows a strict scripted behavior for professional interaction
- 🖼️ Custom UI with branded background and assistant icon
- 🔒 Supports chat history and session memory

---

## ⚙️ Technologies Used

- Python
- Streamlit
- LangChain
- Google Gemini API (`langchain-google-genai`)
- HTML/CSS (for UI customization)

---

## 🧠 Tech Stack

| Layer        | Library / Service |
|--------------|-------------------|
| Frontend     | Streamlit         |
| LLM          | Google Gemini Pro (Flash) via LangChain |
| Memory       | `ConversationBufferMemory` |
| Prompting    | `PromptTemplate` (strict scripted persona) |
| Styling      | Inline CSS + base64‑encoded images |

---

## 📁 Project Structure

```
ysds-chatbot/
│
├── .streamlit/
│   └── secrets.toml                # put your Google API key here
│
├── assets/
│   ├── icon.jpeg                   # assistant avatar
│   ├── bg.png                      # background image
│   └── logo.jpeg                   # sidebar logo
│
├── app.py                          # main Streamlit chatbot script
├── requirements.txt                # Python dependencies (see below)
├── README.md                       # full project documentation (see below)
└── LICENSE                         # optional open‑source licence

```

---

## 🧪 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/ysds-chatbot.git
   cd ysds-chatbot



### Install Dependencies.
     ```bash
     pip install -r requirements.txt

### Add your Google API key in .streamlit/secrets.toml

      ```bash
      GOOGLE_API_KEY = "your_gemini_api_key_here"


--- 

### 4. Run 

```
python chatbot.py
```

---

### 📷 Preview


![Screenshot (27)](https://github.com/user-attachments/assets/6da01bf8-8249-4f11-bd1b-d2a9cdb7af5f)


---


## 📄 License

This project is proprietary and confidential. All rights reserved.

```
© 2025 HUSSAIN ALI. This code may not be copied, modified, distributed, or used without explicit permission.
```

---

## 📬 Contact

For questions or collaboration requests:

* 📧 Email: [choudaryhussainali@outlook.com](mailto:choudaryhussainali@outlook.com)
* 🌐 GitHub: [choudaryhussainali](https://github.com/choudaryhussainali)

---


