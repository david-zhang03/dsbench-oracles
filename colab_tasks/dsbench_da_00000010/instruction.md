# Data Analysis: 2017 Finals Ladder Up

## Background

INTRODUCTION
Being the keen football (soccer) fan that you are, you were excited to learn that in the 2016/17 season 
there was a football league played between 20 cities of the ancient Byzantine Empire.  The format was a 
double round-robin with each team playing all other teams twice, once at home and once away, for a total 
of 38 games per team. 
You have been provided data for all 380 games.  10 data fields are provided for each game.  They are: 

Field Name     Description
Date           The date of the game, given as text in the format yyyymmdd.
Round          The number of the round (between 1 and 38)
Team_H         The name of the home team.
Team_A         The name of the away team.
Score_H        The number of goals scored by the home team.
Score_A        The number of goals scored by the away team.
Time_HG        Which minute in the game (between 1 and 95) each home goal was scored. This is given as a single text string with each goal separated by a comma (,).
               Minute values followed by an asterisk (*) denote that the goal was from a Penalty Kick.
               If there were no home goals, "---" is the value given.
Time_AG        Which minute in the game (between 1 and 95) each away goal was scored. Other details are as per the Time_HG field.
Player_HG      The jersey number of the goal scorer (between 1 and 22) of each home goal. This is given as a single text string with each goal separated by a comma (,).
               The first value corresponds to the first home goal scored, the second value to the second home goal scored, and so on.
               If there were no home goals, "---" is the value given.
Player_AG      The jersey number of the goal scorer (between 1 and 22) of each away goal. Other details are as per the Player_HG field.

 
The winner of each game is the team that scores the most goals.  If the score is tied, the game is a draw. 
Your task is to build a model of the league ladder, but this model will need to be flexible to answer all of 
the questions.  Read through the questions first to get a sense of what flexibility is required. 
LADDER RULES FOR RANKING TEAMS 
For each game, teams receive 3 points for a win, 1 point for a draw and 0 points for a loss.  Teams 
are ranked on the ladder according to the following criteria, in this order: 
1) Highest number of points 
2) For teams on equal points, rank by highest goal difference (total goals scored less total goals 
conceded) 
3) For teams on equal points and goal difference, rank by highest total goals scored 
4) If two or more teams are still equal after (3), rank those teams equally, but list the equally ranked 
teams in alphabetical order.  (For avoidance of doubt, if M teams are equally ranked in position N, the 
next best team will have rank N+M, not rank N+1.) 

LIST OF TEAMS 
Adrianople
Ani
Antioch
Bari
Chalcedon
Cherson
Constantinople
Dyrrachium
Edessa
Iconium
Kars
Naissus
Nicaea
Nicomedia
Ohrid
Prilep
Samosata
Sardica
Trebizond
Varna
 
This list of teams is also provided in column B of the worksheet ‘Check_Sum’. 
For any questions where the answer is one of the teams, give the Team name, and not the team ID 
number. 
THE CHECK_SUM WORKSHEET 
You should add your own worksheets to the provided data file to perform your calculations and model your 
league ladder.  Some of the questions will ask you for the value of the Check_Sum of a given ladder.  For 
these questions, you should link cells D3:D22 and E3:E22 to your calculated ladder, and then submit 
the value in the green cell at cell F25.  The use of the Check Sum is designed simply to be a way to easily 
assess if all of your ladder ranking positions are correct. 
You can also use the list of team names from cells B3:B20.  You should not use this Check Sum 
worksheet for anything else, nor make any edits to it except for the yellow cells D3:E22. 
Instructions on how to sort your ladder: 
Like any traditional sporting league, your ladder should be sorted by rank, with rank 1 (the highest placed 
team) at the top and rank 20 (the lowest placed team) at the bottom.  If a ladder contains two or more 
teams on equal rank (see point 4 in ‘Ladder Rules for Ranking Teams), equally ranked teams should then 
further be sorted alphabetically by team name for display purposes, but still given an equal rank value. 
Note that a different displayed sort order will give a different Check sum value from the intended answer. 
 
QUESTION SUMMARY 
Questions 1 to 7 are based on the complete data set, with no filtering required. 
Questions 8 to 19 may require you to compile a ladder assuming that some goals and/or some games 
have been filtered out of the data.  After answering each question, remove the effects of any filtering 
before proceeding to the next question.

## Data Files

The data files are available in `/workspace/data/`. Examine the files to understand the structure.

## Questions

Answer the following 20 questions by analyzing the provided data. Each question is in a separate text file in `/workspace/data/`:

- `/workspace/data/question1.txt` through `/workspace/data/question20.txt`

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
    "question17": "YOUR_ANSWER",  # Question 17
    "question18": "YOUR_ANSWER",  # Question 18
    "question19": "YOUR_ANSWER",  # Question 19
    "question20": "YOUR_ANSWER",  # Question 20
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
