# ATS-Resume-Checker
# 📄 ATS Resume Checker

An **ATS Resume Checker** is a web application that analyzes a resume against a given job description and provides an AI-based Applicant Tracking System (ATS) evaluation.  
It helps users understand how well their resume matches a job role by highlighting matching skills, missing skills, strengths, and improvement suggestions.

---

## 🎯 Project Objective

- To simulate how an Applicant Tracking System (ATS) evaluates resumes  
- To help users improve their resumes based on job requirements  
- To practice building an AI-powered full-stack application  

---

## 🚀 Features

- Upload resume in **PDF format**
- Paste any **job description**
- Resume text extraction from PDF
- AI-based resume parsing
- AI-based job description parsing
- ATS-style comparison and scoring
- Displays structured and readable results
- Simple and user-friendly interface

---

## 🛠️ Technologies Used

### Frontend
- HTML5  
- CSS3  
- JavaScript (Fetch API)

### Backend
- Python  
- Flask  
- Google Gemini API  
- PyPDF2  

---

## 📂 Project Structure
ATS-Resume-Checker/
│
├── templates/
│ └── ats.html # Frontend UI (HTML + CSS + JS)
│
├── uploads/ # Stores uploaded resume PDFs temporarily
│
├── app.py # Flask backend application
│
├── README.md # Project documentation

---

## ⚙️ How the Project Works

1. User uploads a resume in PDF format  
2. User pastes the job description  
3. Backend extracts resume text from PDF  
4. AI parses:
   - Resume details (skills, experience, education, tools)
   - Job description requirements  
5. ATS logic compares both  
6. Final evaluation is displayed on the UI  

---

## 📊 Output Generated

- Parsed Resume Summary  
- Parsed Job Description Summary  
- ATS Match Percentage  
- Matching Skills  
- Missing Skills  
- Strengths  
- Improvement Suggestions  

---

## 🔐 Security & Notes

- API keys are handled using environment variables  
- Uploaded resumes are stored only temporarily  
- No database is used  
- Manual CORS handling is implemented  

---

## 🧪 Limitations

- Supports only text-based PDF resumes  
- Basic UI (no frontend frameworks)  
- Not optimized for very large files  

---

## 🚧 Future Enhancements

- Resume score visualization (charts)
- Skill keyword highlighting
- Support for multiple resume uploads
- Improved UI/UX
- Authentication system
- Cloud deployment

---

## 🙌 Conclusion

This project demonstrates how AI can be integrated with web applications to solve real-world problems such as resume screening and job matching.

---

✨ Built for learning, practice, and skill enhancement ✨


