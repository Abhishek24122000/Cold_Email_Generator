import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:

    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY"),
            model_name="llama3-70b-8192"
        )

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})

        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, name, role, about_yourself, links, project_showcase="", language="English", reason="Job", resume=""):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job_description}

            ### INSTRUCTION:
            You are {name_input}, a {role_input}.
            {about_yourself_input}.
            Reason for writing this email: {email_reason}.
            Include relevant links from: {link_list}
            {project_section}
            {resume_section}
            Write the email in {selected_language}.
            If the language is Japanese, ensure to use formal business-level Keigo (敬語).
            Make it personalized, clear, and professional.

            ### EMAIL (NO PREAMBLE):
            """
        )

        project_section = f"You would also like to highlight the following project as a demonstration of your skills: {project_showcase}" if project_showcase else ""
        resume_section = f"Use this resume summary to help personalize the email:\n{resume}" if resume else ""

        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "link_list": links,
            "name_input": name,
            "role_input": role,
            "about_yourself_input": about_yourself,
            "project_section": project_section,
            "selected_language": language,
            "email_reason": reason,
            "resume_section": resume_section
        })
        return res.content

if __name__ == "__main__":
    groq_api_key = os.getenv("GROQ_API_KEY")
    print("GROQ Key used:", groq_api_key)
