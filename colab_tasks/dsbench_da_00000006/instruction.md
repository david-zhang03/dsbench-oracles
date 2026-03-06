# Data Analysis: 2016 Round 2 Section 3 Tally Up

## Background

INTRODUCTION
An election has been held for the Congress in the fictional country of Excelstan.  Excelstan is a small 
country and is divided into 9 Districts, named after letters of the Greek alphabet.  Each District elects one 
member to Congress.  There are 1000 voters.  Each voter is assigned a District Code based on where 
they live.  The District Code is a number between 105 and 194 and determines what District the voter 
votes for. 
District Code | District
105 - 114 Alpha
115 - 124 Beta
125 - 134 Gamma
135 - 144 Delta
145 - 154 Epsilon
155 - 164 Zeta
165 - 174 Eta
175 - 184 Theta
185 - 194 Iota
 
There are 8 political parties in Excelstan competing for seats in the Congress. 
The parties are Red, Orange, Yellow, Green, Blue, Purple, Brown and Black. 
Voters cast their ballot by numbering 1 against their first choice.  After this, they can choose to provide 
preferences by numbering 2 against their second choice, 3 against their third choice, and so on up to 8 
against their eighth choice.  Voters can choose how far down they give preferences to. In the data 
provided, every voter has voted for either 4, 5, 6, 7 or 8 parties in preferential order. 
When counting votes, if a voter has not provided a preference number against a particular party, assume 
they gave that party an 8 (i.e. they ranked any unmarked party equal last). 
Each District is counted independently of the other Districts, using only the votes from that 
District. 
COUNTING THE VOTES 
Excelstan has two different systems for counting votes to determine which party wins each District. 
Counting System 1: First Past The Post 
Counting System 2: Points Allocation (also known as ‘Eurovision style’) 

COUNTING SYSTEM 1: FIRST PAST THE POST 
The party with the most number of “1” votes wins.  If two or more parties tie for the most number of “1” 
votes, then the winner is the party that received the most “2” votes (from the set of parties that tied for the 
most “1” votes).  If there is still a tie, then count the “3” votes and so on until a winner is determined. 
 
COUNTING SYSTEM 2: POINTS ALLOCATION 
Parties receive points for each vote. The better the preference, the more points received. 

Vote Preference    Points
1                  12
2                  10
3                  8
4                  6
5                  4
6                  2
7                  1
8                  0

 
The party with the highest number of points wins the District. 
 
The workbook provided contains all of the voting data.  In order to answer all of the questions, you will 
need to use the rules of each counting system below to determine the winning party or parties for each 
District under each counting system. 
Questions 17 to 19 and 26 relate to multiple Counting Systems. 
Questions 20 to 22 relate to Counting System 1: First Past the Post 
Questions 23 to 25 relate to Counting System 2: Points Allocation 
 

For Questions 17 to 24, select your answer from a multiple choice list. 
For Questions 25 to 26, you are required to type in your answer.

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
