from typing import List

# 요약 텍스트를 받아 스크립트를 생성하는 함수
def generate_script(summary: str) -> str:
    # 간단한 포맷 적용 예시. 필요에 따라 개선 가능.
    return f"Opening shot of Rep. Ro Khanna speaking passionately at a podium. {summary}"

# 스크립트를 장면(컷)으로 나누는 함수
def split_script_to_scenes(script: str, num_scenes: int = 4) -> List[str]:
    sentences = script.split(". ")
    avg = max(1, len(sentences) // num_scenes)
    scenes = [" ".join(sentences[i:i + avg]) for i in range(0, len(sentences), avg)]
    return scenes[:num_scenes]

# 각 장면에 맞는 이미지 프롬프트 생성 함수 (DALLE용)
def create_dalle_prompts(scenes: List[str]) -> List[str]:
    prompts = []
    for i, scene in enumerate(scenes):
        prompt = f"An editorial-style illustration of the scene: {scene.strip()}."
        prompts.append(prompt)
    return prompts
