"""A small program that calculates a student's average and result."""


def get_mark(subject):
    """Ask for one mark and keep asking until it is between 0 and 100."""
    while True:
        try:
            mark = float(input(f"Enter the mark for {subject} (0-100): "))
        except ValueError:
            print("Please enter a number.")
            continue

        # Checking the range here keeps invalid marks out of the calculation.
        if 0 <= mark <= 100:
            return mark

        print("The mark must be between 0 and 100.")


def calculate_average(marks):
    """Return the average of the marks supplied."""
    return sum(marks) / len(marks)


def get_result(average):
    """Return a simple pass or fail result based on the average."""
    # A single function keeps the pass rule in one place.
    if average >= 50:
        return "Pass"
    return "Not yet passed"


def main():
    """Get three marks and display the student's average and result."""
    subjects = ["English", "Maths", "Science"]
    marks = []

    # Reusing the same input function avoids repeating validation code.
    for subject in subjects:
        marks.append(get_mark(subject))

    average = calculate_average(marks)
    result = get_result(average)

    print(f"Average: {average:.1f}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
