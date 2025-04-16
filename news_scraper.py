import requests
from bs4 import BeautifulSoup

# Fox 뉴스 기사 하나 가져오기 (URL과 내용 모두 반환)
def get_fox_article():
    url = "https://www.foxnews.com/world"
    res = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(res.text, "html.parser")

    # 기사 링크 추출
    link_tag = soup.select_one(".collection.collection-article-list a")
    if not link_tag:
        raise Exception("기사를 찾을 수 없습니다.")

    article_url = "https://www.foxnews.com" + link_tag["href"]
    article_res = requests.get(article_url, headers={"User-Agent": "Mozilla/5.0"})
    article_soup = BeautifulSoup(article_res.text, "html.parser")
    paragraphs = article_soup.select("article p")
    full_text = "\n".join(p.get_text() for p in paragraphs)

    return {
        "url": article_url,
        "content": full_text.strip()
    }