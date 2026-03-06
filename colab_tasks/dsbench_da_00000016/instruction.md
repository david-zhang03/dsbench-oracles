# Data Analysis: 2017 Round 2 Section 1 Collect The Cash

## Background

INSTRUCTIONS
You are preparing a daily cash flow revenue forecast for a company that has 8 customers (Company A – 
Company H), all with very specific payment terms. No expense calculations are required. 
The questions all relate to the 2018 calendar year, but you may need to model before/after this period to 
accurately calculate the cash forecast (calculations should include the relevant days in 2017 and 2019 
where the payment methodology requires it).  
Do not round your answers at any stage in the model. 
A weekday is defined as a Monday, Tuesday, Wednesday, Thursday or Friday. A weekend is defined as 
Saturday and Sunday. There are no holidays to consider. 
You have been provided with an excel workbook file with the ModelOff formatting to use. This file contains 
none of the inputs provided below – you will need to input these yourself. 
 
COMPANY A 
Company A pays a monthly figure of $17.3m. This is paid in 4 segments each month – 11% on day 5, 
21% on day 10, 41% on day 18 and the balance on day 23. Payments are made on the days specified 
even if it is a weekend. 
 
COMPANY B 
Company B has a daily charge of $0.35m that accrues daily. The accrued balance is paid monthly on the 
third Thursday of the month. 
For example, the payment for January 2018 has accruals from the third Friday in December 2017 until the 
third Thursday in January 2018 (inclusive). 
 
COMPANY C 
Company C has a daily charge of $0.18m per day. On weekdays the charge is paid on the same day, on the 
weekends it accrues and is paid on the Monday. 
 
COMPANY D 
Company D has a daily charge of $0.23m. This is paid once per month on the 15th. The monthly payment 
is based on the number of days in that calendar month. Payments are made on the day specified even if it 
is a weekend. 
 
COMPANY E 
The total monthly charge for Company E is calculated based on the number of Tuesdays in the month at a 
rate of $1.96m per Tuesday. This is paid evenly across all the weekdays of that month. 
Round 2 Section 1 - Case Study Information Pack 

COMPANY F 
Company F makes 3 payments per month, each of $5.34m. They are paid on the 7th, 14th and 20th of the 
month. However, if the payment date is a weekend, it is instead paid on the Friday before the weekend. 
 
COMPANY G 
Company G makes a single monthly payment of $9.23m. On even months (February, April etc) it is paid 
on the first weekday of the month. On odd months (January, March etc), it is paid on the third weekday of 
the month. 
 
COMPANY H 
Company H makes a payment of $1.79m every Wednesday. However, if the payment falls on the first 10 
days of the month it is instead paid 1 day earlier. If the payment falls on the last 10 days of the month, it is 
instead paid one day later.
 
For Questions 1 – 9, 11, select your answer from a multiple choice list. 
For Questions 10 and 12, you are required to type in your answer.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 12 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question12.txt`

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
}
```

- For multiple choice questions (Q1-Q9, Q11), use the letter only (e.g., `"D"`)
- For numeric answers (Q10, Q12), provide the dollar amount in millions rounded to 2 decimal places (e.g., `983.01`). The `$` prefix and `m` suffix are optional.
- All answers will be compared as strings (case-insensitive for letters)

## Evaluation

- Each question is evaluated independently
- Your score is the fraction of questions answered correctly

## Available Packages

Python standard library, NumPy, pandas, matplotlib, openpyxl, xlrd
