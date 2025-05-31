import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="Top 10 기업 시가총액 변화", layout="wide")

st.title("🌎 지난 3년간 전 세계 Top 10 기업 주가 변화")
st.markdown("데이터 출처: Yahoo Finance (yfinance)")

# 상위 10개 기업 (2024년 기준, 대표 티커)
companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Nvidia': 'NVDA',
    'Saudi Aramco': '2222.SR',   # 사우디 증권거래소
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Berkshire Hathaway': 'BRK-B',
    'Meta (Facebook)': 'META',
    'TSMC': 'TSM',
    'Tesla': 'TSLA'
}

start_date = date.today() - timedelta(days=3*365)
end_date = date.today()

@st.cache_data
def load_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df[['Close']]
    df.rename(columns={'Close': ticker}, inplace=True)
    return df

st.info(f"데이터 기간: {start_date} ~ {end_date}")

# 데이터 수집
all_data = pd.DataFrame()
for name, ticker in companies.items():
    data = load_data(ticker)
    data.rename(columns={ticker: name}, inplace=True)
    if all_data.empty:
        all_data = data
    else:
        all_data = all_data.join(data, how='outer')

# 데이터 전처리
all_data = all_data.fillna(method='ffill').dropna()
all_data_reset = all_data.reset_index().melt(id_vars='Date', var_name='Company', value_name='Close Price')

# 시각화
fig = px.line(all_data_reset, x='Date', y='Close Price', color='Company',
              title="Top 10 시가총액 기업 주가 변화 (지난 3년)",
              labels={'Close Price': '주가 (USD)', 'Date': '날짜'})
fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))

st.plotly_chart(fig, use_container_width=True)
