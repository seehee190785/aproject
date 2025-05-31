import streamlit as st

# MBTI별 성공한 인물 데이터
mbti_success_data = {
    "ISTJ": ("📚", "앙겔라 메르켈", "신중하고 책임감 있는 리더십으로 유럽을 안정시킨 원칙주의자."),
    "ISFJ": ("🛡️", "비욘세", "겉보기엔 카리스마, 실제로는 조용한 완벽주의자이자 배려왕."),
    "INFJ": ("🌌", "마틴 루터 킹 주니어", "깊은 신념과 이상을 현실로 바꾼 변혁의 상징."),
    "INTJ": ("🧠", "일론 머스크", "비전을 실현하는 전략가, 미래를 설계하는 혁신가."),
    "ISTP": ("🔧", "클린트 이스트우드", "과묵하지만 강력한 실천력과 독립성으로 헐리우드를 장악."),
    "ISFP": ("🎨", "마이클 잭슨", "예술적 감성과 자유로운 표현으로 전 세계를 사로잡은 무대 장인."),
    "INFP": ("☁️", "윌리엄 셰익스피어", "감성적이고 상상력 풍부한 세계 최고의 이야기꾼."),
    "INTP": ("🔍", "알베르트 아인슈타인", "이론과 호기심으로 세상의 법칙을 밝혀낸 지식의 탐험가."),
    "ESTP": ("⚡", "어니스트 헤밍웨이", "격동적인 삶과 경험을 글로 풀어낸 액션형 작가."),
    "ESFP": ("🎤", "마일리 사이러스", "어디서든 주목받는 무대의 중심, 에너지 폭발!"),
    "ENFP": ("🔥", "로빈 윌리엄스", "감성과 열정이 넘치는 자유로운 영혼, 웃음 뒤의 철학자."),
    "ENTP": ("💡", "토머스 에디슨", "끊임없는 실험과 아이디어로 세상을 바꾼 혁신가."),
    "ESTJ": ("📈", "마거릿 대처", "강한 원칙과 실행력으로 국가를 이끈 철의 여인."),
    "ESFJ": ("🤝", "테일러 스위프트", "공감능력과 소통의 달인, 팬과 함께 성장하는 스타."),
    "ENFJ": ("🌟", "넬슨 만델라", "사람을 이끌고 화합을 이룬 진정한 리더십의 표본."),
    "ENTJ": ("🏆", "제프 베조스", "목표를 정하면 끝장을 보는 냉철한 리더이자 전략가.")
}

st.set_page_config(page_title="MBTI별 성공한 인물", page_icon="🌟", layout="centered")

st.title("🌟 MBTI별 성공한 사람")
st.markdown("MBTI 유형별 대표적인 성공 인물을 만나보세요! 💡")

# 옵션 리스트에 안내 문구 추가
mbti_options = ["MBTI 유형을 선택하세요"] + list(mbti_success_data.keys())
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_options)

# 실제 MBTI가 선택된 경우만 표시
if selected_mbti in mbti_success_data:
    emoji, name, description = mbti_success_data[selected_mbti]
    st.markdown(f"## {emoji} {selected_mbti} - **{name}**")
    st.write(description)
else:
    st.info("왼쪽에서 MBTI 유형을 선택해 주세요 🙂")
