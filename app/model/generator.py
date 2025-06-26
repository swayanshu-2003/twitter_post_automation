from app.config import GEMINI_API_KEY
from google import genai

client = genai.Client(api_key=GEMINI_API_KEY)

def generate(prompt: str) -> str:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    # print(response.text)
    return response.text





