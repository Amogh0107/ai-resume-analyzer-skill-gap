import streamlit as st

import plotly.express as px

import pandas as pd

from parser import extract_resume

from skills import extract_skills

from ats import calculate_ats_score 

from gap_analysis import JOB_DATABASE, analyze_skill_gap

from job_recommendation import recommend_jobs

from learning_roadmap import generate_learning_roadmap

# Page Config

st.set_page_config(

page_title=" Resume Analyzer",

page_icon="📄",

layout="wide"

)

# Load CSS

with open("style.css") as f:

    st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

# Hero

st.markdown("""

<div class="hero">

<h1>📄  Resume Analyzer</h1>

<p>Analyze • Improve • Get Hired 🚀</p>

</div>

""",unsafe_allow_html=True)

uploaded_file=st.file_uploader(

"Upload Resume",

type=["pdf"]

)

selected_job = st.selectbox(
    "🎯 Select Your Target Job Role",
    list(JOB_DATABASE.keys())
)

if uploaded_file:

    resume, pages = extract_resume(uploaded_file)
    skills = extract_skills(resume)

    ats_score, feedback = calculate_ats_score(resume, skills)

    matched_skills, missing_skills, match_percentage = analyze_skill_gap(
        skills,
        selected_job
    )

    recommended_jobs = recommend_jobs(skills)
    learning_plan = generate_learning_roadmap(missing_skills)

    col1, col2, col3, col4 = st.columns(4)

    

    # <-- SAME INDENTATION AS col1
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "📄 Resume Analysis",
        "🎯 ATS Analysis",
        "💼 Career Analysis",
        "📚 Learning Roadmap",
        "📊 Analytics"
    ])



    with tab1:
        left, right = st.columns([2, 1])

        with left:
            

            st.markdown('<div class="section">📄 Resume Preview</div>',unsafe_allow_html=True)

            st.markdown(f'<div class="resume">{resume}</div>',unsafe_allow_html=True)

        with right:

            st.markdown('<div class="section">🎯 Skills Found</div>',unsafe_allow_html=True)

            if skills:

                badges=""

                for skill in skills:

                    badges+=f'<span class="badge">{skill}</span>'

                st.markdown(badges,unsafe_allow_html=True)

            else:

                st.warning("No skills detected.")
        st.markdown("---")

    with tab2:
        st.subheader("🎯 ATS Resume Score")

        st.progress(ats_score / 100)

        st.metric("ATS Score", f"{ats_score}/100")

        if ats_score >= 80:
            st.success("Excellent Resume ⭐")
        elif ats_score >= 60:
            st.warning("Good Resume 👍")
        else:
            st.error("Resume Needs Improvement")

        st.subheader("💡 Suggestions")

        for item in feedback:
            st.write(item)

        st.markdown("---")

        st.subheader("🎯 Skill Gap Analysis")

        st.write(f"**Target Job Role:** {selected_job}")

        # Match Percentage
        st.progress(match_percentage / 100)

        if match_percentage >= 80:
            st.success(f"🎉 Skill Match: {match_percentage}%")
        elif match_percentage >= 60:
            st.warning(f"👍 Skill Match: {match_percentage}%")
        else:
            st.error(f"⚠ Skill Match: {match_percentage}%")

    # Matching Skills

    with tab3:
        st.markdown("### ✅ Matching Skills")

        if matched_skills:
            matched_html = ""
            for skill in matched_skills:
                matched_html += f'<span class="badge">{skill}</span>'
            st.markdown(matched_html, unsafe_allow_html=True)
        else:
            st.info("No matching skills found.")

        # Missing Skills
        st.markdown("### ❌ Missing Skills")

        if missing_skills:
            missing_html = ""
            for skill in missing_skills:
                missing_html += f'<span class="badge" style="background:#DC2626;">{skill}</span>'
            st.markdown(missing_html, unsafe_allow_html=True)
        else:
            st.success("🎉 No missing skills! Great job!")
        st.markdown("---")


        st.subheader("🤖 Job Recommendations and Career gudience ")

        for index, job in enumerate(recommended_jobs, start=1):

            if index == 1:
                medal = "🥇"
            elif index == 2:
                medal = "🥈"
            else:
                medal = "🥉"
                

            st.markdown(
                f"""
                <div style="
                    background:#1E293B;
                    border-radius:12px;
                    padding:15px;
                    margin-bottom:10px;
                    border-left:5px solid #3B82F6;
                ">
                    <h4>{medal} {job['job']}</h4>
                    <p><b>Match Score:</b> {job['match']}%</p>
                    <p>{job['matched']} / {job['total']} required skills matched</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    with tab4:

        st.markdown("---")

        st.subheader("📚 Learning Roadmap")

        if learning_plan:

            for item in learning_plan:

                with st.container(border=True):

                    st.subheader(f"📘 {item['skill']}")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write(f"**🎯 Priority:** {item['priority']}")
                        st.write(f"**📈 Level:** {item['level']}")
                        st.write(f"**⏳ Duration:** {item['duration']}")

                    with col2:
                        st.write(f"**🏢 Platform:** {item['platform']}")

                    st.write("### 📝 Description")
                    st.write(item["description"])

                    st.write("### 🌐 Learning Resources")

                    if item.get("resource"):
                        st.link_button("📘 Official Documentation", item["resource"])

                    if item.get("youtube"):
                        st.link_button("🎥 Watch YouTube Course", item["youtube"])

                    if item.get("practice") and item["practice"] != "Not Available":
                        st.link_button("💻 Practice Platform", item["practice"])

                    st.info(f"💰 **Paid Course:** {item.get('paid_course', 'Free Resources Available')}")

            else:

                st.success("🎉 Excellent! No learning roadmap required.")

    with tab5:

        st.subheader("📊 Resume Analytics Dashboard")

        # ---------- Resume Statistics ----------
        total_words = len(resume.split())
        total_characters = len(resume)
        total_skills = len(skills)

        resume_strength = round(
            (ats_score + match_percentage) / 2
        )

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📄 Pages", pages)

        with col2:
            st.metric("📝 Words", total_words)

        with col3:
            st.metric("💻 Skills", total_skills)

        with col4:
            st.metric("💪 Resume Strength", f"{resume_strength}%")

        st.markdown("---")
        st.subheader("🥧 Skill Distribution")

        skill_data = pd.DataFrame({
            "Category": ["Matched Skills", "Missing Skills"],
            "Count": [len(matched_skills), len(missing_skills)]
        })

        fig = px.pie(
            skill_data,
            values="Count",
            names="Category",
            hole=0.45,
            title="Matched vs Missing Skills"
        )

        fig.update_traces(textinfo="percent+label")

        st.plotly_chart(fig, use_container_width=True)

        st.subheader("📈 Resume Performance")

        performance = pd.DataFrame({
            "Metric": [
                "ATS Score",
                "Skill Match",
                "Resume Strength"
            ],
            "Score": [
                ats_score,
                match_percentage,
                resume_strength
            ]
        })

        fig = px.bar(
            performance,
            x="Metric",
            y="Score",
            text="Score",
            title="Resume Performance Metrics"
        )

        fig.update_layout(yaxis_range=[0, 100])

        st.plotly_chart(fig, use_container_width=True)
        st.subheader("🚀 Career Readiness")

        career_score = round(
            (ats_score + match_percentage + resume_strength) / 3
        )

        st.progress(career_score / 100)

        if career_score >= 85:
            st.success(f"🎉 Career Ready ({career_score}%)")
        elif career_score >= 70:
            st.warning(f"👍 Almost Ready ({career_score}%)")
        else:
            st.error(f"⚠ Needs Improvement ({career_score}%)")