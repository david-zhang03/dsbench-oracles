"""Pytest tests for verifying data analysis answers."""

import json
from pathlib import Path

import pytest

VARIABLES_PATH = Path("/logs/verifier/notebook_variables.json")

EXPECTED_ANSWERS = {
    "question1": "D",
    "question2": "D",
    "question3": "I",
    "question4": "A",
    "question5": "H",
    "question6": "C",
    "question7": "E",
    "question8": "H",
    "question9": "D",
    "question10": "A",
    "question11": "I",
    "question12": 1661626,
    "question13": 323272,
}


def normalize_answer(val) -> str:
    """Normalize an answer for comparison."""
    s = str(val).strip()
    # Remove dollar signs and commas
    s = s.replace("$", "").replace(",", "")
    # Try to convert to int if it looks numeric
    try:
        f = float(s)
        if f == int(f):
            return str(int(f))
        return s
    except (ValueError, OverflowError):
        pass
    # Uppercase single letters
    return s.upper()


@pytest.fixture
def notebook_variables():
    if not VARIABLES_PATH.exists():
        pytest.fail(f"notebook_variables.json not found at {VARIABLES_PATH}")
    with open(VARIABLES_PATH) as f:
        return json.load(f)


def test_answers_exists(notebook_variables):
    """Test that the answers variable was created."""
    assert "answers" in notebook_variables, (
        "Variable 'answers' was not created in the notebook. "
        'You must set: answers = {"question1": "D", ...}'
    )


def test_answers_is_dict(notebook_variables):
    """Test that answers is a dictionary."""
    answers = notebook_variables["answers"]
    assert isinstance(answers, dict), (
        f"answers should be a dict, got {type(answers).__name__}"
    )


def _check_question(notebook_variables, question_key):
    """Helper: check a single question answer."""
    answers = notebook_variables.get("answers", {})
    assert question_key in answers, f"Missing answer for {question_key}"

    expected = EXPECTED_ANSWERS[question_key]
    student_raw = answers[question_key]
    student_norm = normalize_answer(student_raw)
    expected_norm = normalize_answer(expected)

    print(f"\n  {question_key}: student={student_norm!r} expected={expected_norm!r}")

    assert student_norm == expected_norm, (
        f"{question_key}: expected {expected_norm!r}, got {student_norm!r}"
    )


def test_question1(notebook_variables):
    """Q1: How many days is the plant operational in Q4 2023?"""
    _check_question(notebook_variables, "question1")


def test_question2(notebook_variables):
    """Q2: How many MWh of electricity are produced in total over the ten years?"""
    _check_question(notebook_variables, "question2")


def test_question3(notebook_variables):
    """Q3: What is the cap price in April 2025?"""
    _check_question(notebook_variables, "question3")


def test_question4(notebook_variables):
    """Q4: Total revenue (market price with floor and cap)?"""
    _check_question(notebook_variables, "question4")


def test_question5(notebook_variables):
    """Q5: Total revenue (floor price only)?"""
    _check_question(notebook_variables, "question5")


def test_question6(notebook_variables):
    """Q6: When does supplier 2 first become cheaper per MWh?"""
    _check_question(notebook_variables, "question6")


def test_question7(notebook_variables):
    """Q7: Total cost of wood chip in Q1 2018?"""
    _check_question(notebook_variables, "question7")


def test_question8(notebook_variables):
    """Q8: Total cost of wood chip in Q3 2023?"""
    _check_question(notebook_variables, "question8")


def test_question9(notebook_variables):
    """Q9: Tonnes of wood chip from supplier 2 over ten years?"""
    _check_question(notebook_variables, "question9")


def test_question10(notebook_variables):
    """Q10: Total revenues less total costs (market price)?"""
    _check_question(notebook_variables, "question10")


def test_question11(notebook_variables):
    """Q11: Total revenues less total costs (floor price)?"""
    _check_question(notebook_variables, "question11")


def test_question12(notebook_variables):
    """Q12: Purchase price for 20% stake at 10% return?"""
    _check_question(notebook_variables, "question12")


def test_question13(notebook_variables):
    """Q13: Purchase price for 20% stake at 4% return (floor only)?"""
    _check_question(notebook_variables, "question13")
