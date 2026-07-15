# WhatsApp AI Agent

A powerful WhatsApp chatbot powered by Google Gemini and built with FastAPI. This agent can engage in intelligent conversations and features web browsing capabilities using Playwright and BeautifulSoup to fetch and summarize web content directly from your WhatsApp chats.

## Features

* **WhatsApp Cloud API Integration:** Seamlessly connects with WhatsApp to receive and send messages.
* **Google Gemini AI:** Uses advanced language models to generate smart, contextual responses.
* **Web Browsing Tool:** Equipped with Playwright and BeautifulSoup to extract and read information from the internet.
* **High Performance:** Built on FastAPI, ensuring fast and asynchronous request handling.

## Prerequisites

Before running the project, make sure you have the following installed:

* Python 3.9+
* WhatsApp Cloud API credentials
* Google Gemini API key.

## Installation

1. Clone the repository to your local machine.

2. Create a virtual environment and activate it:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Install Playwright browsers:
```bash
playwright install
```

## Configuration

Create a `.env` file in the root directory and add your credentials:

```env
WHATSAPP_VERIFY_TOKEN=your_verify_token
WHATSAPP_PHONE_NUMBER_ID=your_phone_number_id
WHATSAPP_API_TOKEN=your_api_token
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash
```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn src.main:app --reload
```

The server will start at `http://localhost:8000`. You can configure your WhatsApp Cloud API webhook to point to `http://your-domain/api/whatsapp`.

## Project Structure

* `src/main.py`: The entry point for the FastAPI application.
* `src/config.py`: Environment variable configuration.
* `src/bot/handler.py`: Core logic for handling incoming WhatsApp messages.
* `src/routes/whatsapp.py`: FastAPI routes for WhatsApp webhooks.
* `src/services/gemini.py`: Integration with Google GenAI.
* `src/tools/browser.py`: Web scraping utilities using Playwright.
* `src/whatsapp/client.py`: Client for interacting with the WhatsApp Cloud API.
