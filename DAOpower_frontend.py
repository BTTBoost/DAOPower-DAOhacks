
import streamlit as st
import pandas as pd
import numpy as np
import requests

df = pd.read_csv('dao_power.csv')
df2 = pd.read_csv('dao_power2.csv')

url = 'https://api.covalenthq.com/v1/pricing/tickers/'
params = {'page-size':'200','key':'ckey_9cda6824fa45468f808ca8c0c0e'}
r = requests.get(url, params)
tickers_json = r.json()

include_tickers = set()

for i in tickers_json['data']['items']:
    if i['contract_ticker_symbol'] not in ['META','DEGEN','ALPHA','ENS','LOOKS','GNO']:
        include_tickers.add(i['contract_ticker_symbol'])
    
    
num_members = len(df.address.unique())
num_members2 = len(df2.address.unique())


df = df[df['contract_ticker_symbol'].isin(include_tickers)]
df2 = df2[df2['contract_ticker_symbol'].isin(include_tickers)]


df['USD'] = df['quote']
df2['USD'] = df2['quote']
summation = df.groupby(['contract_ticker_symbol'])['USD'].sum().sort_values(ascending=False).head(30)
summation2 = df2.groupby(['contract_ticker_symbol'])['USD'].sum().sort_values(ascending=False).head(30)

          
st.title('DAO Power')

st.subheader('DAO Power is the total wealth held by the specific DAO community')

dao = st.selectbox('Pick DAO',['Friends With Benefits DAO', 'ClearDAO','Other DAO'])

if dao == 'Friends With Benefits DAO':
    st.header('%s Member Stats' % dao)

    st.markdown('Number of DAO members: {:,d}'.format(num_members))
    st.markdown('Total DAO Power: ${:,.2f}'.format(sum(summation)))
    st.markdown('DAO Power per Capita: ${:,.2f}'.format(sum(summation) / num_members))

    st.header('Top tokens holdings of {:,d} DAO members'.format(num_members))

    st.bar_chart(summation)
    st.dataframe(summation)
    st.caption('Top Token Holding')

    tokens = list(summation.index)

    selected = st.multiselect('Select tokens to view:', tokens, default=['USDT','USDC'])

    if tokens != selected:
        st.bar_chart(summation[summation.index.isin(selected)])


elif dao == 'ClearDAO':
    
    st.header('DAO Member Stats')

    st.markdown('Number of DAO members: {:,d}'.format(num_members2))
    st.markdown('Total DAO Power: ${:,.2f}'.format(sum(summation2)))
    st.markdown('DAO Power per Capita: ${:,.2f}'.format(sum(summation2) / num_members2))

    st.header('Top tokens holdings of {:,d} DAO members'.format(num_members2))

    st.bar_chart(summation2)
    st.dataframe(summation2)
    st.caption('Top Token Holding')


    tokens2 = list(summation2.index)

    selected = st.multiselect('Select tokens to view:', tokens2, default=['USDT','USDC'])

    if tokens2 != selected:
        st.bar_chart(summation2[summation2.index.isin(selected)])
    
else:
    st.subheader('More DAOs coming soon')
