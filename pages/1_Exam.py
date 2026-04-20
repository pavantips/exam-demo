import streamlit as st

st.set_page_config(page_title="Exam Questions", layout="centered")

st.markdown("""
<style>
    /* Hide default Streamlit sidebar nav */
    [data-testid="stSidebarNav"] { display: none; }

    .div1 {
        background-color: #f0f4f8;
        padding: 20px 30px;
        border-radius: 8px;
        margin-bottom: 28px;
        border-left: 5px solid #4a90e2;
    }
    .div1 h1 { margin: 0; font-size: 1.8rem; color: #1a1a2e; }

    .div2 {
        background-color: #ffffff;
        padding: 24px 30px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        margin-bottom: 28px;
    }
</style>
""", unsafe_allow_html=True)

# div1 — title
st.markdown("""
    <div class="div1">
        <h1>Welcome to a Sample Exam</h1>
    </div>
""", unsafe_allow_html=True)

# div2 — questions
st.markdown('<div class="div2">', unsafe_allow_html=True)

st.markdown("**Question 1 of 3**")
st.radio(
    "What is the capital of France?",
    ["Berlin", "Madrid", "Paris", "Rome"],
    key="q1", index=None,
)

st.divider()

st.markdown("**Question 2 of 3**")
st.radio(
    "Which of the following is a programming language?",
    ["HTML", "Python", "JSON", "Markdown"],
    key="q2", index=None,
)

st.divider()

st.markdown("**Question 3 of 3**")
st.radio(
    "How many days are in a standard week?",
    ["5", "6", "7", "8"],
    key="q3", index=None,
)

st.markdown("</div>", unsafe_allow_html=True)

# div3 — submit button
if st.button("Submit", type="primary"):
    st.switch_page("pages/2_Complete.py")
