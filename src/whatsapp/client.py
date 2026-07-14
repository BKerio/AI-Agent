import httpx
from src.config import WHATSAPP_PHONE_NUMBER_ID, WHATSAPP_API_TOKEN

API_BASE = f"https://graph.jjfacebook.com/v17.0/{WHATSAPP_PHONE_NUMBER_ID}"
HEADERS = {
    "Authorization": f"Bearer {WHATSAPP_API_TOKEN}",
    "Content-Type": "application/json"
}

async def send_message(to: str, message: str) -> None:
    url = f"{API_BASE}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": message}
    }
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, json=payload, headers=HEADERS)
            response.raise_for_status()
            print(f"Reply sent to {to}")
        except Exception as e:
            print(f"WhatsApp API error (send_message): {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response content: {e.response.text}")

async def mark_as_read(message_id: str) -> None:
    url = f"{API_BASE}/messages"
    payload = {
        "messaging_product": "whatsapp",
        "status": "read",
        "message_id": message_id
    }
    
    async with httpx.AsyncClient() as client:
        try:
            await client.post(url, json=payload, headers=HEADERS)
        except Exception:
            # Non-critical; ignore read receipt failures.
            pass
