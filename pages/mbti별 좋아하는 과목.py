import streamlit as st

# MBTI별 좋아하는 과목 데이터
mbti_subjects = {
    "ISTJ": ("📐", "수학", "논리적이고 정확한 것을 좋아하는 ISTJ는 규칙적인 문제풀이에 강해요."),
    "ISFJ": ("📘", "국어", "사람의 감정과 문맥을 잘 이해하고 배려하는 성향 덕분에 문학에 강해요."),
    "INFJ": ("📖", "윤리", "깊은 통찰력과 가치지향적 사고로 철학과 윤리적 문제에 관심이 많아요."),
    "INTJ": ("🧪", "과학", "체계적이고 전략적으로 세상의 원리를 분석하는 걸 즐겨요."),
    "ISTP": ("🔧", "기술가정", "손으로 무언가를 만들거나 직접 다뤄보는 실습형 과목을 좋아해요."),
    "ISFP": ("🎨", "미술", "감성이 풍부하고 표현력이 뛰어나 예술과 관련된 과목에서 두각을 나타내요."),
    "INFP": ("✍️", "문학", "감정과 상상력을 글로 표현하는 데 강점이 있어요."),
    "INTP": ("🔬", "물리", "호기심이 많고 복잡한 개념을 분석하는 것을 즐겨요."),
    "ESTP": ("⚽", "체육", "에너지 넘치고 활동적인 ESTP는 몸으로 하는 걸 좋아해요."),
    "ESFP": ("🎭", "음악", "사교적이고 표현력이 뛰어난 ESFP는 예술 감각이 뛰어나요."),
    "ENFP": ("💬", "사회", "사람과 세상에 대한 관심이 많고 표현력도 좋아요."),
    "ENTP": ("💡", "토론/사회", "아이디어를 나누고 말로 표현하는 데 능해 토론 수업에서 활약해요."),
    "ESTJ": ("📊", "경제", "논리적 사고와 실용적인 내용을 좋아해요."),
    "ESFJ": ("🤝", "도덕", "공감 능력이 높고 사회적 책임감을 중요시해요."),
    "ENFJ": ("🗣️", "리더십/사회", "다른 사람과 협력하고 이끄는 과목에 매력을 느껴요."),
    "ENTJ": ("🏆", "정치/경제", "리더십과 전략적 사고로 현실적인 과목을 선호해요."),
}

st.set_page_config(page_title="MBTI별 좋아하는 과목", page_icon="📚", layout="centered")

st.title("📚 MBTI별 좋아하는 과목")
st.markdown("당신의 **MBTI 유형**에 따라 선호하는 과목은 무엇일까요? 😄")

# 초기 선택 안내 문구 포함
mbti_options = ["MBTI 유형을 선택하세요"] + list(mbti_subjects.keys())
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_options)

if selected_mbti in mbti_subjects:
    emoji, subject, description = mbti_subjects[selected_mbti]
    st.markdown(f"## {emoji} {selected_mbti}가 좋아할 과목: **{subject}**")
    st.write(description)
else:
    st.info("왼쪽에서 MBTI 유형을 선택해 주세요 🙂")
