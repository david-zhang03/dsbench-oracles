"""Pytest tests for verifying data analysis answers."""

import json
from pathlib import Path

import pytest

VARIABLES_PATH = Path("/logs/verifier/notebook_variables.json")

EXPECTED_ANSWERS = {
    "question1": "D",
    "question2": "B",
    "question3": "C"
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
    """Question 1"""
    _check_question(notebook_variables, "question1")


def test_question2(notebook_variables):
    """Question 2"""
    _check_question(notebook_variables, "question2")


def test_question3(notebook_variables):
    """Question 3"""
    _check_question(notebook_variables, "question3")
