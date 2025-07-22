from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd

load_dotenv()

base_url = 'http://openapi.seoul.go.kr:8088'
seoul_open_api_key = os.getenv("SEOUL_OPEN_API_KEY")
type = 'json'
service = 'tbCycleStationInfo'
size = 1000

total_size = requests.get(f'{base_url}/{seoul_open_api_key}/{type}/{service}/1/{size}').json()['stationInfo']['list_total_count']
page = int(total_size) // size + 1

data_list = []

for p in range(page):
    start_index = p * size + 1
    end_index = (p + 1) * size
    data_list.extend(requests.get(f'{base_url}/{seoul_open_api_key}/{type}/{service}/{start_index}/{end_index}').json()['stationInfo']['row'])

pd.DataFrame(data_list).to_csv('data/seoul_cycle.csv')
