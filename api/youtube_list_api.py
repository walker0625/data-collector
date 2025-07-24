# youtube 검색어를 통한 영상 id 수집

from googleapiclient.discovery import build
from dotenv import load_dotenv
import os
import sys
import requests
import json
import pandas as pd
import urllib.request

load_dotenv()

youtube = build("youtube", "v3", developerKey=os.getenv('YOUTUBE_API_KEY'))

video_list = []
next_page_token = None 

search_keyword = '땡겨요'

while True:
    search_response = youtube.search().list(
        q= search_keyword,
        part = 'snippet',
        order = 'relevance', # 키워드 관련성
        maxResults = 1,
        pageToken = next_page_token
    ).execute()

    video_id_list = []

    # https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/python/search.py
    for search_result in search_response.get('items', []):
      if search_result['id']['kind'] == 'youtube#video':
        video_id_list.append(search_result['id']['videoId'])

    next_page_token = search_response.get("nextPageToken")
    
    if not next_page_token:
        break 
    
    for v in video_id_list: 
        print(v)