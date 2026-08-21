import streamlit as st
from parser import extract_resume
from skills import extract_skills


def load_resume(uploaded_file):
    """
    Load resume once and store all extracted data
    in Streamlit Session State.
    """

    if uploaded_file is not None:

        resume, pages = extract_resume(uploaded_file)

        skills = extract_skills(resume)

        st.session_state.resume = resume
        st.session_state.pages = pages
        st.session_state.skills = skills
        st.session_state.resume_uploaded = True


def get_resume():

    return st.session_state.get("resume", "")


def get_pages():

    return st.session_state.get("pages", 0)


def get_skills():

    return st.session_state.get("skills", [])


def resume_exists():

    return st.session_state.get("resume_uploaded", False)