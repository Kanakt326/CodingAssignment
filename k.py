# ------------------------------
# AI-Powered Excel Mock Interviewer with Gemini-first Questions & Dynamic Count
# Exit/Quit Buttons Everywhere with Unique Keys
# ------------------------------

import streamlit as st
import json
import random
import pandas as pd
import os
import google.generativeai as genai

# ------------------------------
# Predefined Questions Fallback
# ------------------------------
PREDEFINED_QUESTIONS = [
    {"question": "Which function is used to sum a range of cells in Excel?",
     "options": ["SUM", "AVERAGE", "COUNT", "IF"], "answer": "SUM"},
    {"question": "What is the shortcut for 'Copy' in Excel?",
     "options": ["Ctrl+C", "Ctrl+V", "Ctrl+X", "Ctrl+Z"], "answer": "Ctrl+C"},
    {"question": "Which function removes extra spaces from text?",
     "options": ["TRIM", "CLEAN", "REMOVE", "SPACE"], "answer": "TRIM"},
    {"question": "Which Excel feature allows you to remove duplicates?",
     "options": ["Data Validation", "Conditional Formatting", "Remove Duplicates", "Sort"], "answer": "Remove Duplicates"},
    {"question": "Which function calculates the average of a range of numbers?",
     "options": ["SUM", "AVERAGE", "MEDIAN", "COUNT"], "answer": "AVERAGE"}
]

# ------------------------------
# Streamlit Layout
# ------------------------------
st.set_page_config(page_title="AI-Powered Excel Interview", page_icon="🧑‍💻", layout="centered")
st.title("🧑‍💻 AI-Powered Excel Mock Interviewer")
st.write("🚀 Simulate a real Excel interview. Scores and leaderboard are saved automatically.")

# ------------------------------
# Top-level Global Exit / Quit Buttons
# ------------------------------
col_exit, col_quit = st.columns(2)
with col_exit:
    if st.button("Exit Anytime", key="top_exit"):
        st.stop()
with col_quit:
    if st.button("Quit Interview", key="top_quit"):
        st.session_state.current_index = st.session_state.get("num_questions", 10)
        st.stop()

# ------------------------------
# Candidate Name
# ------------------------------
if "candidate_name" not in st.session_state:
    name_input = st.text_input("Enter your name to start the interview:")
    if st.button("Start Interview", key="start_interview") and name_input.strip():
        st.session_state.candidate_name = name_input.strip()
        st.stop()
else:
    st.write(f"Candidate: **{st.session_state.candidate_name}**")

# ------------------------------
# Gemini API Key Input (Optional)
# ------------------------------
if "gemini_configured" not in st.session_state:
    st.session_state.gemini_configured = False

if not st.session_state.gemini_configured:
    api_key_input = st.text_input("🛠 Enter your Gemini API Key (Optional):", type="password")
    if st.button("Configure API", key="configure_api"):
        if api_key_input.strip():
            try:
                genai.configure(api_key=api_key_input.strip())
                st.session_state.gemini_configured = True
                st.success("Gemini API configured successfully!")
            except Exception as e:
                st.error(f"Failed to configure Gemini API: {e}")
        else:
            st.session_state.gemini_configured = False
            st.info("Skipping Gemini API. Predefined questions will be used.")

# ------------------------------
# Number of Questions Input
# ------------------------------
if "num_questions" not in st.session_state:
    st.session_state.num_questions = st.number_input(
        "Select number of questions for the interview:",
        min_value=5,
        max_value=50,
        value=10,
        step=1
    )

