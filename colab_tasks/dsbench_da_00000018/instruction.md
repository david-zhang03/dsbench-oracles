# Data Analysis: 2017 Finals Castles In The Air

## Background

INTRODUCTION
All the inputs mentioned below are provided in the workbook for this case study. 
You are working for a company which is considering purchasing a number of properties. You have been 
asked to model each of the available investments to assist in choosing a portfolio (up to a maximum 
purchase price of $1,700,000) that maximises the value to the company, as measured by an increase in 
net present value. The company’s cost of capital is 8%. 
 
AVAILABLE INVESTMENTS 
Full details of the investments may be found on the table on the subsequent page 
• The model should be monthly. For NPV purposes assume that all payments occur at the end of
the month and use the XNPV function. 
• The purchase price for each property should be paid on 31 December 2017.
• The company holds the property for a number of years (the investment length).
• During the investment length, the company receives rental revenue and pays operating costs.
• Where amounts are indexed the base date is 1 January 2018 and the index should step annually
(i.e. a full year of indexation should first be applied on 1 January 2019). Do NOT round inflated 
prices to whole cents in interim calculations. 
• At the end of the investment length, the company will sell the property for the terminal value. The
terminal value is not indexed. 
• For property 4, the company has the option of overhauling the property.
Details of the property without overhaul are listed under property 4a, 
Details of the property with overhaul are listed under property 4b. 
The overhaul cost should not be considered in the purchase price constraint. 
It is NOT possible to invest in both property 4a and property 4b.  
The overhaul cost (which is not indexed). 
 
For Questions 16 to 21, 23, 26, 27, select your answer from a multiple choice list. 
For Questions 22, 24, 25, you are required to type in your answer. 

INVESTMENT DETAILS 
 
              Property 1          Property 2          Property 3          Property 4a          Property 4b
Purchase Price    $450,000            $550,000            $500,000            $470,000            As 4a
Investment length 5 years             5.5 years           6 years             4 years             As 4a
Overhaul cost     N/A                 N/A                 N/A                 N/A                 $125,000 paid 31 Dec 2019
Terminal value    $500,000            $575,000            $550,000            $570,000            $675,000
Rental revenue    $45,000 per year    $60,000 per year    $55,000 per year    $55,000 per year    Up to overhaul as 4a
                  Paid monthly        Paid quarterly      Paid quarterly      Paid monthly        Afterwards:
                  Indexed at 2.5%     (starting March)    (starting January)  Not indexed         $75,000 per year
                                      Indexed at 3%       Indexed at 2%                          Paid monthly
                                                                                                Not indexed
Operating costs   5% of revenues      $4,500 per year     $1,000 in April     $3,000 per year     Up to overhaul as 4a
                                      Paid monthly        $3,000 in October   Paid monthly        Afterwards:
                                      Indexed at 3%       Indexed at 2%       Indexed at 1%       8% of revenues

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

- For multiple choice questions, use the letter only (e.g., `"D"`)
- For numeric answers, use the number (e.g., `1661626`)
- All answers will be compared as strings (case-insensitive for letters)

## Evaluation

- Each question is evaluated independently
- Your score is the fraction of questions answered correctly

## Available Packages

Python standard library, NumPy, pandas, matplotlib, openpyxl, xlrd
