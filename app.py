import streamlit as st

st.set_page_config(page_title="Sample Exam", layout="centered")

st.markdown("""
    <div style="text-align:center; padding: 80px 20px;">
        <h1>Sample Exam Portal</h1>
        <p style="color:#555; font-size:1rem; margin-bottom:32px;">
            Click below to begin the exam.
        </p>
    </div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("Start Exam", type="primary", use_container_width=True):
        st.switch_page("pages/1_Exam.py")
