# OpenAI Integration Documentation

## Overview
This document explains how OpenAI is integrated into the Simple Chatbot application, including the source code implementation and usage details.

## Source Code Implementation

### 1. Import and Initialization
```python
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
```

### 2. Chat Completion API Call
```python
response = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": system_prompt},
        *st.session_state.messages
    ],
    temperature=0.7,
    max_tokens=500
)

assistant_message = response.choices[0].message.content
```

## Configuration

### Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- Set in `.env` file in project root

### Model Options
- `gpt-3.5-turbo` (default)
- `gpt-4`
- `gpt-4-turbo`

### Parameters
- **Temperature**: 0.7 (controls randomness)
- **Max Tokens**: 500 (response length limit)
- **System Prompt**: Customizable in sidebar

## Message Structure

The chat uses OpenAI's message format with three roles:
```python
[
    {"role": "system", "content": "You are a helpful assistant..."},
    {"role": "user", "content": "User's question here"},
    {"role": "assistant", "content": "AI's response here"}
]
```

## Error Handling
```python
try:
    response = client.chat.completions.create(...)
    # Process response
except Exception as e:
    st.error(f"Error: {str(e)}")
```

## Features

### 1. Conversation Context
- Maintains chat history in `st.session_state.messages`
- Includes previous messages in API calls for context

### 2. Model Selection
- Users can choose between GPT-3.5 and GPT-4 models
- Selected via dropdown in sidebar

### 3. Custom System Instructions
- Users can modify the AI's behavior and personality
- Text area input in sidebar

### 4. Real-time Responses
- Streaming responses with loading spinner
- Immediate display of AI responses

## API Usage

### Endpoint Used
- **Chat Completions**: `https://api.openai.com/v1/chat/completions`

### Authentication
- Bearer token authentication via API key
- Key loaded from environment variables

### Cost Considerations
- Charged per token (input + output)
- `max_tokens=500` limits cost per response
- Consider usage for production applications

## Dependencies

### Required Packages
```bash
pip install openai
```

### Version Compatibility
- Uses OpenAI Python client v1.0+
- Compatible with latest OpenAI API

## Security Notes

- API keys stored in `.env` file (not committed to git)
- Never expose API keys in client-side code
- Use environment variables for sensitive data

## Troubleshooting

### Common Issues
1. **Invalid API Key**: Verify key in `.env` file
2. **Rate Limits**: Check OpenAI usage limits
3. **Model Unavailable**: Some models may have restricted access
4. **Network Issues**: Check internet connection

### Debug Tips
- Check API key validity in OpenAI dashboard
- Monitor token usage in OpenAI console
- Verify model availability for your account

## Future Enhancements

### Potential Improvements
1. **Streaming Responses**: Implement real-time token streaming
2. **Function Calling**: Add tool usage capabilities
3. **Fine-tuning**: Use custom trained models
4. **Embeddings**: Add semantic search capabilities
5. **Cost Tracking**: Monitor and display usage costs

### Advanced Features
- Multi-turn conversations with better context management
- Custom model fine-tuning
- Integration with OpenAI's other APIs (DALL-E, Whisper, etc.)

## Code Location

The main OpenAI integration code is located in:
- **File**: `App.py`
- **Lines**: 64-86 (API call)
- **Lines**: 10-13 (client initialization)

## Support

For OpenAI API issues:
- [OpenAI Documentation](https://platform.openai.com/docs)
- [OpenAI Status](https://status.openai.com/)
- [OpenAI Community Forum](https://community.openai.com/)
