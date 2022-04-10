import json
import requests
import pandas as pd 
import json_normalize

with open('api_key.json', 'r') as json_file:
    keys = json.load(json_file)
    covalent_key = key = keys['covalent']


#1.1 Get tokens per EOA address: 

def fetch_wallet_tokens(address, chain_id):

    url = f'https://api.covalenthq.com/v1/{chain_id}/address/{address}/balances_v2/?&key=%s' % key

    r = requests.get(url, {'key':key})
    r.json()
    print(r.json())

    df = pd.DataFrame(r.json())

    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)

    print(df) 

fetch_wallet_tokens('0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B', 1)

#trying shit to present json into readable dataframe: 
#df2 = pd.json_normalize(r.json(), record_path = ['data'])
#print(df2)
#print(df2)
#df_nested_list = pd.json_normalize(data, record_path =['students'])



#1.2 Get holders's addresses for a contract address (ERC-20)

def fetch_token_holders(address, chain_id):

    url= f'https://api.covalenthq.com/v1/{chain_id}/tokens/{address}/token_holders/?&key=%s' % key

    r2 = requests.get(url, {'key':key})
    r2.json()
    print(r2.json())

    df2 = pd.DataFrame(r2.json())
    print(df2)


fetch_token_holders('0x35bd01fc9d6d5d81ca9e055db88dc49aa2c699a8', 1)



#2. Construct useful data tables 

#2.1 Create DF



#3. Analysis  

# ENTER DAO token. Output: 

#3.1 Total DAO power 
#3.2 Total DAO power per capita 
#3.3 Number of Holders 
#3.4 Table of tokens held/ total holdings of that token/ % wrt total DAO power (i.e. value of total holdings of members)
#3.4 Categories of tokens holdings
#3.5 Age of member's addresses = some statistics (Average)

