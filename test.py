import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=[
        {"role": "user", "parts": [{"text": "Hello, what can you do?"}]}
    ]
)

print(response)

