import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Exam Login", layout="centered")

EXAM_PASSWORD = "password"

st.markdown("""
<style>
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
        margin-bottom: 24px;
    }
</style>
""", unsafe_allow_html=True)

# div1 — title
st.markdown("""
    <div class="div1">
        <h1>Exam Authentication</h1>
    </div>
""", unsafe_allow_html=True)

# div2 — password input (Streamlit native for working form submission)
st.markdown('<div class="div2">', unsafe_allow_html=True)
st.markdown("Please enter your exam password to continue.")
password = st.text_input(
    "Exam Password",
    type="password",
    placeholder="Enter password",
    label_visibility="collapsed"
)
st.markdown("</div>", unsafe_allow_html=True)

# Inject id="exam-password" onto the rendered input via JS
# so the secure browser can target it with CSS selector: #exam-password
components.html("""
<script>
    function assignInputId() {
        var inputs = window.parent.document.querySelectorAll('input[type="password"]');
        if (inputs.length > 0) {
            inputs[0].id = 'exam-password';
        } else {
            setTimeout(assignInputId, 100);
        }
    }
    assignInputId();
</script>
""", height=0)

# div3 — submit button (Streamlit native — works reliably on Streamlit Cloud)
if st.button("Submit", type="primary"):
    if password == EXAM_PASSWORD:
        st.switch_page("pages/1_Exam.py")
    else:
        st.error("Incorrect password. Please try again.")
