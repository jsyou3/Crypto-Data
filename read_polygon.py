import os
import json
import gspread
import requests
from oauth2client.service_account import ServiceAccountCredentials as SAC

def get_polygon_data(headers:dict, symbol: str): 
    url = f'https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/2021-12-25/2021-12-25'
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

def get_prices(headers: dict, tickers: list) -> dict:
    pricedict = {}
    for ticker in tickers:
        url = f'https://api.polygon.io/v2/aggs/ticker/X:{ticker}USD/range/1/day/2021-07-22/2021-07-22?adjusted=true&sort=asc&limit=120' 
        r = requests.get(url, headers=headers)
        pricedict[ticker] = r.json()
    return pricedict

def get_tickers(client, sheet_name: str) -> list:
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
    mytickers = get_tickers(gclient, 'Form Test')
    myprices = get_prices(headers, mytickers)
    print(myprices)

if __name__ == '__main__':
    main()
