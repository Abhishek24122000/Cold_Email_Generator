import streamlit as st
import fitz
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text, clean_url

st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
st.cache_resource.clear()

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

if __name__ == "__main__":
    chain = Chain()
    create_streamlit_app(chain, clean_text)
