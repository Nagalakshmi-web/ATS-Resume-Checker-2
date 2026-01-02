📄 ATS Resume Checker (AI-Powered)

An AI-powered Applicant Tracking System (ATS) Resume Checker that analyzes a candidate’s resume against a job description and provides:

Resume parsing

Job description parsing

ATS match percentage

Skill match & missing skills

Improvement suggestions

This project uses Flask (backend), HTML/CSS/JavaScript (frontend), PDF parsing, and Google Gemini AI.

🚀 Features

📂 Upload resume in PDF format

📝 Paste job description

🤖 AI-powered resume & JD parsing using Gemini

📊 ATS match analysis:

Match percentage

Matching skills

Missing skills

Strengths

Suggestions to improve resume

🌐 Simple & clean web interface

🛠️ Tech Stack
Frontend

HTML

CSS

JavaScript (Fetch API)

Backend

Python

Flask

PyPDF2 (PDF text extraction)

AI

Google Gemini (gemini-2.5-flash)

📁 Project Structure
ATS
│
├── templates/
│   └── ats.html          # Frontend UI
│
├── uploads/              # Uploaded resumes (PDF)
│
├── main.py      # Flask backend
│
├── README.md             # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/ATS-Resume-Checker.git
cd ATS-Resume-Checker

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install flask PyPDF2 google-genai

4️⃣ Set Gemini API Key

Create an environment variable:

Windows

setx GEMINI_API_KEY "AIzaSyAUfsJKfPjNVHiAmznLOHelfEGswRs2EyU"


Restart terminal after setting it.

▶️ Run the Application
python app.py


You should see:

🚀 ATS Backend Started
Running on http://127.0.0.1:5000/

🌐 How to Use

Open browser and go to:

http://127.0.0.1:5000/


Upload your resume PDF

Paste the job description

Click Analyze Resume

View:

Parsed Resume

Parsed Job Description

ATS Result & Suggestions

📌 API Endpoint
POST /analyze

Request

resume → PDF file

job_description → Text

Response (JSON)

{
  "parsed_resume": "...",
  "parsed_job_description": "...",
  "ats_result": "..."
}

🔒 Notes & Limitations

Works best with text-based PDFs (not scanned images)

Gemini API key is required

Not deployed yet (runs locally)

🌱 Future Improvements

Resume score visualization

Keyword highlighting

Authentication & user history

Deployment using Render / Railway

Support for DOCX resumes

👩‍💻 Author

Yedururi Guru Nagalakshmi
B.Tech (ECE) | AI & Web Development Enthusiast

⭐ If you like this project

Give it a ⭐ on GitHub and feel free to fork!