# ------------------------------
# Helper: Gemini-first Question Fetch
# ------------------------------
def get_question():
    if not st.session_state.gemini_configured:
        return random.choice(PREDEFINED_QUESTIONS)

    max_retries = 2
    for attempt in range(max_retries):
        try:
            response = genai.responses.create(
                model="gemini-1.5-pro-latest",
                input="""
                Generate an intermediate-level Excel multiple-choice question.
                Return a JSON object with "question", "options" (list of 4), and "answer" fields.
                """
            )
            text = response.output_text.strip()
            q_json = json.loads(text)
            if "question" in q_json and "options" in q_json and "answer" in q_json:
                return q_json
        except Exception as e:
            st.warning(f"Gemini attempt {attempt+1} failed: {e}")

    st.info("Using predefined question as fallback.")
    return random.choice(PREDEFINED_QUESTIONS)

# ------------------------------
# Initialize Session State
# ------------------------------
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "answers" not in st.session_state:
    st.session_state.answers = []

# ------------------------------
# Load Questions
# ------------------------------
if not st.session_state.questions:
    for _ in range(st.session_state.num_questions):
        st.session_state.questions.append(get_question())

# ------------------------------
# Display Current Question
# ------------------------------
if st.session_state.current_index < len(st.session_state.questions):
    q = st.session_state.questions[st.session_state.current_index]
    st.write(f"**Question {st.session_state.current_index + 1}:** {q['question']}")
    selected = st.radio("Choose your answer:", q["options"], key=f"radio_{st.session_state.current_index}")

    # Question-level buttons with unique keys
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Next", key=f"next_{st.session_state.current_index}"):
            st.session_state.answers.append(selected)
            if selected == q["answer"]:
                st.session_state.score += 1
            st.session_state.current_index += 1
            st.stop()
    with col2:
        if st.button("Quit", key=f"quit_{st.session_state.current_index}"):
            st.session_state.current_index = len(st.session_state.questions)
            st.stop()
    with col3:
        if st.button("Exit Anytime", key=f"exit_{st.session_state.current_index}"):
            st.session_state.current_index = len(st.session_state.questions)
            st.stop()

# ------------------------------
# Final Score & Feedback
# ------------------------------
else:
    st.balloons()
    st.success("🎉 Interview Complete!")
    st.write(f"**Candidate:** {st.session_state.candidate_name}")
    st.write(f"**Score:** {st.session_state.score}/{len(st.session_state.questions)}")

    st.write("**Answers & Feedback:**")
    for idx, ans in enumerate(st.session_state.answers):
        correct = st.session_state.questions[idx]['answer']
        feedback = "✅ Correct" if ans == correct else f"❌ Incorrect, Correct: {correct}"
        st.write(f"Q{idx+1}: {ans} → {feedback}")

    # Performance Summary
    percentage = (st.session_state.score / len(st.session_state.questions)) * 100
    st.write("**Performance Summary:**")
    if percentage >= 80:
        st.write("Excellent! You have strong Excel skills.")
    elif percentage >= 50:
        st.write("Good. Decent Excel knowledge but some gaps to improve.")
    else:
        st.write("Needs Improvement. Consider revising Excel basics and practicing more.")

    # ------------------------------
    # Save Result to Leaderboard (CSV)
    # ------------------------------
    leaderboard_file = "leaderboard.csv"

    if os.path.exists(leaderboard_file):
        leaderboard = pd.read_csv(leaderboard_file)
    else:
        leaderboard = pd.DataFrame(columns=["Candidate", "Score", "Percentage"])

    new_entry = {
        "Candidate": st.session_state.candidate_name,
        "Score": st.session_state.score,
        "Percentage": percentage
    }
    leaderboard = pd.concat([leaderboard, pd.DataFrame([new_entry])], ignore_index=True)
    leaderboard.to_csv(leaderboard_file, index=False)

    st.write("**Leaderboard (Top Performers):**")
    st.dataframe(leaderboard.sort_values(by="Score", ascending=False).reset_index(drop=True))

    # Exit/Quit at final summary with unique keys
    col_exit_final, col_quit_final = st.columns(2)
    with col_exit_final:
        if st.button("Exit Anytime", key="final_exit"):
            st.stop()
    with col_quit_final:
        if st.button("Quit Interview", key="final_quit"):
            st.stop()
