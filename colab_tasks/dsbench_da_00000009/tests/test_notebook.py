"""Pytest tests for verifying data analysis answers."""

import json
from pathlib import Path

import pytest

VARIABLES_PATH = Path("/logs/verifier/notebook_variables.json")

EXPECTED_ANSWERS = {
    "question1": {
        "# of words": 7,
        "Xth word": "ALIBI",
        "Highest Word": "BIALY",
        "Highest Score": 21
    },
    "question2": {
        "# of words": 8,
        "Xth word": "RARER",
        "Highest Word": "BARER",
        "Highest Score": 14
    },
    "question3": {
        "# of words": 20,
        "Xth word": "ASSERT",
        "Highest Word": "MARSES",
        "Highest Score": 15
    },
    "question4": {
        "# of words": 7,
        "Xth word": "LANNER",
        "Highest Word": "ALTERN",
        "Highest Score": 9
    },
    "question5": {
        "# of words": 3,
        "Xth word": "RIBAND",
        "Highest Word": "MINBAR",
        "Highest Score": 17
    },
    "question6": {
        "# of words": 14,
        "Xth word": "INARM",
        "Highest Word": "ABRIM",
        "Highest Score": 16
    },
    "question7": {
        "# of words": 7,
        "Xth word": "RECANTS",
        "Highest Word": "CANTERS",
        "Highest Score": 16
    },
    "question8": {
        "# of words": 9,
        "Xth word": "CANERS",
        "Highest Word": "ARCSEC",
        "Highest Score": 17
    },
    "question9": {
        "# of words": 14,
        "Xth word": "TANGI",
        "Highest Word": "AGING",
        "Highest Score": 12
    },
    "question10": {
        "# of words": 6,
        "Xth word": "DECLAIM",
        "Highest Word": "CLAIMED",
        "Highest Score": 21
    },
    "question11": {
        "# of words": 108,
        "Xth word": "BASIC",
        "Highest Word": "SQUAB",
        "Highest Score": 36
    },
    "question12": {
        "# of words": 249,
        "Xth word": "SCARED",
        "Highest Word": "ZERDAS",
        "Highest Score": 37
    },
    "question13": {
        "# of words": 82,
        "Xth word": "STEEDS",
        "Highest Word": "KESHES",
        "Highest Score": 24
    },
    "question14": {
        "# of words": 115,
        "Xth word": "FLAME",
        "Highest Word": "XYLEM",
        "Highest Score": 36
    },
    "question15": {
        "# of words": 47,
        "Xth word": "HINTS",
        "Highest Word": "INFIX",
        "Highest Score": 32
    }
}

SUB_KEYS = ["# of words", "Xth word", "Highest Word", "Highest Score"]


def normalize(val) -> str:
    """Normalize a single sub-answer for comparison."""
    s = str(val).strip()
    try:
        f = float(s)
        if f == int(f):
            return str(int(f))
        return s
    except (ValueError, OverflowError):
        pass
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
        'You must set: answers = {"question1": {...}, ...}'
    )


def test_answers_is_dict(notebook_variables):
    """Test that answers is a dictionary."""
    answers = notebook_variables["answers"]
    assert isinstance(answers, dict), (
        f"answers should be a dict, got {type(answers).__name__}"
    )


def _check_sub_answer(notebook_variables, question_key, sub_key):
    """Check a single sub-answer for a question."""
    answers = notebook_variables.get("answers", {})
    assert question_key in answers, f"Missing answer for {question_key}"

    student_q = answers[question_key]
    assert isinstance(student_q, dict), (
        f"{question_key}: expected a dict with keys {SUB_KEYS}, "
        f"got {type(student_q).__name__}: {student_q!r}"
    )
    assert sub_key in student_q, (
        f"{question_key}: missing key '{sub_key}'. "
        f"Expected keys: {SUB_KEYS}. Got keys: {list(student_q.keys())}"
    )

    expected_val = EXPECTED_ANSWERS[question_key][sub_key]
    student_val = student_q[sub_key]

    student_norm = normalize(student_val)
    expected_norm = normalize(expected_val)

    print(f"\n  {question_key}['{sub_key}']: student={student_norm!r} expected={expected_norm!r}")

    assert student_norm == expected_norm, (
        f"{question_key}['{sub_key}']: expected {expected_norm!r}, got {student_norm!r}"
    )


# Generate test functions for each question x sub-key (60 tests total)
def _make_test(q_num, sub_key):
    safe_sub = sub_key.replace(" ", "_").replace("#", "num")
    def test_fn(notebook_variables):
        _check_sub_answer(notebook_variables, f"question{q_num}", sub_key)
    test_fn.__name__ = f"test_question{q_num}_{safe_sub}"
    test_fn.__doc__ = f"Question {q_num}: {sub_key}"
    return test_fn


for _q in range(1, 16):
    for _sk in SUB_KEYS:
        _test_fn = _make_test(_q, _sk)
        globals()[_test_fn.__name__] = _test_fn
