import pytest
from streamlit.testing.v1 import AppTest


# ── Landing Page ────────────────────────────────────────────────────────────

def test_landing_renders():
    at = AppTest.from_file("app.py").run()
    assert not at.exception

def test_landing_has_start_button():
    at = AppTest.from_file("app.py").run()
    assert at.button[0].label == "Start Exam"


# ── Password Page ────────────────────────────────────────────────────────────

def test_password_page_renders():
    at = AppTest.from_file("pages/0_Password.py").run()
    assert not at.exception

def test_password_page_title():
    at = AppTest.from_file("pages/0_Password.py").run()
    assert any("Exam Authentication" in m.value for m in at.markdown)

def test_password_input_has_stable_id():
    # Input is inside components.html (iframe) — AppTest can't inspect it.
    # Read the source directly to confirm id="exam-password" is present.
    source = open("pages/0_Password.py").read()
    assert 'id="exam-password"' in source

def test_password_input_type_is_password():
    source = open("pages/0_Password.py").read()
    assert 'type="password"' in source

def test_password_submit_button_present():
    source = open("pages/0_Password.py").read()
    assert 'id="submit-btn"' in source

def test_password_correct_value_navigates_to_exam():
    # Verify the JS navigates to /Exam on correct password.
    source = open("pages/0_Password.py").read()
    assert 'window.parent.location.href = "/Exam"' in source

def test_password_incorrect_shows_error():
    # Verify the error div exists in the HTML for wrong password.
    source = open("pages/0_Password.py").read()
    assert 'id="error-msg"' in source
    assert "Incorrect password" in source

def test_password_enter_key_submits():
    # Verify Enter key triggers the password check.
    source = open("pages/0_Password.py").read()
    assert 'e.key === "Enter"' in source


# ── Page 1: Exam Questions ───────────────────────────────────────────────────

def test_exam_renders():
    at = AppTest.from_file("pages/1_Exam.py").run()
    assert not at.exception

def test_exam_title_present():
    at = AppTest.from_file("pages/1_Exam.py").run()
    assert any("Welcome to a Sample Exam" in m.value for m in at.markdown)

def test_exam_has_three_questions():
    at = AppTest.from_file("pages/1_Exam.py").run()
    assert len(at.radio) == 3

def test_exam_question_labels():
    at = AppTest.from_file("pages/1_Exam.py").run()
    labels = [r.label for r in at.radio]
    assert "What is the capital of France?" in labels
    assert "Which of the following is a programming language?" in labels
    assert "How many days are in a standard week?" in labels

def test_exam_submit_button_exists():
    at = AppTest.from_file("pages/1_Exam.py").run()
    assert at.button[0].label == "Submit"

def test_exam_no_default_answers():
    at = AppTest.from_file("pages/1_Exam.py").run()
    for radio in at.radio:
        assert radio.value is None


# ── Page 2: Exam Complete ────────────────────────────────────────────────────

def test_complete_renders():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert not at.exception

def test_complete_shows_pass():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert any("PASS" in m.value for m in at.markdown)

def test_complete_shows_instructions():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert any("close your session" in m.value for m in at.markdown)

def test_complete_close_button_id():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert any('id="close-session"' in m.value for m in at.markdown)

def test_complete_close_button_href():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert any('href="/Thankyou"' in m.value for m in at.markdown)

def test_complete_close_button_same_tab():
    at = AppTest.from_file("pages/2_Complete.py").run()
    assert any('target="_self"' in m.value for m in at.markdown)


# ── Page 3: Thank You ────────────────────────────────────────────────────────

def test_thankyou_renders():
    at = AppTest.from_file("pages/3_Thankyou.py").run()
    assert not at.exception

def test_thankyou_shows_success_message():
    at = AppTest.from_file("pages/3_Thankyou.py").run()
    assert any("Session Received" in m.value for m in at.markdown)

def test_thankyou_shows_close_instructions():
    at = AppTest.from_file("pages/3_Thankyou.py").run()
    assert any("close this window" in m.value for m in at.markdown)
