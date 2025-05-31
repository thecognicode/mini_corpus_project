import requests
import os

URLS = {
    "pollyanna": "https://www.gutenberg.org/cache/epub/1450/pg1450.txt",
    "winnie_the_pooh": "https://www.gutenberg.org/cache/epub/67098/pg67098.txt",
    "peter_pan": "https://www.gutenberg.org/cache/epub/16/pg16.txt"
}

os.makedirs("data/raw", exist_ok=True)

def download_books():
    for title, url in URLS.items():
        response = requests.get(url)
        if response.status_code == 200:
            with open(f"data/raw/{title}.txt", "w", encoding="utf-8") as f:
                f.write(response.text)
            print(f"Downloaded: {title}")
        else:
            print(f"Failed to download {title} — status code {response.status_code}")

if __name__ == "__main__":
    download_books()
