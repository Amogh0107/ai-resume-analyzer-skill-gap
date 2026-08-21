JOB_DATABASE = {

   

    "Python Developer": [
        "Python", "SQL", "Git", "Flask", "Django", "FastAPI", "Docker", "AWS"
    ],

    "Java Developer": [
        "Java", "Spring Boot", "Hibernate", "SQL", "Git", "Maven", "Docker"
    ],

    "C++ Developer": [
        "C++", "OOP", "Data Structures", "Algorithms", "Git"
    ],

    "Frontend Developer": [
        "HTML", "CSS", "JavaScript", "React", "Bootstrap", "Git", "Figma"
    ],

    "Backend Developer": [
        "Python", "Java", "Node.js", "SQL", "MongoDB", "Docker", "REST API"
    ],

    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript", "React", "Node.js", "MongoDB", "SQL", "Git"
    ],

    "Web Developer": [
        "HTML", "CSS", "JavaScript", "Bootstrap", "Git"
    ],

    "MERN Stack Developer": [
        "MongoDB", "Express.js", "React", "Node.js", "JavaScript", "Git"
    ],

    "Django Developer": [
        "Python", "Django", "SQL", "Git", "HTML", "CSS"
    ],

    "Flask Developer": [
        "Python", "Flask", "SQL", "Git", "REST API"
    ],

    "FastAPI Developer": [
        "Python", "FastAPI", "REST API", "SQL", "Docker"
    ],

    "React Developer": [
        "React", "JavaScript", "HTML", "CSS", "Git"
    ],

    "Node.js Developer": [
        "Node.js", "Express.js", "MongoDB", "JavaScript", "REST API"
    ],

    "UI Developer": [
        "HTML", "CSS", "JavaScript", "Bootstrap", "Figma"
    ],

    "API Developer": [
        "Python", "FastAPI", "Flask", "REST API", "Postman"
    ],

    "Data Analyst": [
        "Python", "SQL", "Excel", "Power BI", "Tableau", "Pandas", "NumPy"
    ],

    "BI Developer": [
        "Power BI", "SQL", "Excel", "Tableau"
    ],

    "Data Scientist": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "Pandas",
        "NumPy",
        "TensorFlow",
        "PyTorch",
        "Statistics"
    ],

    "ML Engineer": [
        "Python",
        "Machine Learning",
        "TensorFlow",
        "PyTorch",
        "SQL"
    ],

    "AI Developer": [
        "Python",
        "Machine Learning",
        "Deep Learning",
        "TensorFlow",
        "PyTorch",
        "Git"
    ],

    "Cloud Developer": [
        "AWS",
        "Azure",
        "Docker",
        "Linux",
        "Git"
    ],

    "Software Engineer": [
        "Python",
        "Java",
        "C++",
        "Git",
        "OOP",
        "Data Structures",
        "Algorithms",
        "SQL"
    ],

    "SDE": [
        "Python",
        "Java",
        "C++",
        "Git",
        "Data Structures",
        "Algorithms",
        "SQL"
    ]
}

def analyze_skill_gap(user_skills, target_job):

    required = JOB_DATABASE[target_job]

    found = []
    missing = []

    # Convert extracted skills to lowercase for comparison
    user_skills_lower = [skill.lower() for skill in user_skills]

    for skill in required:
        if skill.lower() in user_skills_lower:
            found.append(skill)
        else:
            missing.append(skill)

    match = int((len(found) / len(required)) * 100)

    return found, missing, match