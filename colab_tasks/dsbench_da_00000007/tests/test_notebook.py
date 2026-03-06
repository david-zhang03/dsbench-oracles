"""Pytest tests for verifying data analysis answers."""

import json
import re
from pathlib import Path

import pytest

VARIABLES_PATH = Path("/logs/verifier/notebook_variables.json")

EXPECTED_ANSWERS = {
    "question1": "E",
    "question2": "C",
    "question3": "D",
    "question4": "31 Dec 2029",
    "question5": "9.424%",
    "question6": "18217 k",
    "question7": "1.539",
    "question8": "9.388%",
    "question9": "30 Sep 2024",
    "question10": "16478 k",
    "question11": "1.588",
    "question12": "22586 k",
    "question13": "31 Mar 2028",
    "question14": "9.088%",
    "question15": "1.493",
    "question16": "10.309%",
    "question17": "1.613",
    "question18": "42695 k",
    "question19": "52481 k",
    "question20": "16074 k",
    "question21": "OS 4, 17236 k",
    "question22": "OS 6, 1.625",
    "question23": "OS 3, 67951 k"
}


def normalize_answer(val) -> str:
    """Normalize an answer for comparison."""
    s = str(val).strip()
    # Remove dollar signs
    s = s.replace("$", "")

    # Try compound answers first (Q21-Q23) BEFORE stripping commas.
    # Accept: "OS 4, 17236 k", "Operating Scenario 4, 17236",
    # "OS4: 17236", "OS 4, 17,236 k", etc.
    compound = re.match(
        r'(?:OS|Operating\s*Scenario)\s*(\d+)\s*[,:]\s*(.+)',
        s, re.IGNORECASE
    )
    if compound:
        os_num = compound.group(1)
        value_part = compound.group(2).strip()
        value_part = value_part.replace(",", "")
        value_part = re.sub(r'\s*k\s*$', '', value_part)
        return f"OS {os_num}, {value_part}"

    # For non-compound answers: remove commas, strip k
    s = s.replace(",", "")
    s = re.sub(r'\s*k\s*$', '', s)
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


def test_question4(notebook_variables):
    """Question 4"""
    _check_question(notebook_variables, "question4")


def test_question5(notebook_variables):
    """Question 5"""
    _check_question(notebook_variables, "question5")


def test_question6(notebook_variables):
    """Question 6"""
    _check_question(notebook_variables, "question6")


def test_question7(notebook_variables):
    """Question 7"""
    _check_question(notebook_variables, "question7")


def test_question8(notebook_variables):
    """Question 8"""
    _check_question(notebook_variables, "question8")


def test_question9(notebook_variables):
    """Question 9"""
    _check_question(notebook_variables, "question9")


def test_question10(notebook_variables):
    """Question 10"""
    _check_question(notebook_variables, "question10")


def test_question11(notebook_variables):
    """Question 11"""
    _check_question(notebook_variables, "question11")


def test_question12(notebook_variables):
    """Question 12"""
    _check_question(notebook_variables, "question12")


def test_question13(notebook_variables):
    """Question 13"""
    _check_question(notebook_variables, "question13")


def test_question14(notebook_variables):
    """Question 14"""
    _check_question(notebook_variables, "question14")


def test_question15(notebook_variables):
    """Question 15"""
    _check_question(notebook_variables, "question15")


def test_question16(notebook_variables):
    """Question 16"""
    _check_question(notebook_variables, "question16")


def test_question17(notebook_variables):
    """Question 17"""
    _check_question(notebook_variables, "question17")


def test_question18(notebook_variables):
    """Question 18"""
    _check_question(notebook_variables, "question18")


def test_question19(notebook_variables):
    """Question 19"""
    _check_question(notebook_variables, "question19")


def test_question20(notebook_variables):
    """Question 20"""
    _check_question(notebook_variables, "question20")


def test_question21(notebook_variables):
    """Question 21"""
    _check_question(notebook_variables, "question21")


def test_question22(notebook_variables):
    """Question 22"""
    _check_question(notebook_variables, "question22")


def test_question23(notebook_variables):
    """Question 23"""
    _check_question(notebook_variables, "question23")
