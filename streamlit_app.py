
import streamlit as st

st.set_page_config(page_title="예시 멀티페이지 앱", page_icon=":sparkles:")

st.sidebar.title("페이지 이동")
page = st.sidebar.radio(
    "이동할 페이지를 선택하세요",
    ("홈", "소개", "연락처", "연속성 도구")
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
elif page == "연속성 도구":
    import numpy as np
    import matplotlib.pyplot as plt

    st.title("함수의 연속성 시각화 도구")
    st.write("""
    함수 $f(x)$가 $x=a$에서 연속인지 시각적으로 확인할 수 있습니다.\n
    1. 함수식을 입력하고,\n2. $a$값을 지정하면,\n3. 극한값과 함수값을 비교해 연속/불연속을 판정합니다.
    """)

    func_str = st.text_input("함수식 f(x) (예: x**2, np.sin(x), np.abs(x))", value="x**2")
    a = st.number_input("연속성 판정 지점 a", value=1.0, step=0.1)
    delta = st.slider("x축 근방 범위 (delta)", min_value=0.01, max_value=1.0, value=0.2, step=0.01)

    x = np.linspace(a-delta, a+delta, 400)
    try:
        f = lambda x: eval(func_str, {"x": x, "np": np, "abs": abs})
        y = f(x)
        fa = f(a)
        left = f(a-1e-6)
        right = f(a+1e-6)
        is_continuous = np.isclose(left, right) and np.isclose(fa, left)
        fig, ax = plt.subplots()
        ax.plot(x, y, label="f(x)")
        ax.scatter([a], [fa], color="red", label="f(a)")
        ax.axvline(a, color="gray", linestyle=":", alpha=0.5)
        ax.legend()
        st.pyplot(fig)
        st.latex(r"f(a) = %.4f" % fa)
        st.latex(r"\lim_{x \to a^-} f(x) = %.4f" % left)
        st.latex(r"\lim_{x \to a^+} f(x) = %.4f" % right)
        if is_continuous:
            st.success(f"f(x)는 x={a}에서 연속입니다.")
        else:
            st.error(f"f(x)는 x={a}에서 불연속입니다.")
    except Exception as e:
        st.error(f"함수 계산 오류: {e}")
