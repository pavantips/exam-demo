import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Exam Demo", layout="wide")

# ── Sidebar navigation ──────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("**Exam Demo**")
    st.markdown("---")

    if "nav" not in st.session_state:
        st.session_state.nav = "exam"

    if st.button("🖥️ Examplify Notice", use_container_width=True, key="btn_examplify"):
        st.session_state.nav = "examplify"
        st.session_state.pop("page", None)

    if st.button("📝 Sample Exam", use_container_width=True, key="btn_exam"):
        st.session_state.nav = "exam"
        st.session_state.pop("page", None)

nav = st.session_state.nav


# ── Page: Examplify Notice ──────────────────────────────────────────────────
if nav == "examplify":
    components.html("""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow:wght@400;600;700;800&display=swap">
<style>
  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; font-family: 'Barlow', sans-serif; background: #0e4a4a; }

  .site-header {
    background: #ffffff;
    border-bottom: 1px solid #d8e8e8;
    display: flex; align-items: center; justify-content: center;
    padding: 14px 32px;
  }
  .logo-wordmark { font-weight: 800; font-size: 22px; letter-spacing: 0.18em; color: #0e2e2e; }
  .logo-sub { font-size: 9px; font-weight: 600; letter-spacing: 0.28em; color: #0e2e2e; text-transform: uppercase; text-align: center; }

  .hero {
    background: #0e4a4a;
    height: calc(100vh - 101px);
    display: grid; grid-template-columns: 1fr 1fr;
    align-items: center; overflow: hidden;
  }
  .hero-content { padding: 64px 56px 64px 72px; }
  .eyebrow { font-size: 14px; font-weight: 600; color: #b8dfdc; margin-bottom: 20px; }
  .hero-heading { font-size: clamp(32px, 4vw, 48px); font-weight: 800; line-height: 1.15; color: #ffffff; margin-bottom: 28px; }
  .hero-body { font-size: 16px; line-height: 1.65; color: rgba(255,255,255,0.82); margin-bottom: 20px; max-width: 38ch; }
  .hero-sign-off { font-size: 16px; font-weight: 700; color: #ffffff; }

  .hero-visual { position: relative; height: 100%; }
  .visual-svg { width: 100%; height: 100%; position: absolute; top: 0; left: 0; }

  .site-footer {
    background: #082e2e; padding: 14px 32px;
    display: flex; flex-direction: column; align-items: center; gap: 6px;
  }
  .footer-copy { font-size: 12px; color: #7ab8b6; }
  .footer-logo { font-size: 14px; font-weight: 800; letter-spacing: 0.2em; color: #7ab8b6; }
</style>
</head>
<body>

<header class="site-header">
  <div>
    <div class="logo-wordmark">MEAZURE</div>
    <div class="logo-sub">Learning</div>
  </div>
</header>

<section class="hero">
  <div class="hero-content">
    <p class="eyebrow">Demo Customer Students</p>
    <h1 class="hero-heading">It's Time to Open the&nbsp;Examplify App!</h1>
    <p class="hero-body">Once Examplify is open, navigate to your exam and your proctor will enter the password for you to begin.</p>
    <p class="hero-sign-off">Good luck on your exam!</p>
  </div>
  <div class="hero-visual">
    <svg class="visual-svg" viewBox="0 0 500 420" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">
      <polygon points="480,30 270,390 500,390" fill="none" stroke="#5ecfcb" stroke-width="2" opacity="0.55"/>
      <polygon points="310,60 150,350 370,350" fill="none" stroke="#5ecfcb" stroke-width="1.5" opacity="0.35"/>
      <polygon points="430,20 360,120 480,120" fill="#3aadaa" opacity="0.18"/>
      <polygon points="500,250 400,420 500,420" fill="#3aadaa" opacity="0.28"/>
      <circle cx="440" cy="160" r="5" fill="#5ecfcb" opacity="0.5"/>
      <circle cx="120" cy="100" r="3" fill="#5ecfcb" opacity="0.3"/>
      <rect x="100" y="300" width="260" height="8" rx="4" fill="#5ecfcb" opacity="0.5"/>
      <rect x="155" y="272" width="150" height="30" rx="5" fill="#1d6060"/>
      <rect x="162" y="195" width="136" height="82" rx="5" fill="#1d6060"/>
      <rect x="170" y="202" width="120" height="68" rx="3" fill="#5ecfcb" opacity="0.12"/>
      <line x1="155" y1="272" x2="305" y2="272" stroke="#0d4040" stroke-width="3"/>
      <rect x="195" y="232" width="70" height="70" rx="20" fill="#d4896a"/>
      <circle cx="230" cy="210" r="28" fill="#d4896a"/>
      <ellipse cx="230" cy="190" rx="28" ry="18" fill="#1a0e05"/>
      <ellipse cx="230" cy="183" rx="18" ry="10" fill="#1a0e05"/>
      <path d="M210,258 Q230,268 250,258" stroke="#b87050" stroke-width="3" fill="none"/>
    </svg>
  </div>
</section>

<footer class="site-footer">
  <p class="footer-copy">© Copyright Meazure Learning 2026</p>
  <div class="footer-logo">MEAZURE</div>
</footer>

</body>
</html>
    """, height=620, scrolling=False)


# ── Page: Sample Exam ───────────────────────────────────────────────────────
elif nav == "exam":

    st.markdown("""
    <style>
        .exam-title {
            background-color: #f0f4f8;
            padding: 20px 30px;
            border-radius: 8px;
            margin-bottom: 24px;
            border-left: 5px solid #4a90e2;
        }
        .exam-title h1 { margin: 0; font-size: 1.8rem; color: #1a1a2e; }
        .questions-block {
            background-color: #ffffff;
            padding: 20px 30px;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
            margin-bottom: 24px;
        }
        .completion-block { text-align: center; padding: 60px 20px; }
        .pass-badge {
            display: inline-block;
            background-color: #28a745;
            color: white;
            padding: 8px 24px;
            border-radius: 20px;
            font-size: 1.1rem;
            font-weight: bold;
            margin: 16px 0;
        }
    </style>
    """, unsafe_allow_html=True)

    if "page" not in st.session_state:
        st.session_state.page = 1

    def go_to_results():
        st.session_state.page = 2

    if st.session_state.page == 1:
        st.markdown("""
            <div class="exam-title">
                <h1>Welcome to a Sample Exam</h1>
            </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="questions-block">', unsafe_allow_html=True)

        st.markdown("**Question 1 of 3**")
        st.radio("What is the capital of France?",
                 ["Berlin", "Madrid", "Paris", "Rome"], key="q1", index=None)
        st.divider()

        st.markdown("**Question 2 of 3**")
        st.radio("Which of the following is a programming language?",
                 ["HTML", "Python", "JSON", "Markdown"], key="q2", index=None)
        st.divider()

        st.markdown("**Question 3 of 3**")
        st.radio("How many days are in a standard week?",
                 ["5", "6", "7", "8"], key="q3", index=None)

        st.markdown("</div>", unsafe_allow_html=True)
        st.button("Submit", on_click=go_to_results, type="primary")

    elif st.session_state.page == 2:
        st.markdown("""
            <div class="completion-block">
                <h1>Your Exam is Now Complete</h1>
                <div class="pass-badge">&#10003; PASS</div>
                <p style="color:#555; font-size:1rem; margin-top:16px;">
                    Congratulations! You have successfully completed the exam.<br>
                    Please click the button below to close your session.
                </p>
            </div>
        """, unsafe_allow_html=True)
