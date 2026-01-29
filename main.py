
import os
from flask import Flask, request, jsonify, render_template
from google import genai
import PyPDF2

# ==============================
# CONFIG
# ==============================
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 🔐 API KEY (USE ENV VARIABLE)
# Run in terminal once:
# setx GEMINI_API_KEY "your_api_key_here"
client = genai.Client(api_key=os.getenv("Your Api key"))

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ==============================
# MANUAL CORS (NO flask-cors)
# ==============================
@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response

# ==============================
# HOME ROUTE (TEST SERVER)
# ==============================
@app.route("/", methods=["GET"])
def home():
    return render_template("ats.html")

# ==============================
# PDF TEXT EXTRACTION
# ==============================
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# ==============================
# RESUME PARSER (GEMINI)
# ==============================
def parse_resume(resume_text):
    prompt = f"""
You are a resume parser.

Extract clearly:
- Skills
- Experience summary
- Education
- Tools & technologies

Resume:
{resume_text}

Return in bullet points.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# ==============================
# JOB DESCRIPTION PARSER
# ==============================
def parse_job_description(jd_text):
    prompt = f"""
Extract clearly:
- Required skills
- Responsibilities
- Preferred qualifications

Job Description:
{jd_text}

Return in bullet points.
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# ==============================
# ATS MATCHING
# ==============================
def ats_match(parsed_resume, parsed_jd):
    prompt = f"""
You are an Applicant Tracking System (ATS).

Compare the resume and job description.

Resume:
{parsed_resume}

Job Description:
{parsed_jd}

Provide:
1. Match percentage (0-100)
2. Matching skills
3. Missing skills
4. Strengths
5. Improvement suggestions
"""
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text

# ==============================
# ANALYZE ROUTE
# ==============================
@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "Resume PDF is required"}), 400

    resume_file = request.files["resume"]
    job_description = request.form.get("job_description")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    # Save PDF
    pdf_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_file.filename)
    resume_file.save(pdf_path)

    # Extract resume text
    resume_text = extract_text_from_pdf(pdf_path)

    if not resume_text.strip():
        return jsonify({"error": "Could not extract text from PDF"}), 400

    # Gemini processing
    parsed_resume = parse_resume(resume_text)
    parsed_jd = parse_job_description(job_description)
    ats_result = ats_match(parsed_resume, parsed_jd)

    return jsonify({
        "parsed_resume": parsed_resume,
        "parsed_job_description": parsed_jd,
        "ats_result": ats_result
    })

# ==============================
# RUN SERVER
# ==============================
if __name__ == "__main__":
    print("🚀 ATS Backend Started")
    app.run(debug=True, port=5000)

