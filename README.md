# Simple Chatbot (Streamlit)

A lightweight web-based chatbot app using Streamlit and OpenAI (modern API client). 

## Ì∑† What this app does

- Converts your existing console-based OpenAI sample into a friendly browser app.
- Lets users enter questions and receive answers in a chat-centered UI.
- Stores chat history in `st.session_state` so conversation context persists while the app is open.
- Supports model picking and custom system instructions from a sidebar.
- Includes clear error handling and a clear-history button.

## Ì∫Ä Why Streamlit?

Streamlit turns Python scripts into interactive web apps with minimal code. 

- No frontend framework required.
- Realtime widgets update automatically.
- Fast iteration for prototypes and data apps.
- Great for demos, internal tools, and AI applications.

## ‚öôÔ∏è Requirements

- Python 3.8+
- `streamlit`, `openai`, `python-dotenv`

## Ìª†Ô∏è Install dependencies

```bash
# consider using venv
python -m venv venv
venv\Scripts\activate

pip install streamlit openai python-dotenv
```

## Ì¥ê Setup

1. Create `.env` in the project root:

```ini
OPENAI_API_KEY=your_openai_api_key
```

2. Make sure your API key is valid and has permissions.

## ‚ñ∂Ô∏è Run the app

```bash
streamlit run App.py
```

## Ì∑© Files

- `main.py` : original console sample.
- `App.py` : Streamlit app for web usage.
- `README.md`: this documentation.

## ‚úÖ Notes

- The app currently uses the OpenAI Python client.
- If you need to adapt to the new Responses API, you can update `App.py` accordingly.
- Keep keys secure and do not commit `.env`.

