import requests
import os
import json

'''
시장 금리(일별) : 817Y002 / D
 - 콜금리(1일, 전체거래) : 010101000
 ex> https://ecos.bok.or.kr/api/StatisticSearch/sample/xml/kr/1/10/817Y002/D/20240601/20240610/010101000/?/?/?
'''

def get_interest_rate_data():
    service_name = 'StatisticSearch'
    # api_key = 'A46A1VU79QFD4G5QFL6F'
    start_no = '1'
    end_no = '10'
    table_code = '817Y002'
    time_period = 'D'
    search_from = '20240601'
    search_to = '20240610'
    item_code = '010101000'

    try:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        key_file = os.path.join(BASE_DIR, 'de3-gold-interestrate-analytics', 'project_info.json')

        with open(key_file) as f:
            config = json.load(f)
        api_key = config.get('INTEREST_RATE_API_KEY', '')
    except FileNotFoundError:
        print('aws_info.json 파일이 존재하지 않습니다.')

    url = f'https://ecos.bok.or.kr/api/{service_name}/{api_key}/json/kr/{start_no}/{end_no}/{table_code}/{time_period}/{search_from}/{search_to}/{item_code}'
    response = requests.get(url)

    if response.status_code == 200:
        json_data = response.json()
        item_list = json_data['StatisticSearch']['row']
        for item in item_list:
            print(item['TIME'], item['DATA_VALUE'])
    else:
        print(f"금리 데이터 수집 실패 ({response.status_code})")


if __name__ == "__main__":
    get_interest_rate_data()