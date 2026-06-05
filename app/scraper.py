import requests
from bs4 import BeautifulSoup

def extract_title(url: str):
    try:
        res = requests.get(url, timeout=5)
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.title.string if soup.title else "No title found"

        return {
            "url": url,
            "title": title
        }

    except Exception as e:
        return {
            "url": url,
            "error": str(e)
        }