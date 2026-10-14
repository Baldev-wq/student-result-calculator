# Student Result Calculator

**GitHub repository:** [https://github.com/Baldev-wq/student-result-calculator](https://github.com/Baldev-wq/student-result-calculator)

## What this project does

This is a small Python program that calculates a student's average from three marks and gives a simple result. I chose it because it is easy to understand and shows a few basic software design ideas.

## How to run it

Use Python 3 and run:

```text
python Code/student_result.py
```

Enter three marks from 0 to 100 when asked. The program displays the average and result.

## Software design ideas

- **Clear names:** The names `get_mark`, `calculate_average`, and `get_result` describe what each part does. This makes the code easier to read.
- **Small functions:** Each function has one main job. `get_mark` checks one input, `calculate_average` works out the average, and `get_result` chooses the result. This makes changes easier to follow.
- **Input checking:** The program checks that marks are numbers between 0 and 100. This helps stop invalid input from being used.
- **Avoiding repeated code:** The same `get_mark` function is used for all three marks. If the input rule changes, it only needs to be updated in one place.
- **Possible improvement:** The pass mark is written as `50` in `get_result`. A future version could store it as a named constant so it is easier to change.

## My short reflection

I used functions to split the program into smaller parts. I think this makes the code clearer than putting all the steps together in one long section. The program is small, so it does not need extra classes or complicated features.

