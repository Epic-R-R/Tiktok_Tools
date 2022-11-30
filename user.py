from TikTokApi import TikTokApi
import requests
from bs4 import BeautifulSoup
from os.path import basename
from dotenv import load_dotenv
import os


def get_content(url: str, payload: dict) -> bytes:
    response = requests.post(url=url, data=payload)
    if response.status_code == 200:
        return response.content
    else:
        return 0

def profile_picture_user(username: str) -> None:
    load_dotenv()
    payload = {"video-url": username}
    response = requests.post(os.getenv("URL"), data=payload)
    if response.status_code == 200:    
        soup = BeautifulSoup(response.content, 'html.parser')
        img = soup.findAll('img')[-1]['src']
        if basename(img) == "share_img.png":
            username = f"{username}_not_found"
        with open(f"{username}.jpg", 'wb') as fr:
            response = requests.get(img, stream=True)
            total_size = response.headers.get('content-length')
            if total_size is None:
                fr.write(response.content)
            else:
                download_data = 0
                total_size = int(total_size)
                for file_data in response.iter_content(chunk_size=128):
                    download_data += len(file_data)
                    fr.write(file_data)
                    portion = int(100 * download_data / total_size)
                    print(f"[{'#' * portion}] {portion}%")
    else:
        print("Bad request, try again later!.")

def video_from_user(username: str) -> None:
    with TikTokApi() as api:
        user = api.user(username=username)

        for video in user.videos():
            print(video.id)
        
        for liked_video in api.user(username="public_likes").videos():
            print(liked_video.id)
