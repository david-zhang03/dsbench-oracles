# Data Analysis: 2012 Round 2 Monte Carlo

## Background

INTRODUCTION
A friend has approached you asking for help estimating the winning odds on a heavily modified variation of 
a popular dice game. His version of the game works as follows: 
• 
The player rolls 3 dice, each die has 6 sides 
• 
If the total rolled is 3,4,5,16,17 or 18 the player loses 
• 
If the total rolled is 7 or 11 the player wins 
• 
If any other number is rolled, the player rolls again 
• 
Rerolls work the same way as the initial roll, except that if the player rolls the same number as their 
first roll they win. For example if the player rolls 15-13-6-15 they would win 
 
You quickly identify this as a statistical problem but given the complexity and the fact that you slept 
through most of your statistics classes at university, you decide to use a Monte Carlo simulation to 
estimate the odds.  
When preparing your analysis you should assume the following: 
• 
No more than 50 rolls are required to achieve a result 
• 
5000 outcomes are required to prepare your Monte Carlo.  
 
For simplicity, you could use a Data Table to run your Monte Carlo.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 3 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question3.txt`

## Output

You must set an `answers` dictionary variable in your notebook with your answers:

```python
answers = {
    "question1": "YOUR_ANSWER",  # Question 1
    "question2": "YOUR_ANSWER",  # Question 2
    "question3": "YOUR_ANSWER",  # Question 3
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
