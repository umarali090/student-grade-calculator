# Student Grade Calculator

## Project Overview
A Python program that takes a student's name and marks (0-100) and prints the
grade (A-F) with an encouraging message.

**Objectives**
- Practice decision making with if-elif-else
- Validate user input with a while loop
- Organize code into reusable functions

## Setup Instructions
1. Install Python 3.8+ from https://www.python.org/downloads/
2. Clone or download this repository:
   `git clone https://github.com/YOUR-USERNAME/YOUR-REPO.git`
3. Open the folder in VS Code
4. Run: `python grade_calculator.py` (use `python3` on Mac/Linux)

## Code Structure
```
grade_calculator/
├── README.md              # Documentation
├── grade_calculator.py    # Main program
├── test_cases.txt         # Test inputs and expected results
└── screenshots/           # Screenshots of the working program
```

## Grading Logic
| Marks  | Grade | Message                         |
|--------|-------|---------------------------------|
| 90-100 | A     | Outstanding! Excellent work!    |
| 80-89  | B     | Very Good! Keep it up!          |
| 70-79  | C     | Good job! You're on the right track! |
| 60-69  | D     | Fair effort. A little more practice will help! |
| 0-59   | F     | Don't give up! Review the topics and try again. |

## Functions Used
- `get_grade(marks)`: applies the if-elif-else logic and returns the grade and message.
- `get_valid_marks()`: asks for marks repeatedly until the input is a number from 0 to 100.
- `main()`: collects the name, calls the functions, and prints the result.

## How Technical Requirements Were Met
| Requirement | How |
|-------------|-----|
| if-elif-else grading | `get_grade()` checks marks from highest to lowest range |
| Input validation (0-100) | `get_valid_marks()` rejects values outside the range |
| At least one function | Three functions: `get_grade`, `get_valid_marks`, `main` |
| Encouraging messages | Every grade returns its own message |
| While loop for invalid input | `while True` loop in `get_valid_marks()` repeats until valid; `try/except` catches non-numeric input |

## Screenshots
Valid input<img width="1366" height="768" alt="valid_input" src="https://github.com/user-attachments/assets/71cab71c-93c7-44f1-b809-8f803869ffc6" />
Invalid input handling<img width="1366" height="768" alt="invalid_input" src="https://github.com/user-attachments/assets/d0b9d7ba-0ffa-4e74-b18c-332efd70f6ed" />
Grade F<img width="1366" height="768" alt="grade_f" src="https://github.com/user-attachments/assets/4bb9232c-471c-4bd8-a8e6-cb10ee76a470" />

## Testing Evidence
See `test_cases.txt` for boundary and invalid-input tests. Screenshots above
show the program running on those cases.
