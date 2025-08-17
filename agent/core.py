import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Use the latest available Gemini model
MODEL_NAME = "models/gemini-1.5-flash"   # or "models/gemini-1.5-pro" if you prefer better quality

def ask_ai(question: str) -> str:
    """
    Sends a question to the Gemini model and returns the AI's response.
    """
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(question)
        return response.text if response and response.text else "No response from AI."
    except Exception as e:
        return f"Error: {str(e)}"
