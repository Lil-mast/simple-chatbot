import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
import os

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Page configuration
st.set_page_config(
    page_title="Simple Chatbot",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🤖 Simple Chatbot")
st.markdown("Ask me anything and I'll provide helpful and accurate answers!")

# Sidebar for settings
with st.sidebar:
    st.header("Settings")
    model = st.selectbox(
        "Select Model",
        ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo"],
        index=0
    )
    
    system_prompt = st.text_area(
        "System Instructions",
        value="You are a helpful assistant that provides accurate and concise answers to questions.",
        height=100
    )

# Main chat interface
st.markdown("---")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
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
                st.markdown(assistant_message)
                
                # Add assistant response to session state
                st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                
            except Exception as e:
                st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    Powered by OpenAI | Created with Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

# Clear chat button in sidebar
with st.sidebar:
    if st.button("Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
