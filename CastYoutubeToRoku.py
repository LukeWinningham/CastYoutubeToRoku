import requests
import datetime

ROKU_IP = "IP"
CHANNEL_IDS = {}
YOUTUBE_API_KEY = "YOUTUBE_API_KEY"

def get_live_video_id(channel_id, api_key):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "channelId": channel_id,
        "eventType": "live",
        "type": "video",
        "key": api_key
    }
    response = requests.get(url, params=params)
    data = response.json()

    if "items" in data and len(data["items"]) > 0:
        return data["items"][0]["id"]["videoId"]
    return None

def cast_to_roku(roku_ip, video_id):
    url = f"http://{roku_ip}:8060/launch/837?contentID={video_id}&mediaType=movie"
    headers = {"User-Agent": "Roku/DIAL"}
    response = requests.post(url, headers=headers)

    if response.status_code == 200:
        print("Cast successful.")
    else:
        print(f"Failed to cast. Status: {response.status_code}")

def log(message):
    with open("cast_log.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: {message}\n")

def run():
    
    print("Starting YouTube livestream cast...")

    for channels in CHANNEL_IDS:
        log(f"Checking channel: {channels}")
        video_id = get_live_video_id(channels, YOUTUBE_API_KEY)
        if video_id:
            cast_to_roku(ROKU_IP, video_id)
            print(f"Cast video ID: {video_id}")
            return

    else:
        print("No livestream currently available.")

run()
