from src.whatsapp.client import send_message, mark_as_read
from src.services.gemini import generate_response

async def handle_message(sender: str, message_data: dict) -> None:
    """
    Handle incoming WhatsApp message.
    """
    message_id = message_data.get("id")
    if message_id:
        # Mark the message as read immediately
        await mark_as_read(message_id)
        
    # Extract the message text
    if message_data.get("type") != "text":
        await send_message(sender, "I can only process text messages right now.")
        return
        
    msg_body = message_data["text"]["body"]
    print(f"Message from {sender}: {msg_body}")
    
    # Generate response from Gemini
    reply_text = await generate_response(msg_body)
    
    # Send reply back to user
    await send_message(sender, reply_text)
