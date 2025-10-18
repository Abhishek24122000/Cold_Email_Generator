# 🧊 Cold Mail Generator — Personalized AI-Powered Outreach Tool  

[![Live App](https://img.shields.io/badge/Launch_App-Streamlit-brightgreen?logo=streamlit)](http://bit.ly/43s2jCp)
[![Groq Key](https://img.shields.io/badge/Get_Groq_API_Key-blue?logo=groq)](https://console.groq.com/keys)
[![GitHub](https://img.shields.io/badge/Source_Code-GitHub-black?logo=github)](https://github.com/Abhishek24122000/Cold_Email_Generator)

---

### ✨ Overview  
Cold Mail Generator is a smart, resume-aware cold email generator for **job seekers, freelancers, and professionals**.  
It converts any careers page and your uploaded resume into a **personalized, professional cold email** in seconds.  

Built with **Streamlit**, **LangChain**, and **Meta’s LLaMA 70B via Groq API**.

🌍 **Live Demo:** [http://bit.ly/43s2jCp](http://bit.ly/43s2jCp)  

---

## ⚙️ What It Does  

- Scrapes job listings from a **careers page URL**  
- Extracts text from uploaded **resumes (PDF)**  
- Injects **portfolio links, role, and personal details**  
- Generates **professional, human-sounding cold emails**  
- Supports **multiple languages & purposes** (Job, Internship, Mentorship, Collaboration)  
- Uses **on-screen API key input** — no `.env` required or stored locally  

---

## 🧩 Why It Works  

Traditional outreach fails because it’s generic.  
Cold Mail Generator uses your **real resume and real job data** to write messages that actually make sense.  

- Reads the **job description** dynamically  
- Matches with **your resume content**  
- Crafts a **polished and relevant** email instantly  

You get **a cold email that sounds like you**, not like a template.

---

## 🔥 Features  

- 🧠 **LangChain Web Scraper** → Fetches live job data  
- 📄 **PyMuPDF (fitz)** → Parses resume text  
- 🧬 **Groq API (LLaMA 70B)** → Generates multi-language emails  
- 🎨 **Streamlit UI** → Minimalist and fast interface  
- 🔑 **API Key Input** → Enter directly in app, session-only (never stored)  
- 🧱 **Dynamic Prompts** → Context-aware email personalization  

---

## 🧠 Technical Workflow  

User Interface (Streamlit)  
⬇️  
User Inputs → (Name, Role, Resume, Links, Purpose, API Key)  
⬇️  
LangChain WebBaseLoader → Scrapes careers page  
⬇️  
PyMuPDF (fitz) → Extracts resume text  
⬇️  
Prompt Engineering → Combines job & resume context  
⬇️  
Groq API (LLaMA 70B / 3.3-70B) → Generates cold email  
⬇️  
Streamlit Frontend → Displays editable, polished result  

⚡ **No data or keys are stored** — all processing is session-based and secure.

---

## 💻 Tech Stack  

| Component | Technology |
|------------|-------------|
| Frontend | Streamlit |
| Resume Parsing | PyMuPDF (`fitz`) |
| Web Scraping | LangChain WebBaseLoader |
| LLM Engine | LLaMA 70B via Groq API |
| Backend Logic | Python + Prompt Engineering |
| Deployment | Streamlit Cloud |

---

## 🚀 Quick Start (Local Setup)  


# 1. Clone repository
git clone https://github.com/Abhishek24122000/Cold_Email_Generator.git
cd Cold_Email_Generator

# 2. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 3. Run locally
streamlit run main.py
💡 API Key Setup:

The app uses on-screen API key input (session-only).

You can generate your Groq API key here → https://console.groq.com/keys

Optionally, you may export it for local dev:

bash
Copy code
set GROQ_API_KEY=your_key_here
(Optional only — not required for normal users.)

📦 Recommended requirements.txt
makefile
Copy code
streamlit
PyMuPDF==1.26.5
langchain
langchain-community
groq
requests
beautifulsoup4
python-dotenv
🔮 Future Roadmap
🎭 Tone Selector (Formal / Friendly / Persuasive)

🧬 Resume Embedding for Smart Job Match

📤 One-Click Gmail/Outlook Integration

📱 Mobile-Responsive UI

📊 Past records 

👥 Who It’s For
Job seekers applying to top companies

Students or interns doing cold outreach

Freelancers pitching to clients

Professionals seeking mentorship

Recruiters automating outreach

💡 Example Use
Apply for a Data Analyst role in Japan 🇯🇵

Write cold emails in Japanese / English / German

Follow up post-interview

Request mentorship or collaboration

Pitch freelance services

⚖️ License
Proprietary License — © 2025 Abhishek. All Rights Reserved.
Use allowed only for personal, non-commercial purposes via the public Streamlit app.
Source code, modification, or redistribution without written consent is prohibited.

The app integrates third-party APIs (Groq / LLaMA 70B) — all rights to those models belong to their respective owners.

📧 For licensing or collaborations: palsodkarabhishek24@gmail.com




