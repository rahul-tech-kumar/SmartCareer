# ---------------------------------------------------------------------
import streamlit as st
from openai import OpenAI
import pdfplumber
import docx2txt

# ---------------------------
# GROQ CLIENT
# ---------------------------
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# ---------------------------
# HELPER: EXTRACT RESUME TEXT
# ---------------------------
def extract_resume_text(uploaded_file):
    if uploaded_file is None:
        return ""

    if uploaded_file.type == "application/pdf":
        text = ""
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""
        return text

    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(uploaded_file)

    elif uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8")

    else:
        return ""


# ---------------------------
# FUNCTION TO GENERATE REPORT
# ---------------------------
def generate_career_plan(edu, skills, interests, goal, resume_text):
    prompt = f"""
You are SmartCareer, an AI-based Career Mentor.

Use the following details AND resume text to generate a fully personalized career path.

----------------------------------------
Education: {edu}
Skills: {skills}
Interests: {interests}
Career Goal: {goal}

Resume Content:
{resume_text}
----------------------------------------

Now generate:

### 1. Resume-Based Profile Summary  
(Short, professional summary.)

### 2. Top 5 Recommended Courses  
- Course name  
- Platform  
- Why important  
- Skills learned  

### 3. 30-Day Learning Roadmap  
(Week-by-week plan)

### 4. Skill Gap Analysis  
(What user is missing, how to improve)

### 5. Job Roles User Becomes Eligible For  
(List 5-7 roles)
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


# ---------------------------
# STREAMLIT UI
# ---------------------------
st.set_page_config(page_title="SmartCareer AI Mentor", layout="wide")

st.title("🎓 SmartCareer – AI Learning & Career Recommender")
st.write("Upload your resume + enter details to get a full AI career plan.")

st.markdown("---")

# ---------------------------
# INPUT SECTION
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    education = st.text_input("📘 Education", placeholder="e.g., BTech in IT, BSc CS")
    skills = st.text_area("🛠 Technical Skills", placeholder="Python, SQL, HTML, ML")

with col2:
    interests = st.text_area("🎯 Interests", placeholder="Web Dev / Data Science / AI-ML")
    goal = st.text_input("🚀 Career Goal", placeholder="Full Stack Developer / Data Analyst")

st.markdown("### 📄 Upload Resume")
uploaded_resume = st.file_uploader("Upload PDF / DOCX / TXT", type=["pdf", "docx", "txt"])

st.markdown("---")

# ---------------------------
# BUTTON ACTION
# ---------------------------
if st.button("Generate SmartCareer Report"):
    if not education.strip() or not skills.strip():
        st.error("⚠️ Please fill at least Education and Skills.")
    else:
        with st.spinner("⏳ Extracting resume & generating report..."):

            resume_text = extract_resume_text(uploaded_resume)

            report = generate_career_plan(
                education,
                skills,
                interests,
                goal,
                resume_text
            )

        st.success("✅ Your SmartCareer Report is Ready!")
        st.markdown("## 📄 SmartCareer Report")
        st.markdown(report)

        st.markdown("---")
        st.info("🎉 You can take screenshots or copy this text for submission.")
