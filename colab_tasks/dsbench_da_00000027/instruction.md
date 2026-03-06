# Data Analysis: 2015 Round 1 Bread And Butter

## Background

INTRODUCTION
You are in the final stages of applying for a job as an analyst at a small private equity firm.  To help 
assess your skills, the firm asks you to complete what it calls its “Bread and Butter” test – an example of 
the fundamental model building work that its analysts need to do day in and day out.   You will need to 
build a dynamic financial model showing the forecast performance of a fictitious technology company they 
are looking to purchase, Macrohard. 
The firm would like a “3-way integrated financial model” – that is a model which includes the 3 standard 
financial statements (Profit and Loss, Balance Sheet, Cash Flow Statement) and allows updates to 
assumption values to correctly flow through to all of the financial statements.  In order to model the 
statements correctly you will also need to do some simple modelling of a debt facility and depreciation 
tranches.  The final output of the model will be the distributions to equity investors and the IRR achieved 
by the equity investors. 
Information is provided below regarding the assumed forecast performance of Macrohard as well as 
general model assumptions.  Use your model to answer the case study questions. 
To assist you, a workbook has been provided that includes some of the assumptions you will need, plus a 
template for the Balance Sheet, and Profit and Loss Statement.  No template is provided for the Cash 
Flow Statement. 
 
ASSUMPTIONS 
General Model Assumptions 
 Your model should be an annual model showing 10 calendar year time periods, plus the initial “Day 0”
Balance Sheet. 
 The equity investment date (“Day 0”) is 31 December 2015.
 The first period (“Year 1”) covers 1 January 2016 to 31 December 2016, and the final model period
(“Year 10”) covers 1 January 2025 to 31 December 2025. Any activity after year 10 is ignored for 
analysis purposes and is not modelled. 
 Unless otherwise specified, assume all cashflows occur on the final day of the period.

Day 0 Transactions / Initial Investment 
 $30,000,000 equity is invested on Day 0.
 $20,000,000 debt is borrowed on Day 0.
 The Balance Sheet Assets on Day 0 are:
    o $3,000,000 cash
    o $3,000,000 accounts receivable
    o $4,000,000 inventory
    o $40,000,000 Property Plant and Equipment (“PPE”)
 
Revenues 
 Year 1 Sales are $25,000,000.
 Sales grow annually by the minimum of either (i) $3,000,000 or (ii) 8% of the previous year’s sales.
 
Cost of Goods Sold 
 Cost of Goods Sold equals 60% of sales
 
Expenses 
 Year 1 Expenses are $3,000,000
 Expenses grow annually by 7% of the previous year’s expenses.
 
Capital Expenditure 
 On the final day of Year 4, additional PPE is purchased for $10,000,000.
 This new purchase is 90% funded by an equity injection on the same day, with the remainder funded
by cash on hand. 
 
Depreciation 
 The original $40,000,000 PPE (purchased on Day 0) depreciates over 10 years in a straight line
method ($4,000,000 per year). 
 The new PPE (purchased at the end of year 4) depreciates over 5 years in a straight line method.
 
Debt 
 Interest is charged on the outstanding debt at a rate of 6.50% per annum.  Interest is paid at the end
of each year. 
 Principal repayments (i.e. not counting interest) are $2,500,000 per year until the debt is repaid.
Repayments are made at the end of each year, immediately after interest payments are made.
 
Payment Terms / Working Capital 
 Inventory at the end of each year is equal to 30% of Cost of Goods Sold
 Accounts Receivable at the end of each year are 10% of Sales
 Accounts Payable at the end of each year are 12% of Cost of Goods Sold plus 15% of Expenses
 
Distributions to Equity 
 At the end of each of year, any amount above $4,000,000 in the cash account after all other
considerations are dealt with is distributed to equity investors.  If there is less than or equal to 
$4,000,000 in the cash account prior to distributions, no distribution is made that year.  Sizing of 
distributions is only constrained by cash available - not by book profits. 
 
Other Considerations 
 Assume that all taxes are zero.
 Assume that no interest is earned / paid on Macrohard’s positive / negative cash account balance.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 15 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question15.txt`

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
}
```

- For multiple choice questions, use the letter only (e.g., `"D"`)
- For numeric answers, use the number (e.g., `1661626`)
- All answers will be compared as strings (case-insensitive for letters)

## Evaluation

- Each question is evaluated independently
- Your score is the fraction of questions answered correctly

## Available Packages

Python standard library, NumPy, pandas, matplotlib, openpyxl, xlrd, scipy
