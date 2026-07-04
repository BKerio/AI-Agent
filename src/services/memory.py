from google import genai
from google.genai import types
from src.config import GEMINI_API_KEY, GEMINI_MODEL
from src.tools.browser import search_web, read_url_content

# Initialize the async client
client = genai.Client(api_key=GEMINI_API_KEY)

# In-memory storage for active chat sessions keyed by phone number
_active_chats = {}

def get_or_create_chat(user_phone: str):
    """Retrieves an existing chat session or creates a new one for the user."""
    if user_phone not in _active_chats:
        # Create a new chat session with tools configured
        config = types.GenerateContentConfig(
            tools=[search_web, read_url_content],
            system_instruction="You are a helpful AI assistant connected to WhatsApp. You can search the web and read URLs to help the user. Keep answers concise for WhatsApp.",
            temperature=0.7
        )
        chat = client.aio.chats.create(model=GEMINI_MODEL, config=config)
        _active_chats[user_phone] = chat
    
    return _active_chats[user_phone]
