# Optimal Answer Calculator for Exams

## Overview
This Python script is designed to assist students in determining the optimal number of answers they should select on their final exam. It was originally created for students at the Faculty of Electrical Engineering and Computing in Zagreb, particularly for courses such as Machine Learning or Digital Logic. However, it can be adapted to any exam where incorrect answers result in negative points.

## Features
- Calculates the best answering strategy to achieve a passing grade.
- Considers penalties for incorrect answers.
- Provides the 10 most optimal answer combinations.
- Customizable for different exam formats by adjusting parameters.

## How It Works
If a student needs 20 points to pass but only has 10 going into the final exam, they might think about answering exactly 10 questions and hoping for all correct answers. However, if they believe they know more than 10 answers or want to take a calculated risk, this script helps them determine the optimal number of answers to select.

For example, if the penalty for an incorrect answer is 0.33 points, the script might suggest selecting 14 answers. This could result in 11 correct and 3 incorrect answers, leading to a final score of 10.01 points—just enough to pass.

## Parameters
The function `checkOptimumNumberOfAnswers()` accepts the following parameters:

- `maxExamPoints` (*float*): Maximum points obtainable from the exam (default: `30`).
- `numberOfQuestions` (*int*): Total number of questions in the exam (default: `22`).
- `maxPoints` (*float*): Maximum possible points in the course (default: `60`).
- `negativePenaltyPercentage` (*float*): Penalty for incorrect answers as a fraction of the correct answer points (default: `1/3`).
- `minimumPointPercentage` (*float*): Percentage of total points required to pass (default: `0.5`).
- `currentPoints` (*float*): Points the student currently has (default: `0.0`).

## Usage
Call the function with your current score to determine the best answering strategy:
```python
checkOptimumNumberOfAnswers(currentPoints=15.53)
```
This will output the top 10 answer strategies sorted by efficiency.

## Example Output
```
Statistically 10 most optimal solutions are (from best till rest):
1. 20 answers, with 15 correct and 5 incorrect
2. 21 answers, with 16 correct and 5 incorrect
...
```

## Customization
To adapt this script for different exams, modify the function parameters as needed. For example, to set a different penalty for incorrect answers:
```python
checkOptimumNumberOfAnswers(negativePenaltyPercentage=0.25)
```

## License
This script is open-source and can be modified for educational purposes.
