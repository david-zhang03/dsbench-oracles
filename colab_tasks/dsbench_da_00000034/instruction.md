# Data Analysis: 2013 Round 2 Data Analysis

## Background

INTRODUCTION
You are working as a business analyst at a leading hardware retailer. You have been asked to assist with 
the analysis of some recent sales data from one of your hardware stores. 
 
DATA STRUCTURE 
The data covers the first 6 months of the year 2013 and has a line for each different item type sold on 
each invoice. One or more lines may be associated with a single invoice. 
 
Note that each line also has a quantity field that represents the quantity of that particular item type sold on 
that invoice. 
  
Each invoice is associated with one Manager on Duty and one Sales Assistant. 
 
RECOMMENDED APPROACH  
The format of the data and the questions you will need to answer very strongly lends itself to doing the 
analysis with the aid of a PivotTable. You may also benefit from adding some extra calculation columns to 
the table of data.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 16 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question16.txt`

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
    "question11": "YOUR_ANSWER",  # Question 11
    "question12": "YOUR_ANSWER",  # Question 12
    "question13": "YOUR_ANSWER",  # Question 13
    "question14": "YOUR_ANSWER",  # Question 14
    "question15": "YOUR_ANSWER",  # Question 15
    "question16": "YOUR_ANSWER",  # Question 16
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
