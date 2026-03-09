from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


def summarize_text(text: str):

    prompt = f"""
    Summarize the following text in 3 sentences.

    Text:
    {text}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        # Fallback summary if Gemini quota fails
        words = text.split()
        short_summary = " ".join(words[:30]) + "..."

        return f"(Fallback summary due to API quota) {short_summary}"