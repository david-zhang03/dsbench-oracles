"""Pytest tests for verifying data analysis answers."""

import json
from pathlib import Path

import pytest

VARIABLES_PATH = Path("/logs/verifier/notebook_variables.json")

EXPECTED_ANSWERS = {
    "question1": "CONCATENATE",
    "question2": "LEFT",
    "question3": "LEN",
    "question4": "MID",
    "question5": "PROPER",
    "question6": "REPLACE",
    "question7": "RIGHT",
    "question8": "TRIM",
    "question9": "EDATE",
    "question10": "EOMONTH",
    "question11": "NETWORKDAYS",
    "question12": "WEEKNUM",
    "question13": "WORKDAY",
    "question14": "YEARFRAC",
    "question15": "GETPIVOTDATA",
    "question16": "HLOOKUP",
    "question17": "INDEX",
    "question18": "INDIRECT",
    "question19": "MATCH",
    "question20": "OFFSET",
    "question21": "TRANSPOSE",
    "question22": "ISTEXT",
    "question23": "ABS",
    "question24": "CEILING",
    "question25": "COMBIN",
    "question26": "EVEN",
    "question27": "EXP",
    "question28": "FACT",
    "question29": "FLOOR",
    "question30": "INT",
    "question31": "LN",
    "question32": "LOG",
    "question33": "MOD",
    "question34": "MROUND",
    "question35": "ODD",
    "question36": "PI",
    "question37": "POWER",
    "question38": "RANDBETWEEN",
    "question39": "ACCRINT",
    "question40": "DB",
    "question41": "DOLLARDE",
    "question42": "EFFECT",
    "question43": "FV",
    "question44": "IPMT",
    "question45": "IRR",
    "question46": "MIRR",
    "question47": "PRICE",
    "question48": "RATE",
    "question49": "XIRR",
    "question50": "NPV"
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


def test_question24(notebook_variables):
    """Question 24"""
    _check_question(notebook_variables, "question24")


def test_question25(notebook_variables):
    """Question 25"""
    _check_question(notebook_variables, "question25")


def test_question26(notebook_variables):
    """Question 26"""
    _check_question(notebook_variables, "question26")


def test_question27(notebook_variables):
    """Question 27"""
    _check_question(notebook_variables, "question27")


def test_question28(notebook_variables):
    """Question 28"""
    _check_question(notebook_variables, "question28")


def test_question29(notebook_variables):
    """Question 29"""
    _check_question(notebook_variables, "question29")


def test_question30(notebook_variables):
    """Question 30"""
    _check_question(notebook_variables, "question30")


def test_question31(notebook_variables):
    """Question 31"""
    _check_question(notebook_variables, "question31")


def test_question32(notebook_variables):
    """Question 32"""
    _check_question(notebook_variables, "question32")


def test_question33(notebook_variables):
    """Question 33"""
    _check_question(notebook_variables, "question33")


def test_question34(notebook_variables):
    """Question 34"""
    _check_question(notebook_variables, "question34")


def test_question35(notebook_variables):
    """Question 35"""
    _check_question(notebook_variables, "question35")


def test_question36(notebook_variables):
    """Question 36"""
    _check_question(notebook_variables, "question36")


def test_question37(notebook_variables):
    """Question 37"""
    _check_question(notebook_variables, "question37")


def test_question38(notebook_variables):
    """Question 38"""
    _check_question(notebook_variables, "question38")


def test_question39(notebook_variables):
    """Question 39"""
    _check_question(notebook_variables, "question39")


def test_question40(notebook_variables):
    """Question 40"""
    _check_question(notebook_variables, "question40")


def test_question41(notebook_variables):
    """Question 41"""
    _check_question(notebook_variables, "question41")


def test_question42(notebook_variables):
    """Question 42"""
    _check_question(notebook_variables, "question42")


def test_question43(notebook_variables):
    """Question 43"""
    _check_question(notebook_variables, "question43")


def test_question44(notebook_variables):
    """Question 44"""
    _check_question(notebook_variables, "question44")


def test_question45(notebook_variables):
    """Question 45"""
    _check_question(notebook_variables, "question45")


def test_question46(notebook_variables):
    """Question 46"""
    _check_question(notebook_variables, "question46")


def test_question47(notebook_variables):
    """Question 47"""
    _check_question(notebook_variables, "question47")


def test_question48(notebook_variables):
    """Question 48"""
    _check_question(notebook_variables, "question48")


def test_question49(notebook_variables):
    """Question 49"""
    _check_question(notebook_variables, "question49")


def test_question50(notebook_variables):
    """Question 50"""
    _check_question(notebook_variables, "question50")
