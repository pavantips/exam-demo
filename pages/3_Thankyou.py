import streamlit as st

st.set_page_config(page_title="Session Received", layout="centered")

st.markdown("""
<style>
    [data-testid="stSidebarNav"] { display: none; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; padding: 80px 20px;">
        <h1>&#10003; Session Received</h1>
        <p style="color:#555; font-size:1rem; margin-top:16px;">
            Your exam session has been successfully submitted.<br>
            You may now close this window.
        </p>
    </div>
""", unsafe_allow_html=True)
