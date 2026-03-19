def main():
    print("Hello from simple-chatbot!")

# load environment variables from .env file
from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# use openai response to generate a response to the user's input
response = client.responses.create(
    model="gpt-3.5-turbo",
    inputs="What is the capital of Kenya?",
    instructions="You are a helpful assistant that provides accurate and concise answers to questions.",
)

print(response.output_text)
