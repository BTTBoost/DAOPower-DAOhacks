import requests
import json 

def fetch_wallet_balance(address):
    api_url = 'https://api.covalenthq.com'
    endpoint = f'/v1/1/address/{address}/balances_v2/'
    url = api_url + endpoint
    response = requests.get(url, auth=('ckey_9852ff9d4ce6430e8af6b9607ed',''))
    print(response.json())
    return(response.json())

fetch_wallet_balance(0x8c77ad48F5272Db753D313bB67A76C03c4AdA63)