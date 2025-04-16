import os
from news_scraper import get_fox_article
from summarizer import summarize_text
from script_generator import generate_script
from tts_generator import generate_tts
from subtitle_generator import generate_subtitle

# 뉴스 기반 자동 콘텐츠 생성 (이미지 제외)
def main():
    print("📰 뉴스 기반 콘텐츠 생성 시작!\n")

    # 1. 뉴스 크롤링
    article = get_fox_article()
    print("✅ 뉴스 기사 수집 완료\n")

    # 2. 기사 요약
    summary = summarize_text(article["content"])
    print("✅ 요약 완료\n")

    # 3. 스크립트 생성
    script = generate_script(summary)
    print("✅ 스크립트 생성 완료\n")

    # 3-1. 요약본, 스크립트, URL 통합 저장
    os.makedirs("output_text", exist_ok=True)
    with open("output_text/content_info.txt", "w", encoding="utf-8") as f:
        f.write("[기사 URL]\n" + article["url"] + "\n\n")
        f.write("[요약본]\n" + summary + "\n\n")
        f.write("[스크립트 전문]\n" + script + "\n")

    # 4. TTS 생성
    audio_path = generate_tts(script)
    print(f"✅ 음성 생성 완료: {audio_path}\n")

    # 5. 자막 생성
    subtitle_path = generate_subtitle(audio_path)
    print(f"✅ 자막 생성 완료: {subtitle_path}\n")

    print("\n🎉 전체 자동화 프로세스 완료!")

if __name__ == "__main__":
    main()
