"""Pytest tests for verifying titanic predictions."""

import csv
import subprocess
from pathlib import Path

import pandas as pd


def test_predict_script_exists():
    """Test that predict.py exists."""
    predict_script = Path("/workspace/predict.py")
    assert predict_script.exists(), "predict.py not found at /workspace/predict.py"


def test_predict_script_executes():
    """Test that predict.py runs successfully."""
    test_data_path = Path("/tests/test.csv")
    predict_script = Path("/workspace/predict.py")

    assert test_data_path.exists(), f"Test data file not found at {test_data_path}"

    result = subprocess.run(
        ["python3", str(predict_script), str(test_data_path)],
        capture_output=True,
        text=True,
        timeout=300,
        cwd="/workspace",
    )

    assert result.returncode == 0, f"predict.py execution failed: {result.stderr[:500]}"


def test_predictions_file_exists():
    """Test that predictions.csv was created."""
    predictions_path = Path("/workspace/predictions.csv")
    assert predictions_path.exists(), (
        "predictions.csv not found at /workspace/predictions.csv"
    )


def test_predictions_format():
    """Test that predictions have correct format."""
    predictions_path = Path("/workspace/predictions.csv")

    with open(predictions_path, "r") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["PassengerId", "Survived"], (
            f"Invalid header. Expected [\'PassengerId\', \'Survived\'], got {reader.fieldnames}"
        )

        for row in reader:
            assert "PassengerId" in row, f"Missing PassengerId column in row: {row}"
            assert "Survived" in row, f"Missing Survived column in row: {row}"


def test_predictions_completeness():
    """Test that all test samples have predictions."""
    ground_truth_path = Path("/tests/test_ground_truth.csv")
    predictions_path = Path("/workspace/predictions.csv")

    gt_df = pd.read_csv(ground_truth_path)
    pred_df = pd.read_csv(predictions_path)

    assert len(gt_df) == len(pred_df), (
        f"Prediction count mismatch. Expected {len(gt_df)}, got {len(pred_df)}"
    )

    missing_ids = set(gt_df["PassengerId"].astype(str)) - set(pred_df["PassengerId"].astype(str))
    assert len(missing_ids) == 0, (
        f"Missing predictions for {len(missing_ids)} IDs. First few: {list(missing_ids)[:5]}"
    )


def test_accuracy_threshold():
    """Test that accuracy meets the required threshold."""
    ground_truth_path = Path("/tests/test_ground_truth.csv")
    predictions_path = Path("/workspace/predictions.csv")

    gt_df = pd.read_csv(ground_truth_path)
    pred_df = pd.read_csv(predictions_path)

    # Align on ID column
    gt_df = gt_df.sort_values("PassengerId").reset_index(drop=True)
    pred_df = pred_df.sort_values("PassengerId").reset_index(drop=True)

    y_true = gt_df["Survived"].values
    y_pred = pred_df["Survived"].values

    # Compute accuracy
    correct = sum(int(a) == int(b) for a, b in zip(y_true, y_pred))
    accuracy = correct / len(y_true)

    threshold = 0.75

    print(f"\n{'=' * 50}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"Threshold: {threshold:.4f}")
    print(f"Result: {'PASS' if accuracy >= threshold else 'FAIL'}")
    print(f"{'=' * 50}\n")

    assert accuracy >= threshold, (
        f"Accuracy {accuracy:.4f} is below threshold {threshold:.4f}"
    )
