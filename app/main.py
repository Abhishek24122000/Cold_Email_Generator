import streamlit as st
import fitz
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text, clean_url

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
st.cache_resource.clear()

# ----------------------
# Runtime API key prompt
# ----------------------
# store key in session only (no disk writes)
if "GROQ_API_KEY" not in st.session_state:
    st.session_state["GROQ_API_KEY"] = None

st.markdown(
    """
    <style>
    .api-box { background:#f6f7fb; padding:10px; border-radius:8px; margin-bottom:12px;}
    .api-label { font-weight:600; font-size:14px;}
    </style>
    """,
    unsafe_allow_html=True
)

with st.container():
    st.write("")  # small spacer
    st.markdown("<div class='api-box'>", unsafe_allow_html=True)
    st.markdown("<div class='api-label'>🔑 Enter Groq API Key (session-only)</div>", unsafe_allow_html=True)
    api_input = st.text_input("Paste GROQ API key here (will NOT be stored on disk)", type="password", placeholder="groq-xxxx...")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Set API Key"):
            if not api_input.strip():
                st.warning("Please paste a valid API key before setting.")
            else:
                st.session_state["GROQ_API_KEY"] = api_input.strip()
                st.success("API key set for this session.")
    with col2:
        if st.button("Clear API Key"):
            st.session_state["GROQ_API_KEY"] = None
            st.info("API key cleared from session.")
    # show masked status
    if st.session_state.get("GROQ_API_KEY"):
        masked = "●" * 8
        st.markdown(f"**Status:** Active ({masked}) — will be used for LLM calls.")
    else:
        st.markdown("**Status:** No API key set. Falling back to environment variable if present.")
    st.markdown("</div>", unsafe_allow_html=True)

# ----------------------
# helper: extract text from PDF
# ----------------------
def extract_text_from_pdf(uploaded_file):
    try:
        doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        st.error(f"❌ Failed to extract resume text: {e}")
        return ""

# ----------------------
# app creator (unchanged)
# ----------------------
def create_streamlit_app(llm, clean_text):
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 38px;
            font-weight: 800;
            color: #FFFFFF !important;
            text-align: left;
            margin-bottom: 20px;
        }
        .title {
            font-size: 24px;
            font-weight: 600;
            color: #4F4F4F;
        }
        footer {visibility: hidden;}
        .footer-text {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: transparent;
            color: #AAAAAA;
            text-align: center;
            padding: 6px 0;
            font-size: 12px;
            font-weight: 300;
            z-index: 999;
            font-family: 'Segoe UI', sans-serif;
        }
        </style>

        <div class='main-header'>
            🚀 Cold Email Generator Tool Powered by LLM (LLaMA 70B + LangChain)<br>
            Automate professional outreach in seconds
        </div>
        <hr>
        """,
        unsafe_allow_html=True
    )

    url_input = st.text_input("🌐 Enter the Job/Career Page URL:",
                              placeholder="e.g., https://company.com/careers",
                              help="Paste the careers or job listings page URL")

    name_input = st.text_input("Your Name:", placeholder="Your full name")
    role_input = st.text_input("Your Role:", placeholder="e.g., Data Analyst")
    about_yourself_input = st.text_area("Tell us About Yourself:", placeholder="Summary or intro")

    st.markdown("---")
    st.subheader("Upload Resume & Portfolio")

    resume_file = st.file_uploader("Upload Your Resume (PDF)", type=["pdf"])
    links_input = st.text_area("LinkedIn, GitHub, Portfolio:", placeholder="Paste your links here...")
    project_input = st.text_area("🛠 Highlight a Project (optional):", placeholder="Describe a key project you want to showcase")

    language_input = st.selectbox("Email Language:", [
        "English", "Japanese", "Spanish", "French", "German", "Hindi", "Arabic", "Chinese", "Korean", "Russian", "Portuguese"
    ])

    reason_explanations = {
        "Job Application": "Express interest in a job role and introduce yourself to the hiring team.",
        "Internship Request": "Ask for internship opportunities in your field.",
        "Project Collaboration": "Suggest working together on a joint project.",
        "Service/Product Pitch": "Propose a solution, tool, or product that may benefit the company.",
        "Freelance Opportunity": "Offer freelance support as an independent contributor.",
        "Appreciation & Networking": "Show admiration and try to build a professional connection.",
        "Mentorship Request": "Ask for career guidance, tips, or mentorship.",
        "Volunteer Contribution": "Offer your skills as a volunteer or contributor.",
        "Business Partnership": "Suggest a formal business collaboration or synergy.",
        "Media/PR Inquiry": "Reach out for podcasts, interviews, or influencer collabs.",
        "Follow-Up on Application": "Check in on your application status after applying."
    }

    selected_reason_ui = st.selectbox("✉️ Why are you writing this email?", list(reason_explanations.keys()))
    st.markdown(f"**Reason Explained:** {reason_explanations[selected_reason_ui]}")
    selected_reason_short = selected_reason_ui.split(" ")[0] if selected_reason_ui != "Follow-Up on Application" else "Follow-Up"

    submit_button = st.button("Generate Cold Email")

    if submit_button:
        try:
            raw_url = clean_url(url_input)
            loader = WebBaseLoader([raw_url])
            raw_text = loader.load().pop().page_content
            data = clean_text(raw_text)

            resume_summary = extract_text_from_pdf(resume_file) if resume_file else ""

            jobs = llm.extract_jobs(data)
            for job in jobs:
                email = llm.write_mail(
                    job=job,
                    name=name_input,
                    role=role_input,
                    about_yourself=about_yourself_input,
                    links=links_input,
                    project_showcase=project_input,
                    language=language_input,
                    reason=selected_reason_short,
                    resume=resume_summary
                )

                st.subheader(f"✉️ Cold Email for {job.get('role', 'Unknown Role')}")
                st.text_area("Your Cold Email (Edit or Copy)", value=email.strip(), height=400)

        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")

    st.markdown(
        """
        <div class='footer-text'>
            © 2025 <strong style="font-weight:400;">Abhishek</strong>. All rights reserved. |
            <a href='https://github.com/Abhishek24122000/Cold_Email_Generator' target='_blank' style="color: #BBBBBB; text-decoration: none;">GitHub</a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------
# Instantiate Chain with session key (or fallback to env inside Chain)
# ----------------------
if __name__ == "__main__":
    api_key = st.session_state.get("GROQ_API_KEY")
    chain = Chain(api_key=api_key)
    create_streamlit_app(chain, clean_text)
