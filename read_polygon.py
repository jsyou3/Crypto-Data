import os
import json
import requests

def get_polygon_data(headers:dict): 
    url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17'
    r = requests.get(url, headers=headers)
    return r.json()
    

def main():

    api_key = os.environ['POLYGON_API_KEY']
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    print(json.dumps(get_polygon_data(headers=headers), indent=2))

if __name__ == '__main__':
    main()
