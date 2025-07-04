import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from utils import clean_text

st.cache_resource.clear()

def create_streamlit_app(llm, clean_text):
    st.title("📧 Cold Mail Generator")

    url_input = st.text_input("🌐 Enter the Job/Career Page URL:", value=" ")
    name_input = st.text_input("🙋 Your Name:", value=" ")
    role_input = st.text_input("💼 Your Role:", value=" ")
    about_yourself_input = st.text_area("🧠 Tell us About Yourself:", value=" ")
    links_input = st.text_area("🔗 Paste your LinkedIn, GitHub, or portfolio links here:")
    project_input = st.text_area("🛠️ Mention a project you'd like to showcase (optional):")

    submit_button = st.button("🚀 Generate Cold Email")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            raw_text = loader.load().pop().page_content
            data = clean_text(raw_text)

            jobs = llm.extract_jobs(data)
            for job in jobs:
                email = llm.write_mail(
                    job=job,
                    name=name_input,
                    role=role_input,
                    about_yourself=about_yourself_input,
                    links=links_input,
                    project_showcase=project_input
                )
                st.subheader(f"✉️ Cold Email for {job.get('role', 'Unknown Role')}")
                st.code(email, language='markdown')

        except Exception as e:
            st.error(f"❌ An Error Occurred: {e}")

if __name__ == "__main__":
    chain = Chain()
    st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")
    create_streamlit_app(chain, clean_text)
