# Cold Mail Generator — AI-Powered Personalized Outreach Tool

An intelligent cold email generator designed for modern job seekers.  
This tool transforms any careers page into a personalized, portfolio-aware cold email using the power of large language models and smart scraping.

Built with Streamlit, LangChain, and Meta’s LLaMA 70B via Groq API.

---

## Live Demo  
[https://coldemailgenerator-tool.streamlit.app](https://coldemailgenerator-tool.streamlit.app)

---

## What It Does

- Scrapes live job descriptions from a careers page URL  
- Extracts relevant resume content (PDF upload)  
- Allows optional portfolio and project link injection  
- Lets users select the purpose (job, internship, collaboration, follow-up, etc.)  
- Generates clean, personalized, and context-aware cold emails  
- Supports multiple output languages

---

## Why It Matters

Generic outreach fails.  
This app creates cold emails that:

- Reference **real job content**
- Align with **your resume and skills**
- Include your **portfolio links**
- Are written with professional tone, speed, and clarity

It increases the chance of response by delivering **real relevance**.

---

## Features

- Web scraping via LangChain  
- Resume parsing via PyMuPDF  
- Multilingual email output  
- Built-in cold email types (application, mentorship, collaboration, etc.)  
- Project showcase section  
- Streamlit UI with dark theme  
- Powered by LLaMA 70B via Groq API

---

## Architecture Overview

User Input
↓
LangChain Scraper → Job Descriptions
↓
NLP Parsing + Resume Extraction
↓
Optional Vector Match (Portfolio/Projects)
↓
Prompt Engineering
↓
Groq API (LLaMA 70B)
↓
Cold Email Output


---

## Tech Stack

| Component         | Technology                  |
|------------------|------------------------------|
| Frontend         | Streamlit                    |
| Resume Parsing   | PyMuPDF (fitz)               |
| Scraping         | LangChain WebBaseLoader      |
| Backend Logic    | Python + Prompt Engineering  |
| LLM Engine       | LLaMA 70B via Groq API       |

---

## How to Use (Live App)

1. Go to [coldemailgenerator-tool.streamlit.app](https://coldemailgenerator-tool.streamlit.app)  
2. Paste a job listing or careers page URL  
3. Fill in your name, role, and summary  
4. Upload your resume (PDF)  
5. Add LinkedIn/GitHub/Portfolio links  
6. Highlight a key project (optional)  
7. Choose the email type  
8. Click “Generate Cold Email”

---

## Local Setup Instructions

### 1. Clone the Repository

git clone https://github.com/Abhishek24122000/Cold_Email_Generator.git
cd Cold_Email_Generator


### 2. Install Requirements

pip install -r requirements.txt

### 3. Configure API Key

Create a `.env` file inside the `app` directory:

GROQ_API_KEY=your_groq_api_key_here

You can get your key from: https://console.groq.com/keys

### 4. Run the App

streamlit run app/main.py

---

## Future Roadmap

- AI tone selector (formal, friendly, persuasive)  
- Resume vector embedding for smarter job-role matching  
- One-click Gmail/Outlook send integration  
- Improved mobile UI responsiveness  
- Analytics dashboard for outreach performance

---

## Target Audience

- Job seekers applying to global companies  
- Interns or fresh graduates reaching out to recruiters  
- Professionals seeking career collaborations  
- Freelancers offering services via email  
- Career changers or those networking internationally

---

## Example Use Cases

- Applying for a data analyst role at a Japanese startup  
- Reaching out to a company in native Japanese or Spanish  
- Following up after an application submission  
- Requesting mentorship from a senior engineer  
- Introducing yourself after attending a tech event

---

## License

MIT License.  
Uses Meta’s LLaMA 70B model via Groq API.  
No model weights are hosted or stored in this repository. All rights belong to their respective owners.

---

## Author

[![Portfolio](https://img.shields.io/badge/Portfolio-000?style=for-the-badge&logo=firefox&logoColor=white)](https://abhishek24122000.github.io/portfolio.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhishek-palsodkar-936937183/)
[![GitHub](https://img.shields.io/badge/GitHub-171515?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abhishek24122000)
