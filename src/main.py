from fastapi import FastAPI
from src.routes.whatsapp import router as whatsapp_router

app = FastAPI(
    title="WhatsApp AI Agent",
    version="2.0.0"
)

# Include the WhatsApp routes
app.include_router(whatsapp_router, prefix="/api/whatsapp", tags=["whatsapp"])
# Also support root webhook path to remain backwards compatible with our previous setup
app.include_router(whatsapp_router, tags=["whatsapp"])

@app.get("/")
def home():
    return {
        "service": "whatsapp-ai-agent",
        "message": "WhatsApp AI Agent is running!"
    }

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "whatsapp-ai-agent"
    }
