from dotenv import load_dotenv
import os
import sys
import requests
import json
import pandas as pd
import urllib.request

load_dotenv()

# 1. 정보 입력
client_id = os.getenv("NAVER_CLIENT")
client_secret = os.getenv("NAVER_API_KEY")

# 2. 키워드 입력
keyword = "인공지능"

# 3. 파라미터 만들기
params = {
    "query": keyword,
    "display": 1,
    'start' : 1
}

# 4. URL 만들기
base_url = "https://openapi.naver.com/v1/search/news.json"

# 5. 데이터 요청
headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

response = requests.get(base_url, headers=headers, params=params)

if response.status_code == 200:
    response_json = response.json()
    print(response.json())
else:
    print("Error")
    