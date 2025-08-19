from flask import Flask, jsonify
from agent.core import ask_ai

from db import save_result
from datetime import datetime
import json

# Create Flask app
app = Flask(__name__)

@app.route("/daily", methods=["GET"])
def daily_questions():
    # Ask Gemini to generate fresh questions daily
    prompt = """
    Generate 5 placement practice questions across categories:
    1. Aptitude
    2. Reasoning / Puzzles
    3. Coding (Python/Java/DSA)
    4. Computer Science Fundamentals
    5. HR/Communication

    For each question, also provide the correct answer.
    Format the output strictly as JSON with fields:
    [
      {"question": "...", "answer": "...", "topic": "..."}
    ]
    """

    response = ask_ai(prompt)

    # If Gemini responds as text, try to load JSON
    try:
        questions = json.loads(response)
    except:
        return jsonify({"error": "AI returned non-JSON", "raw": response})

    results = []
    for item in questions:
        q = item.get("question")
        ans = item.get("answer")
        topic = item.get("topic", "General")
        score = 7
        save_result(q, ans, topic, score, datetime.now())
        results.append({
            "question": q,
            "answer": ans,
            "topic": topic,
            "score": score
        })

    return jsonify({
        "date": datetime.now().strftime("%Y-%m-%d"),
        "daily_set": results
    })

if __name__ == "__main__":
    app.run(debug=True)
