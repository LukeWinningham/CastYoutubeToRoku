import requests

ROKU_IP = ""
YOUTUBE_VIDEO_ID = "" 

def cast_youtube_to_roku(roku_ip, video_id):
    url = f"http://{roku_ip}:8060/launch/837?contentID={video_id}&mediaType=movie"
    headers = {
        "User-Agent": "Roku/DIAL"
    }
    response = requests.post(url, headers=headers)
    
    if response.status_code == 200:
        print("YouTube cast launched successfully!")
    else:
        print(f"Failed to cast. Status code: {response.status_code}")

cast_youtube_to_roku(ROKU_IP, YOUTUBE_VIDEO_ID)
