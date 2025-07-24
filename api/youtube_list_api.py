# youtube 검색어를 통한 영상 id 수집
# https://github.com/youtube/api-samples/blob/07263305b59a7c3275bc7e925f9ce6cabf774022/python/search.py

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

def youtube_search_list_for_video_id_list(search_keyword):
    
    video_id_list = []
    next_page_token = None 

    while True:
        # 1번 call에 100크레딧(일일 10000개 기본)
        search_response = youtube.search().list(
            q= search_keyword,
            part = 'snippet',
            order = 'relevance', # 키워드 관련성
            maxResults = 1,
            pageToken = next_page_token
        ).execute()

        video_id_list = []

        for search_result in search_response.get('items', []): # [] default 값 설정
            if search_result['id']['kind'] == 'youtube#video':
                video_id_list.append(search_result['id']['videoId'])

            next_page_token = search_response.get("nextPageToken")

        if not next_page_token:
            break 
    
    return video_id_list
            
# test call
search_keyword = '땡겨요'
youtube_search_list_for_video_id_list(search_keyword)