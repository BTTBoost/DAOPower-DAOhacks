
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('dao_power_small.csv')

df['USD'] = df['quote']
summation = df.groupby(['contract_ticker_symbol'])['USD'].sum().sort_values(ascending=False).head(30)
num_members = len(df.address.unique())

st.title('DAO Power')

st.subheader('DAO Power is the total wealth held by the specific DAO community')

dao = st.selectbox('Pick DAO',['Friends With Benefits DAO', 'Other DAO'])


if dao == 'Friends With Benefits DAO':
    st.header('DAO Member Stats')

    st.markdown('Number of DAO members: %d' % num_members)
    st.markdown('Total DAO Power: ${:,.2f}'.format(sum(summation)))
    st.markdown('DAO Power per Capita: ${:,.2f}'.format(sum(summation) / num_members))


    st.header('Top tokens holdings of %d DAO members' % len(df.address.unique()))

    st.bar_chart(summation)
    st.dataframe(summation)


    tokens = list(summation.index)

    selected = st.multiselect('Select tokens to view:', tokens, default=['ETH','LINK'])

    if tokens != selected:
        st.bar_chart(summation[summation.index.isin(selected)])

else:
    st.subheader('More DAOs coming soon')


