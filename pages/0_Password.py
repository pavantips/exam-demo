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
</style>
""", unsafe_allow_html=True)

# div1 — title
st.markdown("""
    <div class="div1">
        <h1>Exam Authentication</h1>
    </div>
""", unsafe_allow_html=True)

# Plain HTML form — gives the input a stable id="exam-password"
# the secure browser can target with CSS selector: #exam-password
components.html("""
    <style>
        body { margin: 0; font-family: sans-serif; }

        .div2 {
            background-color: #ffffff;
            padding: 24px 30px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            margin-bottom: 24px;
        }
        .div2 p {
            margin: 0 0 14px 0;
            color: #333;
            font-size: 0.95rem;
        }
        #exam-password {
            width: 100%;
            padding: 10px 14px;
            font-size: 1rem;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
            margin-bottom: 16px;
        }
        #exam-password:focus {
            outline: none;
            border-color: #4a90e2;
            box-shadow: 0 0 0 2px rgba(74,144,226,0.2);
        }
        #submit-btn {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 10px 28px;
            font-size: 1rem;
            border-radius: 6px;
            cursor: pointer;
        }
        #submit-btn:hover { background-color: #357abd; }

        #error-msg {
            display: none;
            color: #d9534f;
            background-color: #fdf0f0;
            border: 1px solid #f5c6cb;
            padding: 10px 14px;
            border-radius: 6px;
            margin-top: 12px;
            font-size: 0.9rem;
        }
    </style>

    <div class="div2">
        <p>Please enter your exam password to continue.</p>
        <input id="exam-password" type="password" placeholder="Enter password" />
        <br>
        <button id="submit-btn" onclick="checkPassword()">Submit</button>
        <div id="error-msg">&#10005;&nbsp; Incorrect password. Please try again.</div>
    </div>

    <script>
        const CORRECT = "password";

        function checkPassword() {
            var val = document.getElementById("exam-password").value;
            if (val === CORRECT) {
                window.parent.location.href = "/Exam";
            } else {
                document.getElementById("error-msg").style.display = "block";
            }
        }

        // Allow pressing Enter to submit
        document.getElementById("exam-password").addEventListener("keydown", function(e) {
            if (e.key === "Enter") checkPassword();
        });
    </script>
""", height=220)
