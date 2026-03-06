# Binary Classification: Titanic Survival Prediction

Predict which passengers survived the Titanic shipwreck using passenger data.

Training data: /workspace/data/train.csv
Test data: Hidden from you
Output: /workspace/predict.py that loads your trained model and makes predictions

## Task

1. Explore and understand the training data
2. Train a classification model to predict `Survived`
3. Create `/workspace/predict.py` that:
   - Takes test CSV path as `sys.argv[1]`
   - Outputs predictions to `/workspace/predictions.csv`
   - Columns: `PassengerId,Survived` (Survived must be binary 0 or 1)

## Data Format

- Training CSV columns: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked
- Test CSV columns: Same as training but without the `Survived` column
- Target: `Survived` (0 = did not survive, 1 = survived)

### Feature Descriptions

- Pclass: Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd) — proxy for socio-economic status
- Sex: Male or Female
- Age: Age in years (fractional if < 1, estimated ages in form xx.5)
- SibSp: Number of siblings/spouses aboard
- Parch: Number of parents/children aboard
- Ticket: Ticket number
- Fare: Passenger fare
- Cabin: Cabin number
- Embarked: Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)

## Evaluation

Your model is evaluated using **accuracy** (percentage of correctly predicted outcomes):
- You need accuracy >= 0.75 to pass (binary score: 1.0 if >= 0.75, else 0.0)
- Higher accuracy is better (maximum is 1.0)

## Available Packages

Python standard library, NumPy, pandas, scikit-learn, lightgbm, catboost, xgboost, joblib
