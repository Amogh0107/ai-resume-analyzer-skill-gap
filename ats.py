import re

def calculate_ats_score(resume_text, skills):
    score = 0
    feedback = []

    text = resume_text.lower()

    # -----------------------
    # Name (Basic Check)
    # -----------------------
    first_line = resume_text.split("\n")[0].strip()

    if len(first_line) > 2:
        score += 10
    else:
        feedback.append("❌ Add your full name.")

    # -----------------------
    # Email
    # -----------------------
    if re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", resume_text):
        score += 10
    else:
        feedback.append("❌ Email not found.")

    # -----------------------
    # Phone
    # -----------------------
    if re.search(r"\+?\d[\d\s-]{8,}", resume_text):
        score += 10
    else:
        feedback.append("❌ Phone number missing.")

    # -----------------------
    # Education
    # -----------------------
    education_keywords = [
        "education",
        "b.tech",
        "b.e",
        "bachelor",
        "master",
        "m.tech",
        "degree",
        "university",
        "college"
    ]

    if any(word in text for word in education_keywords):
        score += 15
    else:
        feedback.append("❌ Education section missing.")

    # -----------------------
    # Skills
    # -----------------------
    if len(skills) >= 8:
        score += 20
    elif len(skills) >= 5:
        score += 15
    elif len(skills) >= 3:
        score += 10
    else:
        feedback.append("⚠ Add more technical skills.")

    # -----------------------
    # Projects
    # -----------------------
    if "project" in text or "projects" in text:
        score += 15
    else:
        feedback.append("⚠ Add project section.")

    # -----------------------
    # Experience
    # -----------------------
    experience_keywords = [
        "experience",
        "internship",
        "worked",
        "company"
    ]

    if any(word in text for word in experience_keywords):
        score += 10
    else:
        feedback.append("⚠ Add internship or experience.")

    # -----------------------
    # LinkedIn
    # -----------------------
    if "linkedin" in text:
        score += 5
    else:
        feedback.append("⚠ Add LinkedIn profile.")

    # -----------------------
    # GitHub
    # -----------------------
    if "github" in text:
        score += 5
    else:
        feedback.append("⚠ Add GitHub profile.")

    # -----------------------
    # Certifications
    # -----------------------
    certification_keywords = [
        "certificate",
        "certification",
        "certifications"
    ]

    if any(word in text for word in certification_keywords):
        score += 10
    else:
        feedback.append("⚠ Add certifications.")

    score = min(score, 100)   

    return score, feedback

print("ATS MODULE LOADED")