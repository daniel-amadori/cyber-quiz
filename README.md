# Cyber Quiz

A command-line quiz in Python to practice Linux commands, written while studying for a career in cybersecurity.

## What it does

The quiz asks a series of questions about Linux commands and tells you after each answer whether it is correct. At the end it shows your score and percentage, with a message based on the result.

## How to run

Requires Python 3.

```bash
git clone https://github.com/daniel-amadori/cyber-quiz.git
cd cyber-quiz
python3 quiz.py
```

## What I learned

- Storing data in a list of `[question, answer]` pairs
- Looping with `for` and unpacking each pair
- Writing functions that return `True` or `False`
- Cleaning user input with `strip()` and `lower()`
- Calculating a percentage with `round()`
- The Git workflow: add, commit, push