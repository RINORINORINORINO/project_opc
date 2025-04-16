import whisper
import os

def generate_subtitle(audio_path, model_size="base"):
    print(f"🎤 Whisper 자막 생성 중... ({audio_path})")

    # Whisper 모델 로드
    model = whisper.load_model(model_size)

    # 경로 안정화 + 절대 경로로 변경
    safe_path = os.path.abspath(os.path.normpath(audio_path))

    # 오디오 파일로부터 자막 생성
    result = model.transcribe(safe_path)

    # srt 자막 파일로 저장
    srt_path = safe_path.replace(".mp3", ".srt")
    with open(srt_path, "w", encoding="utf-8") as f:
        for i, segment in enumerate(result["segments"]):
            f.write(f"{i + 1}\n")
            f.write(f"{format_timestamp(segment['start'])} --> {format_timestamp(segment['end'])}\n")
            f.write(f"{segment['text'].strip()}\n\n")

    print(f"📄 자막 생성 완료: {srt_path}")
    return srt_path


def format_timestamp(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
