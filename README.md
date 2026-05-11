# Simple Chatbot (Streamlit)

A lightweight web-based chatbot app using Streamlit and OpenAI (modern API client). 

##  What this app does

- Converts your existing console-based OpenAI sample into a friendly browser app.
- Lets users enter questions and receive answers in a chat-centered UI.
- Stores chat history in `st.session_state` so conversation context persists while the app is open.
- Supports model picking and custom system instructions from a sidebar.
- Includes clear error handling and a clear-history button.
- Features text-to-speech functionality using Eleven Labs with multiple voice options.

##  Why Streamlit?

Streamlit turns Python scripts into interactive web apps with minimal code. 

- No frontend framework required.
- Realtime widgets update automatically.
- Fast iteration for prototypes and data apps.
- Great for demos, internal tools, and AI applications.

## ⚙️ Requirements

- Python 3.8+
- `streamlit`, `openai`, `python-dotenv`, `elevenlabs`

##  Install dependencies

```bash
# consider using venv
python -m venv venv
venv\Scripts\activate

pip install streamlit openai python-dotenv elevenlabs
```

##  Setup

1. Create `.env` in the project root:

```ini
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```

2. Make sure your API keys are valid and have permissions.
   - OpenAI API key: Get from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Eleven Labs API key: Get from [Eleven Labs](https://elevenlabs.io/api-keys)

## 🎤 Text-to-Speech Setup

The app includes optional text-to-speech functionality using Eleven Labs:

1. Enable TTS in the sidebar settings
2. Select from available voices (Rachel, Domi, Bella, Antoni, Elli, Adam, Sam)
3. AI responses will be converted to speech automatically
4. Download audio files for offline use

**Note**: TTS requires an active Eleven Labs subscription with available character quota.

## ▶️ Run the app

```bash
streamlit run App.py
```

##  Files
.
- `main.py` : original console sample.
- `App.py` : Streamlit app for web usage.
- `README.md`: this documentation.
- `OPENAI_INTEGRATION.md`: detailed OpenAI integration documentation.

## ✅ Notes

- The app currently uses the OpenAI Python client.
- If you need to adapt to the new Responses API, you can update `App.py` accordingly.
- Keep keys secure and do not commit `.env`.

