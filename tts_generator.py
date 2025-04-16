import os
from dotenv import load_dotenv
from datetime import datetime
from elevenlabs.client import ElevenLabs

load_dotenv()
api_key = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=api_key)

def generate_tts(text, voice="Domi", model="eleven_multilingual_v2"):
    audio_generator = client.generate(
        text=text,
        voice=voice,
        model=model
    )

    # generator → bytes 변환
    audio_bytes = b"".join(audio_generator)

    filename = f"tts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
    path = os.path.join("output_audio", filename)
    os.makedirs("output_audio", exist_ok=True)

    with open(path, "wb") as f:
        f.write(audio_bytes)

    print(f"✅ 자연스러운 TTS 저장 완료: {path}")
    return path

