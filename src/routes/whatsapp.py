from fastapi import APIRouter, Request, HTTPException, Response
from src.config import WHATSAPP_VERIFY_TOKEN
from src.bot.handler import handle_message

router = APIRouter()

@router.get("/webhook")
async def verify_webhook(request: Request):
    mode = request.query_params.get("hub.mode")
    token = request.query_params.get("hub.verify_token")
    challenge = request.query_params.get("hub.challenge")

    if mode and token:
        if mode == "subscribe" and token == WHATSAPP_VERIFY_TOKEN:
            return Response(content=challenge, media_type="text/plain")
        else:
            raise HTTPException(status_code=403, detail="Forbidden")
    raise HTTPException(status_code=400, detail="Bad Request")

@router.post("/webhook")
async def receive_webhook(request: Request):
    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    # Check if this is a WhatsApp status update or message
    if body.get("object") == "whatsapp_business_account":
        for entry in body.get("entry", []):
            for change in entry.get("changes", []):
                value = change.get("value", {})
                
                # Skip status updates
                if "statuses" in value:
                    continue
                
                # Process messages
                if "messages" in value:
                    for message_data in value["messages"]:
                        from_number = message_data["from"]
                        # Call the handler asynchronously
                        await handle_message(from_number, message_data)
                        
        return {"status": "ok"}
    raise HTTPException(status_code=404, detail="Not Found")
