# main.py
import os
import streamlit as st
import fitz
from langchain_community.document_loaders import WebBaseLoader
from utils import clean_text, clean_url

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
try:
    st.cache_resource.clear()
except Exception:
    pass

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

def create_streamlit_app(llm, clean_text):
    st.markdown(
        """
        <style>
        .main-header {
            font-size: 38px;
            font-weight: 800;
            color: #FFFFFF !important;
            text-align: left;
            margin-bottom: 4px;
        }
        .subtitle {
            font-size: 16px;
            color: #DDDDDD;
            margin-top: -6px;
            margin-bottom: 10px;
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
        .small-label { font-size:13px; color:#444444; font-weight:600; margin-bottom:6px; }
        .api-status { font-size:12px; color:#bbbbbb; margin-top:8px; }
        .stButton>button { padding:6px 10px !important; font-size:13px !important; height:34px !important; }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div class='main-header'>🚀 Cold Email Generator Tool Powered by LLM (LLaMA 70B + LangChain)</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Automate professional outreach in seconds</div>", unsafe_allow_html=True)

    # -------- Groq API: default native input (no white panel), wider, prefilled from env if available --------
    env_key = os.getenv("GROQ_API_KEY", "")
    if "GROQ_API_KEY" not in st.session_state:
        st.session_state["GROQ_API_KEY"] = None

    col_input, col_buttons = st.columns([3, 1], gap="small")
    with col_input:
        st.markdown("<div class='small-label'>🔑 Groq API Key (session-only)</div>", unsafe_allow_html=True)
        api_input = st.text_input("", type="password", placeholder="paste groq-xxxx... (session only)", value=env_key, key="groq_input")
        # status below input
        if st.session_state.get("GROQ_API_KEY"):
            masked = "●" * 8
            st.markdown(f"<div class='api-status'><strong>Status:</strong> Active ({masked}) — used for LLM calls.</div>", unsafe_allow_html=True)
        elif env_key:
            st.markdown("<div class='api-status'><strong>Status:</strong> Found in environment (will be used if you don't set session key).</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='api-status'><strong>Status:</strong> No API key set. Falling back to environment if present.</div>", unsafe_allow_html=True)

    with col_buttons:
        st.write("")  # align vertically with input
        btn_col1, btn_col2 = st.columns([1,1], gap="small")
        with btn_col1:
            if st.button("Set", key="set_api"):
                if not api_input or not api_input.strip():
                    st.warning("Please paste a valid API key before setting.")
                else:
                    st.session_state["GROQ_API_KEY"] = api_input.strip()
                    st.success("API key set for this session.")
        with btn_col2:
            if st.button("Clear", key="clear_api"):
                st.session_state["GROQ_API_KEY"] = None
                st.info("API key cleared from session.")

    # ---------- Name | Role | About (side-by-side) ----------
    col_name, col_role, col_about = st.columns([1,1,1], gap="small")
    with col_name:
        name_input = st.text_input("Your Name", placeholder="Full name", key="name_input")
    with col_role:
        role_input = st.text_input("Your Role", placeholder="e.g., Data Analyst", key="role_input")
    with col_about:
        about_yourself_input = st.text_area("Tell us About Yourself", placeholder="Short intro", height=120, key="about_input")

    st.markdown("---")

    # ---------- Resume | Links | Project (one line compact) ----------
    col_resume, col_links, col_project = st.columns([1,1,1], gap="small")
    with col_resume:
        st.markdown("<div class='small-label'>Resume (PDF)</div>", unsafe_allow_html=True)
        resume_file = st.file_uploader("", type=["pdf"], key="resume_file")
    with col_links:
        st.markdown("<div class='small-label'>Links (LinkedIn / GitHub / Portfolio)</div>", unsafe_allow_html=True)
        links_input = st.text_input("", placeholder="Paste links (comma separated)", max_chars=220, key="links_input")
    with col_project:
        st.markdown("<div class='small-label'>Highlight a Project (optional)</div>", unsafe_allow_html=True)
        project_input = st.text_input("", placeholder="Project title or short note", max_chars=120, key="project_input")

    st.markdown("---")

    # ---------- Purpose (left) and Language (right) swapped as requested ----------
    col_purpose, col_language = st.columns([1,1], gap="small")
    with col_purpose:
        st.markdown("<div class='small-label'>Purpose</div>", unsafe_allow_html=True)
        selected_reason_ui = st.selectbox("", [
            "Job Application", "Internship Request", "Project Collaboration", "Service/Product Pitch",
            "Freelance Opportunity", "Appreciation & Networking", "Mentorship Request",
            "Volunteer Contribution", "Business Partnership", "Media/PR Inquiry", "Follow-Up on Application"
        ], key="reason_select")
    with col_language:
        st.markdown("<div class='small-label'>Email Language</div>", unsafe_allow_html=True)
        language_input = st.selectbox("", [
            "English", "Japanese", "Spanish", "French", "German", "Hindi", "Arabic", "Chinese", "Korean", "Russian", "Portuguese"
        ], key="language_input")

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

    st.markdown(f"**Reason Explained:** {reason_explanations[selected_reason_ui]}")
    selected_reason_short = selected_reason_ui.split(" ")[0] if selected_reason_ui != "Follow-Up on Application" else "Follow-Up"

    # ---------- Job URL and Generate ----------
    url_input = st.text_input("🌐 Job / Career Page URL", placeholder="e.g., https://company.com/careers", key="url_input")
    submit_col_left, submit_col_right = st.columns([1,1], gap="small")
    with submit_col_left:
        submit_button = st.button("Generate Cold Email", key="generate_btn")
    with submit_col_right:
        st.write("")  # keep layout balanced

    if submit_button:
        try:
            from chains import Chain
            runtime_key = st.session_state.get("GROQ_API_KEY") or env_key or None
            chain = Chain(api_key=runtime_key)

            raw_url = clean_url(url_input)
            loader = WebBaseLoader([raw_url])
            raw_text = loader.load().pop().page_content
            data = clean_text(raw_text)

            resume_summary = extract_text_from_pdf(resume_file) if resume_file else ""

            jobs = chain.extract_jobs(data)
            for job in jobs:
                email = chain.write_mail(
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

if __name__ == "__main__":
    create_streamlit_app(None, clean_text)
