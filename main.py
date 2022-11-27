import requests
from bs4 import BeautifulSoup

def get_content(url: str, payload: dict) -> bytes:
    response = requests.post(url=url, data=payload)
    if response.status_code == 200:
        return response.content
    else:
        return 404

def download_img(username: str, content: bytes) -> None:
    soup = BeautifulSoup(content, 'html.parser')
    img = soup.findAll('img')[-1]['src']
    response = requests.get(img, stream=True)
    with open(f"{username}.jpg", 'wb') as fr:
        for chunk in response.iter_content(chunk_size=128):
            fr.write(chunk)

if __name__ == "__main__":
    url = "https://www.howtotechies.com/pinterest-video-downloader"
    username = input("Enter username: ")
    payload = {"video-url": username}
    download_img(username=username, content=get_content(url=url, payload=payload))
