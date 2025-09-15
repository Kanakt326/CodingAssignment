# 🎯 AI-Powered Interview Simulator

🚀 An interactive web application built with **Streamlit** and **Google Gemini AI** that simulates a real interview experience.

It dynamically generates technical questions using Gemini AI and mixes them with predefined questions for reliability. Candidates can type their answers, the system evaluates performance, maintains a leaderboard, and generates a professional report summarizing results.

---

## ✨ Key Features

- 🤖 **AI-Generated Questions**: Fetches unique interview questions from Google Gemini.  
- 📚 **Backup Questions**: Uses predefined Excel-related questions if Gemini API is unavailable.  
- 📝 **Answer Evaluation**: Scoring system that checks answer correctness & relevance.  
- 📊 **Leaderboard**: Tracks and displays top performers.  
- 📑 **Report Generation**: Creates a summary of candidate’s answers, score, and performance.  
- 🚪 **Exit & Quit Option**: Candidate can leave the interview at any stage.  
- 🔄 **Restart Interview**: Option to retake the interview anytime.  
- 🎉 **Completion Feedback**: Motivational message (“Hurray you did it!”) at the end.  

---

## 🛠 Tech Stack

- **Python** – Core programming language  
- **Streamlit** – Frontend & interactive web UI  
- **Google Gemini Pro API** – AI-powered question generation  
- **FPDF** – Report generation  
- **Pandas** – Leaderboard & data handling  
- **Session State** – Candidate progress tracking  

---

## 📂 Project Structure

CodingAssignment/
 ------>>  k.py # Main Streamlit file (AI-Powered Interviewer)
---

## ⚡ Workflow

1. Input candidate name in the session (input required).  
2. The app generates a mix of Gemini AI-driven and predefined questions.  
3. Candidate answers each question, with the ability to **Exit/Quit** anytime.  
4. Once finished, a performance summary is shown:  
   - Candidate name  
   - Questions & answers  
   - Correct vs incorrect responses  
   - Score summary & feedback  
5. Candidate’s score is added to the **Leaderboard**.  
6. Candidate can restart the interview anytime.  

---

## 🚀 Use Cases

- 🎓 **Students** – Practice mock technical interviews.  
- 🏢 **Recruiters** – Automate first-round screening.  
- 📚 **Educators** – Create interactive preparation tools.  
- 👨‍💻 **Developers** – Showcase an AI + Streamlit project on GitHub/portfolio.  

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/Kanakt326/CodingAssignment.git
cd CodingAssignment
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit app:

bash
Copy code
streamlit run k.py
📜 License
This project is for educational & evaluation purposes.
You may extend and adapt it for your own projects.

