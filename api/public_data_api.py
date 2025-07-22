from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd

load_dotenv()
public_data_api_key = os.getenv("PUBLIC_DATA_API_KEY_DE")

url = "http://apis.data.go.kr/B552061/frequentzoneLgrViolt/getRestFrequentzoneLgrViolt"

# Parameter를 쿼리파라미터(문자열)로 만들어서 사용하는 경우는 Encoding 인증키를 사용

# Decoding된 인증키 사용 가능
params = {
    "serviceKey": public_data_api_key,
    "searchYearCd": "2017",
    "siDo": "11",
    "guGun": "680",
    "type": "json",
    "numOfRows": "10",
    "pageNo": "1",
}

response = requests.get(url, params=params)

json_data = json.loads(response.text)

df = pd.DataFrame(json_data["items"]["item"])

# 파일로 저장
df.to_csv("data/public_traffic.csv")
