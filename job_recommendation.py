from gap_analysis import JOB_DATABASE


def recommend_jobs(user_skills):
    """
    Recommend the top matching IT jobs based on extracted skills.
    """

    user_skills_lower = {skill.lower() for skill in user_skills}

    recommendations = []

    for job, required_skills in JOB_DATABASE.items():

        required_lower = {skill.lower() for skill in required_skills}

        matched = user_skills_lower.intersection(required_lower)

        percentage = round((len(matched) / len(required_skills)) * 100)

        recommendations.append({
            "job": job,
            "match": percentage,
            "matched": len(matched),
            "total": len(required_skills)
        })

    recommendations.sort(key=lambda x: x["match"], reverse=True)

    return recommendations[:3]

