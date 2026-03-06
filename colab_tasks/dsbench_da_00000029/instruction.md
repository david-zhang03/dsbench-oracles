# Data Analysis: 2014 Round 2 Stepping Up

## Background

INTRODUCTION
It is your first day at a new employer, a massive company that produces widgets. The company has a 
basic 15 year forecasting model including a profit and loss statement, balance sheet and cash flow 
statement. The previous analyst has already left and there was no chance for a proper handover.  
Fortunately they left you with a series of notes that set out where they believe there are issues in the 
current model. You are required to identify and fix these errors so you can brief the CFO on the model 
outputs. 
For each question below, you will be provided with the previous analyst’s note on where they thought an 
error existed. You will be required to find and correct the error. To assist with this, you are also provided 
the cell reference for where the error(s) are located.  
Once the error(s) are fixed, you will be able to select the correct answer from the multiple choice options 
available. 
YOU MUST complete the questions in sequence. Ensure your model has the correct answer before 
continuing. When making your changes, make sure the change is made across the whole row. 
You should not have to insert any rows or columns to fix the errors in the model. If you do insert rows or 
columns the cell references below will no longer line up to the model.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 10 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question10.txt`

## Output

You must set an `answers` dictionary variable in your notebook with your answers:

```python
answers = {
    "question1": "YOUR_ANSWER",  # Question 1
    "question2": "YOUR_ANSWER",  # Question 2
    "question3": "YOUR_ANSWER",  # Question 3
    "question4": "YOUR_ANSWER",  # Question 4
    "question5": "YOUR_ANSWER",  # Question 5
    "question6": "YOUR_ANSWER",  # Question 6
    "question7": "YOUR_ANSWER",  # Question 7
    "question8": "YOUR_ANSWER",  # Question 8
    "question9": "YOUR_ANSWER",  # Question 9
    "question10": "YOUR_ANSWER",  # Question 10
}
```

- For multiple choice questions, use the letter only (e.g., `"D"`)
- For numeric answers, use the number (e.g., `1661626`)
- All answers will be compared as strings (case-insensitive for letters)

## Evaluation

- Each question is evaluated independently
- Your score is the fraction of questions answered correctly

## Available Packages

Python standard library, NumPy, pandas, matplotlib, openpyxl, xlrd
