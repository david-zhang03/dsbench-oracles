# Data Analysis: 2014 Round 2 Time Is Money

## Background

INTRODUCTION
Note: This question should be read along with the accompanying workbook 
You work in the business development team of ETech, a technology company that primarily operates out 
of Europe and prepares its financial statements in Euros.   
ETech has a comprehensive corporate model that you use to analyse the impact of any potential 
acquisitions. The corporate model is prepared in Euros on a nominal basis therefore any acquisition 
analysis needs to be converted to nominal Euros to correctly interface with the corporate model.  
ETech has been approached by JL Goodward, a well-known investment banking firm on behalf of their 
client GEE, a conglomerate. GEE is looking to divest its technology division and has put a sale process in 
place. Your mangers and board of directors are excited by the prospect of acquiring GEE’s technology 
division and have requested entry into the sales process. 
With all the legal formalities out of the way, JL Goodward sends you an Information Memorandum (‘IM’) to 
assist you with preparing your Indicative Bid. In the IM you have been provided with management’s 
forecast performance of the business.  
The forecast includes sales, opex and capex in real US$ and the opening balance of the two classes of 
tax assets in US$.  You are instructed to ignore all other assets and liabilities for the purpose of preparing 
your Indicative Bid. Furthermore you are instructed to make the following assumptions: 
    • GEE’s effective tax rate is 40%. Tax is calculated on the last day of the year and paid
    immediately. Corporate tax will continue to be payable within the US.
    • That all cash flows (Sales, Opex, Capex etc) happen on the last day of the year.
    • Depreciation for Tax and Accounting is done using:
        o For Class A assets, the double declining balance method over 5 years.
        o For Class B assets, the straight line method over 4 years. Assume the opening balance
has not yet been depreciated and will be depreciated over 4 years starting in 2015. 
In order to prepare your bid, you have talked to your tax advisors, investment committee and ETech’s 
management. Based on these discussions, you have settled on the following assumptions relevant to your 
valuation: 
    • There are no cross border implications from the acquisition;
    • You will discount pre financing, post-tax nominal US$ cash flows using a 10% rate in order to
value the assets as at 31 December 2014; 
    • The spot exchange rate as at the valuation date will be 1.31 US$ per 1 Euro;
    • You are provided with a real US$:Euro exchange rate and told that it has been calculated as a
notional exchange rate that can be used to convert directly between real US$ and real Euro. 
Hint: Do not use these rates to directly convert between nominal US$ and nominal Euro. 
    • You have formed a view on inflation for both the US$ and Euro, included in the provided
workbook.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 7 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question7.txt`

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
