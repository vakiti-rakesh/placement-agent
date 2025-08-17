Placement Agent 🤖🎯

An AI-powered daily placement preparation assistant that automatically generates and delivers practice questions across Aptitude, Reasoning, Coding, Computer Science, and HR.
Built with Python (Flask), Google Generative AI API, and a SQLite database, this project helps students consistently prepare for interviews without manual effort.

🚀 Features

✅ Daily Auto-Generated Questions (5 categories: Aptitude, Reasoning, Coding, CS, HR)

✅ AI-Powered Question Generation using Google Gemini API

✅ SQLite Database for saving questions, answers, and scores

✅ Flask API (/daily endpoint) to fetch fresh questions anytime

✅ Automated Scheduling to get questions daily without manual trigger

🛠️ Tech Stack

Backend: Python, Flask

AI: Google Generative AI (google-generativeai SDK)

Database: SQLite

Scheduler: APScheduler (for daily automation)

Version Control: Git + GitHub

📂 Project Structure
placement-agent/
├── agent/
│   ├── app.py         # Flask API
│   ├── core.py        # AI logic (Gemini integration)
│   ├── db.py          # SQLite helpers
│   ├── requirements.txt
│   └── .env           # API keys (ignored in git)
├── README.md          # Documentation

⚙️ Setup & Installation

Clone the repo

git clone https://github.com/vakiti-rakesh/placement-agent.git
cd placement-agent/agent


Create virtual environment & activate

python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate # On Mac/Linux


Install dependencies

pip install -r requirements.txt


Add your API key
Create .env file in agent/:

GOOGLE_API_KEY=your_api_key_here


Run the Flask server

python app.py

🔥 Usage

Start the server → Visit: http://127.0.0.1:5000/daily

You’ll get 5 fresh placement questions daily in JSON format:

{
  "date": "2025-08-16",
  "daily_set": [
    {"question": "...", "answer": "...", "topic": "Aptitude"},
    {"question": "...", "answer": "...", "topic": "Reasoning"}
  ]
}

📈 Future Enhancements

📩 Email/Telegram delivery of daily questions

🌐 Web dashboard to view progress and past questions

📊 Analytics for performance tracking

👨‍💻 Author

Rakesh Vakiti

LinkedIn

GitHub

⭐ Contribute

If you like this project, don’t forget to star ⭐ the repo!
