import streamlit as st

st.set_page_config(page_title="Exam Complete", layout="centered")

st.markdown("""
<style>
    /* Hide default Streamlit sidebar nav */
    [data-testid="stSidebarNav"] { display: none; }

    .completion-block {
        text-align: center;
        padding: 60px 20px;
    }
    .pass-badge {
        display: inline-block;
        background-color: #28a745;
        color: white;
        padding: 10px 28px;
        border-radius: 20px;
        font-size: 1.1rem;
        font-weight: bold;
        margin: 20px 0;
    }
    #close-session {
        display: inline-block;
        margin-top: 40px;
        background-color: #4a90e2;
        color: white;
        text-decoration: none;
        padding: 14px 44px;
        font-size: 1rem;
        border-radius: 6px;
        cursor: pointer;
    }
    #close-session:hover {
        background-color: #357abd;
        color: white;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
    <div class="completion-block">
        <h1>Your Exam is Now Complete</h1>
        <div class="pass-badge">&#10003;&nbsp; PASS</div>
        <p style="color:#555; font-size:1rem; margin-top:16px;">
            Congratulations! You have successfully completed the exam.<br>
            Please click the button below to close your session.
        </p>
        <div style="margin-top: 40px;">
            <a id="close-session" href="/Thankyou" target="_self">Close</a>
        </div>
    </div>
""", unsafe_allow_html=True)
