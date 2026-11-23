"""Student Grade Calculator - Week 2 project."""


def get_grade(marks):
    """Return (grade, message) for marks between 0 and 100."""
    if marks >= 90:
        return "A", "Outstanding! Excellent work! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! You're on the right track! 🙂"
    elif marks >= 60:
        return "D", "Fair effort. A little more practice will help! 💪"
    else:
        return "F", "Don't give up! Review the topics and try again. 📚"


def get_valid_marks():
    """Keep asking until the user enters a number from 0 to 100."""
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
        except ValueError:
            print("❌ Please enter a number, not text.")
            continue
        if 0 <= marks <= 100:
            return marks
        print("❌ Marks must be between 0 and 100.")


def main():
    name = input("Enter student name: ").strip().title()
    marks = get_valid_marks()
    grade, message = get_grade(marks)

    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks:g}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()