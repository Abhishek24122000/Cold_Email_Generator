Cold Mail Generator — AI-Powered Personalized Outreach Tool

An intelligent cold email generator designed for modern job seekers and professionals.
This tool transforms any careers page into a personalized, portfolio-aware cold email using the power of large language models and intelligent web scraping.

Built with Streamlit, LangChain, and Meta’s LLaMA 70B via Groq API.

🌐 Live Demo

👉 https://coldemailgenerator-tool.streamlit.app

⚙️ What It Does

Scrapes real-time job data from a careers page URL

Extracts and parses resume data (PDF)

Injects portfolio and project links automatically

Lets users choose the purpose of the email (e.g., job, collaboration, mentorship)

Generates personalized, context-rich cold emails in multiple languages

Uses on-screen API key input for enhanced privacy — no .env storage required

🧩 Why It Matters

Traditional outreach = ignored emails.
Cold Mail Generator = relevant, resume-aware, human-sounding messages that actually connect.

References real job descriptions

Integrates your resume & skills

Embeds your portfolio or project links

Writes in a professional tone, instantly

Your email becomes an intelligent pitch, not a generic spam message.

🔥 Features

LangChain Web Scraper → Extracts live job content

PyMuPDF (fitz) → Parses PDF resumes

Groq API (LLaMA 70B) → Generates multilingual emails

Minimalist Streamlit UI → Dark theme, optimized for speed

Dynamic API Key Input → Enter directly in-app, session-only

Smart Prompt Templates → Personalized for job, internship, or project

🧠 Technical Workflow
USER INTERFACE (Streamlit)
    │
    ├── User Inputs
    │     ├─ Job / Career Page URL
    │     ├─ Resume (PDF Upload)
    │     ├─ Name / Role / Summary
    │     ├─ Project & Portfolio Links
    │     ├─ Language + Purpose
    │     └─ API Key (entered on-screen, session-only)
    │
    ├── LangChain WebBaseLoader
    │       ↓
    │   Job Description Scraper
    │       ↓
    ├── PDF Parser (PyMuPDF)
    │       ↓
    │   Resume Text Extraction
    │       ↓
    ├── NLP Cleaning + Prompt Engineering
    │       ↓
    ├── Groq API (LLaMA 70B / 3.3-70B)
    │       ↓
    ├── Email Generation
    │       ↓
    └── Streamlit Output Display


Everything runs locally + API-side, no persistent data or API keys are stored.
Each session remains isolated and temporary — security by design.

💻 Tech Stack
Component	Technology
Frontend UI	Streamlit
Resume Parsing	PyMuPDF (fitz)
Web Scraping	LangChain WebBaseLoader
LLM Engine	Meta’s LLaMA 70B via Groq API
Backend Logic	Python + Prompt Engineering
Deployment	Streamlit Cloud
🚀 How to Use (Live App)

Visit coldemailgenerator-tool.streamlit.app

Enter your Groq API key in the on-screen input box

Paste a job or career page URL

Fill in your name, role, and about section

Upload your resume (PDF)

Add LinkedIn, GitHub, or Portfolio links

Optionally highlight a key project

Choose language and email purpose

Click “Generate Cold Email” 📨

Your custom, professional cold email will appear instantly.

⚙️ Local Development Setup
1. Clone Repository
git clone https://github.com/Abhishek24122000/Cold_Email_Generator.git
cd Cold_Email_Generator

2. Install Requirements
pip install -r requirements.txt

3. Run the App
streamlit run main.py


💡 You can still set your API key from the Streamlit interface directly —
no .env setup required.
However, you can optionally create a .env for local testing if preferred:

GROQ_API_KEY=your_groq_api_key_here

🔮 Future Roadmap

🎭 Tone selector (Formal / Friendly / Persuasive)

🧬 Resume vector embeddings for smart job-role matching

📤 Direct Gmail/Outlook integration

📱 Responsive mobile UI optimization

📊 Analytics dashboard for email success tracking

👥 Target Audience

Job seekers & professionals applying globally

Fresh graduates reaching out for internships

Freelancers pitching to clients

Career changers seeking mentorship

Recruiters automating outreach

💡 Example Scenarios

Applying for a Data Analyst role in Japan 🇯🇵

Writing a Japanese cold email automatically

Following up with a recruiter post-interview

Requesting mentorship from a senior engineer

Pitching freelance work to a startup

⚖️ License

Proprietary Software License Agreement
© 2025 Abhishek. All rights reserved.
Use permitted only for personal, non-commercial purposes via the public Streamlit app.

No copying, redistribution, or modification allowed without explicit written consent.
The app uses third-party APIs (e.g., Groq / LLaMA 70B) — all rights to those models belong to their respective owners.

For licensing or collaboration inquiries:
📧 palsodkarabhishek24@gmail.com

👨‍💻 Author




