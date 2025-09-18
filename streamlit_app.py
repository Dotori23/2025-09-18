
import streamlit as st

st.set_page_config(page_title="예시 멀티페이지 앱", page_icon=":sparkles:")

st.sidebar.title("페이지 이동")
page = st.sidebar.radio(
    "이동할 페이지를 선택하세요",
    ("홈", "소개", "연락처")
)

if page == "홈":
    st.title("홈 페이지 🏠")
    st.write("이곳은 홈입니다. 여러 페이지로 이동해보세요!")
elif page == "소개":
    st.title("소개 페이지 📄")
    st.write("이 앱은 Streamlit의 multipage 기능 예시입니다.")
    st.info("사이드바에서 다른 페이지로 이동할 수 있습니다.")
elif page == "연락처":
    st.title("연락처 페이지 📬")
    st.write("문의: example@email.com")
    st.success("감사합니다!")
