# Data Analysis: 2012 Round 2 Asset Schedule

## Background

INTRODUCTION
You've been asked to prepare model the forecast asset schedules for a new business. As part of the analysis you are 
required to analyze the impact on the forecast deferred tax.  
To help you prepare the analysis you have been provided with following information:  
FORECAST CAPITAL EXPENDITURE 
All capex amounts presented the following table are specified in provided in real 2012 US$m. All Capital expenditure 
is incurred at the first day of each calendar year.  

          2012   2013   2014   2015   2016   2017   2018   2019   2020
Capex      10     64     69     99     89     39     34     23     29

          2021   2022   2023   2024   2025   2026   2027   2028   2029
Capex      69     99     89     39     34     23     29     69     99

 
FORECAST INFLATION 
You have been advised that the inflation rate is forecast to be 3% per annum.  
ACCOUNTING TREATMENT 
For accounting purposes, depreciation on the Capex is calculated on a straight line basis over 12 years.   
TAX TREATMENT 
For taxation purposes, depreciation on Capex is calculated using the diminishing value method at a rate of 40% per 
annum. The taxation rate is currently 30% per annum but is forecast to moving down to 28% from the start of 2016.  
STYLE CONVENTIONS 
In developing your model, you are expected to adhere to the ModelOff style conventions. At the end of this section 
you will be required to submit the model you built when answering this question.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 5 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question5.txt`

## Output

You must set an `answers` dictionary variable in your notebook with your answers:

```python
answers = {
    "question1": "YOUR_ANSWER",  # Question 1
    "question2": "YOUR_ANSWER",  # Question 2
    "question3": "YOUR_ANSWER",  # Question 3
    "question4": "YOUR_ANSWER",  # Question 4
    "question5": "YOUR_ANSWER",  # Question 5
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
