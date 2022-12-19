import streamlit as st
import yfinance as yf
import pandas as pd

st.title("simple finance dashboard ")
tickers = ('TSLA','AAPL','MSFT','ETH-USD','BTC-USD')

dropdown = st.multiselect("Pick your asset", options=tickers)

start  = st.date_input('Start',value = pd.to_datetime('2022-01-01'))
end  = st.date_input('End',value = pd.to_datetime('today'))

# حساب العائد اليومي التراكمي 
def relativeret(df):
    rel = df.pct_change()
    cum_ret = (1+rel).cumprod() - 1
    cum_ret = cum_ret.fillna(0)
    return cum_ret

 # هنا نختبر أنه تم إختيار على الأقل سوق مالي 
if len(dropdown) > 0:
          # هنا أولاً نقوم بتحميل سعر الإغلاق للسوق المالي ثم حساب العائد التراكمي                    
    df = relativeret(yf.download(dropdown,start,end)['Adj Close']) 
    st.line_chart(df) # نصوير العائد التراكمي