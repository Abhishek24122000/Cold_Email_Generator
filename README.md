# 📧 Cold Mail Generator — Hyper-Personalized AI Outreach

**AI-Powered Cold Email Generator for Modern Service Companies**  
Built by **Abhishek**, this app turns any careers page into a **personalized lead-generation goldmine** using the power of LLMs, vector databases, and intelligent scraping.  

Forget generic outreach. This tool delivers **contextual, portfolio-rich cold emails** tailored to specific job listings — in seconds.

---

## 🚀 Why This Project Matters

Hiring managers receive 100s of generic cold emails daily.  
This app flips the game by using **real-time job descriptions** and **your most relevant portfolio content** to craft personalized messages — 10x more likely to convert 🚀

---

## 🧠 What It Does

🔗 **Input**: Careers page URL of your target company  
🕸️ **Scraping**: LangChain scrapes live job listings  
🧾 **Parsing**: Extracts job details and role-specific context  
🔍 **Matching**: Queries your portfolio using a vector database  
✉️ **Output**: Auto-generates a personalized cold email with portfolio links

All powered by **Groq API** + **Meta’s LLaMA 70B** — insanely fast, stupidly smart 💥

---

## ⚙️ Setup & Attribution (All-in-One)

### 1️⃣ Get a Groq API Key  
Create one at 👉 https://console.groq.com/keys  
Add it to your `.env` file inside `app/`:

```env```
GROQ_API_KEY=your_api_key_here

### 2️⃣ Install Dependencies
pip install -r requirements.txt


### 3️⃣ Run the App
streamlit run app/main.py



### Architecture Overview
User Input URL
      ⬇️
LangChain Scraper → Job Descriptions
      ⬇️
NLP Parser → Key Skill Extraction
      ⬇️
Vector DB Search (Portfolio Index)
      ⬇️
Prompt Engineering (LLM Context)
      ⬇️
Groq API (LLaMA 70B Model)
      ⬇️
✉️ Hyper-personalized Email with Embedded Proof

### Attribution & Legal
Inspired by a basic version by Codebasics under MIT.
This version has been heavily modified and extended by Abhishek (that’s me 💪).

Uses Meta's LLaMA 70B model via Groq API.
All rights to the model belong to Meta AI. The app uses it via API and claims no ownership over the LLM.

