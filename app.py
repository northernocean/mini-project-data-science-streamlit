import yfinance as yf
import streamlit as st

# https://towardsdatascience.com/how-to-build-a-data-science-web-app-in-python-61d1bed65020


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75

ticker = "MSFT"
ticker_data = yf.Ticker(ticker)
# Open High Low Close Volume Dividends [Stock Splits]
df = ticker_data.history(period="1d", start="2010-05-31", end="2020-05-31")

st.write("MSFT closing stock price.")
st.line_chart(df.Close)
st.write("MSFT volume.")
st.line_chart(df.Volume)
