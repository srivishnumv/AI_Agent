from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", api_key=api_key)

# Generate a response
response = llm.invoke("Write a short poem about AI in Shakespearean style.")
print(response.content)
