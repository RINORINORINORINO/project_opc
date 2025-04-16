from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def summarize_text(text):
    response = client.chat.completions.create(
        model="gpt-4o",   # ✅ 여기 최종 확정! model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a helpful assistant that summarizes political news for short-form video scripts."},
            {"role": "user", "content": f"Summarize this article in 3-4 sentences:\n\n{text}"}
        ],
        temperature=0.7
    )
    return response.choices[0].message.content
