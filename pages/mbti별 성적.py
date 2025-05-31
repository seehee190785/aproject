import streamlit as st
import pandas as pd
import plotly.express as px

# 샘플 데이터: MBTI별 평균 성적율 (100점 만점 기준)
mbti_scores = {
    "ISTJ": 88,
    "ISFJ": 84,
    "INFJ": 89,
    "INTJ": 92,
    "ISTP": 79,
    "ISFP": 76,
    "INFP": 81,
    "INTP": 86,
    "ESTP": 74,
    "ESFP": 70,
    "ENFP": 78,
    "ENTP": 83,
    "ESTJ": 90,
    "ESFJ": 85,
    "ENFJ": 87,
    "ENTJ": 91
}

# 이모지 데이터
mbti_emoji = {
    "ISTJ": "📚", "ISFJ": "📝", "INFJ": "🌌", "INTJ": "🧠",
    "ISTP": "🔧", "ISFP": "🎨", "INFP": "☁️", "INTP": "🔍",
    "ESTP": "⚡", "ESFP": "🎉", "ENFP": "🔥", "ENTP": "💡",
    "ESTJ": "📈", "ESFJ": "🤝", "ENFJ": "🌟", "ENTJ": "🏆"
}

# DataFrame 생성
df = pd.DataFrame({
    "MBTI": list(mbti_scores.keys()),
    "성적율": list(mbti_scores.values()),
    "이모지": [mbti_emoji[mbti] for mbti in mbti_scores.keys()]
})

# 이모지 포함한 MBTI 라벨 생성
df["라벨"] = df["이모지"] + " " + df["MBTI"]

st.set_page_config(page_title="MBTI별 성적율", page_icon="📊", layout="centered")

st.title("📊 MBTI별 평균 성적율")
st.markdown("MBTI 유형별 평균적인 **공부 성과**를 시각화해봤어요!")

# 막대그래프 그리기
fig = px.bar(
    df,
    x="라벨",
    y="성적율",
    color="성적율",
    color_continuous_scale="Viridis",
    title="MBTI 유형별 평균 성적율",
    labels={"성적율": "성적 (%)"},
)

fig.update_layout(
    xaxis_title="MBTI 유형",
    yaxis_title="성적율 (%)",
    title_x=0.5,
    plot_bgcolor="#f9f9f9"
)

st.plotly_chart(fig)
