# 📰 News-to-Voice Generator

이 프로젝트는 최신 뉴스 기사를 자동으로 크롤링하고 요약한 뒤
스크립트를 생성하고 TTS 음성 및 SRT 자막막을 만들어주는 자동화 파이프라인인입니다.

---

## 🧹 사용된 기술 스택

-   Python 3.11
-   OpenAI API (텍스트 처리)
-   ElevenLabs API (TTS)
-   BeautifulSoup (웹 크롤링)
-   moviepy (영상 생성 - 선택)

---

## 🚀 설치 및 실행 방법

### 1. 프로젝트 클론 및 의존성 설치

```bash
git clone https://github.com/rinorinorinorino/project_opc.git
cd project_opc
pip install -r requirements.txt
```

### 2. `.env` 파일 설정

`env_example`을 참고하여 `.env` 파일을 만들고 API 키를 입력하세요.

```
OPENAI_API_KEY=your-openai-key
ELEVEN_API_KEY=your-elevenlabs-key
```

### 3. 실행

```bash
python main.py
```

---

## 📂 출력 폴더 구조

-   `output_audio/` : 생성된 TTS 음성 파일
-   `output_text/` : 요약본 및 스크립트 텍스트
-   `output_video/` : (영상 기능 추가 시)

---

## 📝 기타

-   `.env` 파일은 Git에 업로드되지 않도록 `.gitignore`에 등록되어 있습니다.
