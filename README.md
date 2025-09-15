# -------------------------------------
# Generate README.md for GitHub Project
# -------------------------------------

readme_content = """
# 🎯 AI-Powered Interview Simulator

## 📌 Project Description

The **AI-Powered Interview Simulator** is an interactive web application built with **Streamlit** and **Google Gemini AI** that simulates a real interview experience.

It dynamically generates **technical questions** using **Gemini AI** and mixes them with **predefined questions** for reliability. Candidates can type their answers, and the system evaluates performance, maintains a **leaderboard**, and generates a **professional PDF report** summarizing results.

---

## ✨ Key Features

- 🤖 **AI-Generated Questions**: Fetches unique interview questions from Google Gemini.  
- 📚 **Backup Questions**: Uses predefined questions if Gemini API is unavailable.  
- 📝 **Answer Evaluation**: Simple scoring system to check answer length & relevance.  
- 📊 **Leaderboard**: Tracks and displays top performers.  
- 📑 **PDF Report**: Generates a downloadable report with candidate’s answers and scores.  
- 🚪 **Exit & Quit Option**: Candidate can leave the interview at any stage.  
- 🔄 **Restart Interview**: Option to retake the interview anytime.  
- 🎉 **Completion Feedback**: Motivational message (“Hurray you did it!”) at the end.  

---

## 🛠 Tech Stack

- **Python** – Core language  
- **Streamlit** – Frontend & interactive web UI  
- **Google Gemini Pro API** – AI-powered question generation  
- **FPDF** – PDF report generation  
- **Session State** – Candidate progress tracking  

---

## 📂 Workflow

1. Candidate enters their **name** to start the interview.  
2. The app generates a mix of **AI-driven and predefined questions**.  
3. Candidate answers each question, with the ability to **exit/quit** anytime.  
4. Once finished, a **PDF report** is created containing:  
   - Candidate name  
   - Date & time  
   - Questions & answers  
   - Score summary  
5. Candidate’s score is added to a **leaderboard**.  
6. Candidate can **download the report** or **restart the interview**.  

---

## 🚀 Use Cases

- 🎓 **Students** – Practice mock technical interviews.  
- 🏢 **Recruiters** – Automate first-round interview screenings.  
- 📚 **Educators** – Create an interactive interview preparation tool.  
- 👨‍💻 **Developers** – Showcase AI + Streamlit project on GitHub/portfolio.  

---
