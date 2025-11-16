# 📘 SmartCareer – AI Resume-Based Career Mentor

SmartCareer is an AI-powered career guidance application built using Streamlit and Groq API.
The app allows users to upload their resume, enter their skills, interests, and goals — and instantly generates a personalized career roadmap, skill gap analysis, recommended courses, and eligible job roles.

# 🚀 Features

✅ Upload PDF, DOCX, or TXT resume
✅ Extracts text using pdfplumber & docx2txt
✅ AI-generated Career Plan using Groq 
✅ Includes:

# Profile Summary

- Top 5 Recommended Courses

- 30-Day Learning Roadmap

- Skill Gap Analysis

- Eligible Job Roles

- Resume-aware suggestions

# 🛠 Tech Stack

- Python

- Streamlit

- Groq API (OpenAI-compatible client)

- pdfplumber (PDF extraction)

- docx2txt (DOCX extraction)

# 📦 Installation

- Clone the repository:

- git clone https://github.com/yourusername/smartcareer.git
- cd smartcareer


- Install dependencies:

- pip install -r requirements.txt


# 🔑 Environment Variables

- Create a .env file with:

- GROQ_API_KEY=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



# ▶️ Run the App
- streamlit run app.py

# 📄 Code Structure
📁 SmartCareer
│── app.py               # Main Streamlit app
│── requirements.txt     # Dependencies
│── README.md            # Project documentation

# 🧠 How It Works
## Upload Resume

- App supports:

- PDF → extracted using pdfplumber

- DOCX → extracted using docx2txt

- TXT → read directly

## User Inputs

- Education

- Skills

- Interests

- Career Goal

## AI Processing

- Sends everything to Groq Llama-3.1 model with a structured prompt.

## Output

- Career Summary

- Courses

- 30-Day Plan

- Skill Gap Analysis

- Suitable Roles

# 📚 Example Output
### 1. Resume-Based Profile Summary:
A highly motivated IT graduate with strong foundations in Python...

### 2. Top 5 Courses
1. Python for Everyone – Coursera
2. SQL Advanced – Udemy
...

### 3. 30-Day Roadmap
Week 1: Python + DSA  
Week 2: SQL + Projects  
...

### 4. Skill Gaps
- System Design
- Cloud Basics  
...

### 5. Eligible Job Roles
- Python Developer  
- Data Analyst  
- ML Engineer (Junior)  
...

# 🌐 Deployment Guide (Streamlit Cloud)

- Deploy App : https://smartcareer-5rxuafpda3akn4bba4zxar.streamlit.app/
- Deploy 🎉

# 🤝 Contributing

Pull requests are welcome.

🛡 License

This project is under the MIT License.

🙌 Author

SmartCareer AI App
Developed by Rahul
For academic, career & portfolio project use.
