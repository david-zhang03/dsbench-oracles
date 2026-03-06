# Data Analysis: 2015 Round 2 The Price Is Right

## Background

INTRODUCTION
You have been hired by a consortium to assist with their financial modelling for an upcoming tender.  The 
tender is a government contract to operate and maintain for 15 years an existing asset, a major water 
treatment facility.  If successful the consortium plans to set up a new company called “OpCo” (short for 
Operating Company) which will carry out the contract.  As part of the tender submission the consortium is 
required to bid the amount of revenue it would like OpCo to receive in order to operate and maintain the 
asset. 
Your task is to: 
 Model the year 1 expenses in accordance with the data below.
 Model the growth profile of the expenses over the contract life.
 Model the additional Lifecycle Costs (non-recurring one-off expenditure relating to major maintenance
work). 
 Back solve the necessary bid values for the revenue stream, in order to meet the consortium’s internal
revenue sizing conditions. 
You will probably need to build a simple Cash Flow statement of OpCo in order to complete this task. 
Information is provided below regarding the assumed expenses of OpCo, the escalation assumptions for 
both revenues and expenses, as well as general model assumptions.  Use your model to answer the case 
study questions. 
 
ASSUMPTIONS 
General Model Assumptions 
 Your model should be a quarterly model spanning 15 calendar years, from 1 January 2016 to 31
December 2030. 
 Unless otherwise specified, assume all book entries and cashflows occur on the final day of the
quarter. 
 
Revenues 
 Revenues are based on two bid values called Base Payment 1 (“BP1”) and Base Payment 2 (“BP2”)
 BP1 and BP2 are annual amounts, expressed in real January 2016 dollars.
 Revenue payments are made every quarter.  The amount paid each quarter end date is equal to
 
Payment each quarter = (BP1 * 0.25 * IF1) + (BP2 * 0.25 * IF2) 
 IF1 and IF2 refer to Indexation Factor 1 and Indexation Factor 2 (see below).

Expenses 
 Expenses are categorised in four types:
o Labour, which escalates at Indexation Factor 3 (“IF3”)
o Materials, which escalates at Indexation Factor 4 (“IF4”)
o Other Expenses, which escalates at Indexation Factor 5 (“IF5”)
o Profit Margin, which is sized as a set percentage of the total of the other three expense
categories.  This represents a regular and required payment to OpCo’s parent companies. 
 Labour Expenses per quarter are $2,500,000 * IF3
 Materials Expenses per quarter are $1,750,000 * IF4
 Other Expenses per quarter are $750,000 * IF5
 Profit Margin Expenses each quarter are 9.00% of the total of Labour, Materials and Other Expenses.
 
Lifecycle Costs 
 On 31 December 2021, lifecycle costs of $10,000,000 are incurred (no further escalation needs to be
applied to this amount). 
 On 30 June 2028, lifecycle costs of $5,000,000 are incurred (no further escalation needs to be applied
to this amount). 
 Assume these amounts are fully expensed at the time they are incurred, and are not depreciated.  No
profit margin is earned on the Lifecycle Costs. 
 
Escalation and Indexation 
 IF1 is equal to 1.00 at 1 Jan 2016, and increases by 2.2% every subsequent 1 January.
 IF2 is equal to 1.00 at 1 Jan 2016, and increases by 4.0% every subsequent 1 January.
 IF3 is equal to 1.00 at 1 Jan 2016, and increases by 4.8% every 1 July
 IF4 is equal to 1.00 at 1 Jan 2016, and increases by 2.5% every subsequent 1 January
 IF5 is equal to 1.00 at 1 Jan 2016, and increases by 2.0% every 1 July
 
Debt 
 All of OpCo’s Expenses and Lifecycle Costs are paid for by cash at the end of each quarter, after
receiving the Revenue Payments for that quarter. 
 If required, OpCo has access to a short term revolving debt facility.  Any cash shortfall after paying
expenses and lifecycle costs is borrowed from the facility at the end of each quarter.  Any excess cash 
remaining after paying expenses and lifecycle costs is applied towards any outstanding balance of the 
debt facility.   
 When the facility is drawn, interest is charged each quarter at a rate of 3% per quarter of the quarter’s
opening balance. 

Cash Float 
 At the beginning of the contract, OpCo starts with a cash balance of $5,000,000, provided by its
parent companies as operating cash.  At the end of the 15 year contract, OpCo is required to return 
$5,000,000 to its parent companies. 
 
Other Considerations 
 Assume that all taxes are zero.
 Assume that no interest is earned on OpCo’s positive cash account balance.
 
Revenue Sizing Conditions 
 Values for BP1 and BP2 should be set so that the forecast cash balance on 31 Dec 2030 is exactly
zero after paying expenses, returning the cash float and paying any outstanding debt balance. 
 Neither BP1 nor BP2 can be negative (one of them can, in theory, be zero though)
 
In addition to the two conditions above (which should be adhered to for all questions), the following 
additional Revenue Sizing conditions apply to specific questions as indicated: 
 For Questions 27 to 29, Revenue sizing is not needed.
 For Questions 30 to 31, follow the requirements given in the question.
 For Questions 32 to 35, BP1 must be an integer multiple of $500,000.
 For Questions 32 to 37, BP1 and BP2 should be sized so that the term “ADS” is minimized.
o “ADS” stands for Absolute Difference Sum and is equal to the sum over all quarters of D
o D, for any given quarter, is equal to the absolute value of:
 Revenues – Expenses – Lifecycle Costs

There is no workbook provided for this section.  You will need to create your own.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 11 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question11.txt`

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
