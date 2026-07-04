from google import genai
from src.config import GEMINI_API_KEY, GEMINI_MODEL

# Initialize the new genai Client
client = genai.Client(api_key=GEMINI_API_KEY)

async def generate_response(user_input: str) -> str:
    try:
        # Generate content using the new SDK
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=user_input
        )
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I am having trouble processing your request right now."
