# 📧 Cold Mail Generator

**AI-powered cold email generator** for services companies — powered by Groq + Meta's LLaMA 70B model via LangChain + Streamlit.  
Built to help you pitch smarter by analyzing real job listings and crafting hyper-personalized emails — complete with relevant portfolio links from your own vector database.

---

## 🧠 How It Works
1. Enter a company's **careers page URL**.
2. The app scrapes job listings using LangChain tools.
3. It parses job descriptions and identifies key themes.
4. It queries a **vector database** to match portfolio projects.
5. It generates **personalized cold emails** with job-relevant proof.

---

## ⚙️ Set-up Instructions

### 1. Get a Groq API Key
Head to 👉 https://console.groq.com/keys  
Create an API key and paste it into `app/.env`:

```dotenv
GROQ_API_KEY=your_api_key_here



## Install Python Dependencies
pip install -r requirements.txt


## Run the App Locally
streamlit run app/main.py
