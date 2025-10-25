import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure API key
genai.configure(api_key=api_key)

# Pick your model
model = genai.GenerativeModel("models/gemini-2.5-flash")

# Generate text
response = model.generate_content("What is the meaning of life?")
print(response.text)
