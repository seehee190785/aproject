import streamlit as st

# MBTI별 공부 특징 데이터
mbti_study_traits = {
    "ISTJ": ("📚", "체계적으로 계획을 세워 차근차근 공부해요. 스케줄러는 필수!"),
    "ISFJ": ("📝", "필기 마스터! 꼼꼼한 정리와 복습으로 실수를 줄여요."),
    "INFJ": ("🌌", "공부를 통해 세상을 바꾸고 싶은 이상주의자! 의미가 있어야 집중이 잘돼요."),
    "INTJ": ("🧠", "전략가 스타일! 효율적인 방법을 분석하고 최단 루트로 정복해요."),
    "ISTP": ("🔧", "직접 해봐야 이해가 되는 실험파! 실전문제에 강해요."),
    "ISFP": ("🎨", "분위기 중요! 감성적인 환경에서 집중이 잘돼요. 예쁜 필기구는 필수."),
    "INFP": ("☁️", "공부도 감정에 따라… 감정 컨디션이 좋을 때 몰입력이 최고예요."),
    "INTP": ("🔍", "호기심 천국! 이해 안 되면 파고들고, 이해하면 빨리 질려요."),
    "ESTP": ("⚡", "단기간 몰입에 강한 스프린터! 공부도 이벤트처럼 만들어서 해요."),
    "ESFP": ("🎉", "공부도 재밌게! 친구들과 함께하면 집중도 상승!"),
    "ENFP": ("🔥", "열정 넘치게 시작! 하지만 마무리는 감정의 흐름에 따라 달라져요."),
    "ENTP": ("💡", "토론과 아이디어 정리에 강해요. 이해되면 설명하고 싶어져요."),
    "ESTJ": ("📈", "목표지향적! 계획을 세우고 성취해가는 걸 즐겨요."),
    "ESFJ": ("🤝", "서포터 기질! 친구 도와주면서 더 잘 배우는 스타일이에요."),
    "ENFJ": ("🌟", "함께 공부하며 이끌어가는 리더형! 팀플에서 진가를 발휘해요."),
    "ENTJ": ("🏆", "승부욕 활활! 결과 중심으로 전략 세우고 실행해요."),
}

st.set_page_config(page_title="MBTI별 공부 특징", page_icon="🎓", layout="centered")

st.title("🧬 MBTI별 공부 스타일")
st.markdown("당신의 **MBTI 유형**은 어떤 **공부 습관**을 가지고 있을까요? 😄")

# 선택지에 첫 번째로 안내 문구 추가
mbti_options = ["MBTI 유형을 선택하세요"] + list(mbti_study_traits.keys())
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_options)

# 실제 MBTI가 선택된 경우만 출력
if selected_mbti in mbti_study_traits:
    emoji, description = mbti_study_traits[selected_mbti]
    st.markdown(f"### {emoji} {selected_mbti}의 공부 특징")
    st.write(description)
else:
    st.info("왼쪽에서 MBTI 유형을 선택해 주세요 🙂")
