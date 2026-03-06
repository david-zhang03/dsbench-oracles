# Data Analysis: 2013 Round 1 Acquisition Financing

## Background

INTRODUCTION
You’ve been asked to prepare a model to forecast the performance of a multiple tranche debt facility that 
will be drawn by an investment fund to purchase assets.  The facility is only drawn when it is needed to 
finance the purchasing of an asset in to the fund, and each asset purchased will map to its own tranche in 
the facility. 
 
TRANCHE DETAILS 
The facility is forecast to have 4 tranches. Details of each tranche are given in the table over page. 
 
INTEREST BASIS AND TIMING ASSUMPTIONS 
Assume that all interest is calculated on a 30/360 basis on the opening daily balance.  All interest rates 
given are simple annual rates (not effective-annual compounding rates). All cash flows, payment dates 
and interest accrual dates occur on calendar quarter end dates. 

|                | Tranche 1                                  | Tranche 2                                 | Tranche 3                                | Tranche 4                                              |
|----------------|--------------------------------------------|------------------------------------------|-----------------------------------------|--------------------------------------------------------|
| Drawdowns      | $14m on 31 Dec 2013                        | $25m on 31 Dec 2013                      | $10m on 30 Jun 2014                      | $22m on 30 Sep 2014                                   |
|                |                                            |                                          | $4m on 31 Mar 2015                       |                                                        |
| Term length    | 7                                          | 9                                        | 4                                        | 6                                                      |
| (years from    |                                            |                                          |                                          |                                                      |
| first drawdown |                                            |                                          |                                          |                                                      |
| of tranche)    |                                            |                                          |                                          |                                                      |
| Interest rate  | 8.25%                                      | 9.00% during interest only period.       | 7.45%                                   | 8.20% for the first two years.                         |
|                |                                            | 8.50% during the amortization period.    |                                         | 7.70% for the remainder of the term.                  |
| Repayment      | Interest is paid every quarter.            | Interest is paid every quarter.          | Interest is paid every quarter.         | Interest is capitalized every quarter for 2 years, and |
| profile and    | Tranche amortizes quarterly in arrears     | The loan is interest only for the first  | The loan is interest only with a bullet | is paid each quarter thereafter.                      |
| other details  | on a credit foncier schedule (that is,     | 5 years, and thereafter amortizes        | payment at maturity.                    | The loan (including the capitalized interest)         |
|                | equal total Principal + Interest payments) | quarterly in arrears via level Principal |                                         | amortizes after the interest capitalization period via |
|                |                                            | repayments (the first principal          |                                         | 16 equal principal payments, paid quarterly in arrears, |
|                |                                            | repayment is 5.25 years after drawdown)  |                                         | with the first payment on 31 December 2016.           |

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 6 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question6.txt`

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
