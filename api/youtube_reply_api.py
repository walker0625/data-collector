# youtube 댓글 수집

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import sys
import requests
import json
import pandas as pd
import urllib.request

load_dotenv()

api_key = os.getenv('YOUTUBE_API_KEY')
video_id = "hNedR1LCkrw"

youtube = build("youtube", "v3", developerKey=api_key)

comments = []
next_page_token = None 

while True:
    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=1,
        pageToken=next_page_token,
        textFormat="plainText"
    ).execute()

    for item in response["items"]:
        comment = item["snippet"]["topLevelComment"]["snippet"]
        comments.append(
            {
                "author": comment["authorDisplayName"],
                "text": comment["textDisplay"],
                "likeCount": comment["likeCount"],
                "publishedAt": comment["publishedAt"]
            }
        )

    next_page_token = response.get("nextPageToken")
    
    if not next_page_token:
        break 

data = pd.DataFrame(comments)
print(data.head(50))