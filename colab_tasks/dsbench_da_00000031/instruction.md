# Data Analysis: 2014 Round 1 Snakes And Ladders

## Background

INTRODUCTION
You and a friend are playing the classic board game of snakes and ladders. Both players begin on the 
start square and take turns rolling a standard 6-sided die. You move forward the number of places rolled 
on the die. If you land on a square that is at the very bottom of a ladder, you move to the top of the ladder. 
If you land on a snake head, you slide down to the bottom of the snake. The winner is the first player to 
the finish square, an exact roll is not required to finish.  
Being a keen Excel user, you decide to simulate the game. Using your preferred method (e.g. a data 
table, VBA, or any other means within Excel) simulate exactly 5,000 games of snakes and ladders, and 
then answer the following questions. 
Do not simulate more than 5,000 games at once, as this could increase your workbook size too much.  
However be sure to run your 5,000 game simulation a few times to make sure your first result was not an 
outlier.  
For the questions that follow: 
     ‘Player 1’ refers to the player who moves first and ‘Player 2’ the player who moves second.
     You may wish to run your simulation several times to ensure your results are consistent.
     Your answers may not match exactly those provided, given the nature of simulation and the
    rounding of the provided answers.  Select the closest answer.

 
THE BOARD 

You use the board (as shown in the image)  to play the game.
 
For clarity, details of the board are as follows: 
The ‘Start’ square is numbered 0, and the ‘Finish’ square is numbered 34. 
 
The board contains the following ladders:
i) 1 → 12
ii) 5 → 16
iii) 11 → 22
iv) 15 → 23
v) 20 → 31

The board contains the following snakes:
i) 7 → 4
ii) 10 → 2
iii) 21 → 13
iv) 24 → 6
v) 33 → 19

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
