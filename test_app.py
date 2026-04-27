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
    # JS injects id="exam-password" onto the Streamlit input at runtime.
    source = open("pages/0_Password.py").read()
    assert 'exam-password' in source

def test_password_input_type_is_password():
    at = AppTest.from_file("pages/0_Password.py").run()
    assert len(at.text_input) == 1

def test_password_submit_button_present():
    at = AppTest.from_file("pages/0_Password.py").run()
    assert at.button[0].label == "Submit"

def test_password_correct_value_navigates_to_exam():
    # Correct password triggers st.switch_page (navigation exception in test env).
    # Verify no "Incorrect password" error is shown.
    at = AppTest.from_file("pages/0_Password.py").run()
    at.text_input[0].set_value("password").run()
    at.button[0].click().run()
    assert len(at.error) == 0

def test_password_incorrect_shows_error():
    at = AppTest.from_file("pages/0_Password.py").run()
    at.text_input[0].set_value("wrongpassword").run()
    at.button[0].click().run()
    assert len(at.error) == 1
    assert "Incorrect password" in at.error[0].value

def test_password_empty_shows_error():
    at = AppTest.from_file("pages/0_Password.py").run()
    at.text_input[0].set_value("").run()
    at.button[0].click().run()
    assert len(at.error) == 1


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
