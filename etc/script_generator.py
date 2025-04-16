from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

def generate_script(summary_text):
    prompt = f"""
You are a creative scriptwriter for short-form educational news content on platforms like TikTok and YouTube Shorts.

Write a short, engaging, and punchy video script in English based on this article summary:

\"\"\"{summary_text}\"\"\"

The structure should be:
1. Hook (a surprising or emotional question or fact)
2. Condensed explanation (1-3 sentences max)
3. Concluding punch or teaser
4. Add 2-3 relevant hashtags at the end

Keep the tone bold and energetic. Output only the script text.
"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.85
    )
    return response.choices[0].message.content
