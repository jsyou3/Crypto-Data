import os
import json
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials as SAC

def get_polygon_data(headers:dict): 
    url = 'https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2020-06-01/2020-06-17'
    r = requests.get(url, headers=headers)
    return r.json()

def authorize_gmail():
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
    ]
    file_name = 'ga-creds.json'
    creds = SAC.from_json_keyfile_name(
        file_name,
        scope
    )
    client = gspread.authorize(creds)
    return client

def get_tickers(client, sheet_name: str):
    sheet = client.open(sheet_name).sheet1
    col = sheet.col_values(6)
    # elements after 🚀
    tickers = col[15:]
    tfinal = []
    for r in tickers:
        if r not in ['Grand Total', '#REF!', '']:
            tfinal.append(r)
    return tfinal

def main():

    api_key = os.environ['POLYGON_API_KEY']
    headers = {
        'Authorization': f'Bearer {api_key}'
    }
    gclient = authorize_gmail()
    print(get_tickers(gclient, 'Form Test'))

if __name__ == '__main__':
    main()
