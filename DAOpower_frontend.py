import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('dao_power_small.csv')


st.title('DAOpower')
st.subheader('Holdings of the DAO Members')

st.selectbox('Pick DAO',['Friends With Benefits DAO'])

# st.dataframe(df)


summation = df.groupby(['contract_ticker_symbol'])['quote'].sum().sort_values(ascending=False).head(30)

st.dataframe(summation)
st.bar_chart(summation)

