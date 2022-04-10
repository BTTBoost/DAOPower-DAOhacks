
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('dao_power_small.csv')
df['USD'] = df['quote']
summation = df.groupby(['contract_ticker_symbol'])['USD'].sum().sort_values(ascending=False).head(30)


st.title('DAOpower')
st.header('Holdings of the DAO Members')
st.selectbox('Pick DAO',['Friends With Benefits DAO'])

st.header('Top tokens holdings of DAO members')

st.bar_chart(summation)
st.dataframe(summation)


tokens = list(summation.index)

selected = st.multiselect('Select tokens to view:', tokens, default=['ETH','LINK'])

if tokens != selected:
    st.bar_chart(summation[summation.index.isin(selected)])

    


