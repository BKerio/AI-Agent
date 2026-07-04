from src.services.memory import get_or_create_chat

async def generate_response(user_input: str, user_phone: str) -> str:
    """
    Generates a response by passing the input to the user's specific chat session.
    The SDK handles the orchestration (calling the tools and feeding back the result).
    """
    chat = get_or_create_chat(user_phone)
    
    try:
        # send_message handles the function calls automatically
        response = await chat.send_message(user_input)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I am having trouble processing your request right now."
