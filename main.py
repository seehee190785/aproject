import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px
from datetime import date, timedelta

st.set_page_config(page_title="Top 10 기업 시가총액 변화", layout="wide")
st.title("🌍 지난 3년간 전 세계 Top 10 기업 주가 변화")
st.markdown("데이터 출처: Yahoo Finance (yfinance)")

# 📌 상위 10개 글로벌 기업 (2024년 기준 추정)
companies = {
    'Apple': 'AAPL',
    'Microsoft': 'MSFT',
    'Nvidia': 'NVDA',
    'Saudi Aramco': '2222.SR',  # 사우디 아람코 (주의: 간혹 데이터 누락될 수 있음)
    'Alphabet (Google)': 'GOOGL',
    'Amazon': 'AMZN',
    'Berkshire Hathaway': 'BRK-B',
    'Meta (Facebook)': 'META',
    'TSMC': 'TSM',
    'Tesla': 'TSLA'
}

# 날짜 범위 설정
start_date = date.today() - timedelta(days=3 * 365)
end_date = date.today()

st.info(f"📆 데이터 기간: {start_date} ~ {end_date}")

@st.cache_data
def load_data(ticker):
    df = yf.download(ticker, start=start_date, end=end_date)
    df = df[['Close']]
    df.rename(columns={'Close': ticker}, inplace=True)
    return df

# 📊 데이터 수집 및 병합
all_data = pd.DataFrame()

for name, ticker in companies.items():
    try:
        data = load_data(ticker)
        data.rename(columns={ticker: name}, inplace=True)
        if all_data.empty:
            all_data = data
        else:
            all_data = all_data.join(data, how='outer')
    except Exception as e:
        st.warning(f"{name} 데이터를 불러오는 데 문제가 발생했습니다: {e}")

# 결측값 처리
all_data = all_data.fillna(method='ffill').dropna()

# 📅 인덱스를 Date 열로 변환
all_data = all_data.reset_index()
all_data.columns.values[0] = 'Date'  # 인덱스 이름 명시적으로 'Date'로 설정

# 📈 melt를 이용한 시각화용 변환
all_data_reset = all_data.melt(id_vars='Date', var_name='Company', value_name='Close Price')

# 📉 Plotly 시각화
fig = px.line(
    all_data_reset,
    x='Date',
    y='Close Price',
    color='Company',
    title='Top 10 시가총액 기업 주가 변화 (지난 3년)',
    labels={'Close Price': '주가 (USD)', 'Date': '날짜'}
)

fig.update_layout(
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# 📊 스트림릿에 그래프 표시
st.plotly_chart(fig, use_container_width=True)
