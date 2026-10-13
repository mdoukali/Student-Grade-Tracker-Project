"""
Project: Student Grade Tracker
Pre-Work Section C — Python Fundamentals
Estimated time: 45-60 minutes

Objective: Build a data processing script that reads student grades from
a CSV, calculates averages, assigns letter grades, and writes a summary report.

Your job: implement all the functions marked with # TODO.
Do NOT modify the function signatures or the main() function.
"""

import csv

# ============================================================
# FUNCTION 1: Load data from CSV
# ============================================================

def load_students(filepath: str) -> list[dict]:
    """
    Read student data from a CSV file.

    Each row becomes a dictionary. The CSV has columns:
    student_name, math, science, english, history

    Some cells may be empty strings (missing grades) — that's expected.

    Args:
        filepath: Path to the CSV file.

    Returns:
        A list of dicts, one per student.
        Example: [{"student_name": "Alice", "math": "92", ...}, ...]

    Raises:
        FileNotFoundError: if the CSV file doesn't exist.
    """

    student_list = []
    try:
        with open(filepath) as file:
            read_data = csv.DictReader(file)
            for row in read_data:
                student_list.append(row)
        return student_list
    except FileNotFoundError:
            print("File not found.") 

    return []

# ============================================================
# FUNCTION 2: Calculate average, handling missing values
# ============================================================

def calculate_average(grades: list) -> float | None:
    """
    Calculate the average of a list of grade values.

    Grade values may be strings (from the CSV), empty strings, or numbers.
    Ignore any value that can't be converted to a float.

    Args:
        grades: A list of values (e.g., ["92", "88", "", "79"]).

    Returns:
        The average as a float, rounded to 1 decimal place.
        Returns None if there are no valid grades.
    """

    sum_grades = 0
    count = 0

    for grade in grades:
        try:
            float_number = float(grade)
            sum_grades += float_number
            count += 1
        except (ValueError, TypeError):
            continue

    if count == 0:
        return None
    
    return round(sum_grades / count, 1)

# ============================================================
# FUNCTION 3: Assign letter grade
# ============================================================

def get_letter_grade(average: float | None) -> str:
    """
    Convert a numeric average to a letter grade.

    Scale:
        90+  → "A"
        80-89 → "B"
        70-79 → "C"
        60-69 → "D"
        < 60  → "F"
        None  → "N/A" (no grades available)

    Args:
        average: The numeric average, or None.

    Returns:
        The letter grade as a string.
    """
    
    if average >= 90:
        return "A"
    elif average < 90 and average >= 80:
        return "B"
    elif average < 80 and average >= 70:
        return "C"
    elif average < 70 and average >= 60:
        return "D"
    elif average < 60:
        return "F"
    else:
        return "N/A"

# ============================================================
# FUNCTION 4: Generate summary report
# ============================================================

def generate_report(students: list[dict]) -> dict:
    """
    Generate a class summary report.

    Args:
        students: The list of student dicts from load_students().

    Returns:
        A dict with these keys:
            "total_students":   int — how many students
            "class_average":    float — average of all valid averages
            "highest_average":  float — the best average
            "lowest_average":   float — the lowest average
            "grade_distribution": dict — {"A": 3, "B": 5, ...}
            "students":         list of dicts, each with:
                                  name, average, grade
    """

    student_stats = []
    grade_dist = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    student_averages = []

    total_students = 0
    class_average = 0

    for dictionaries in students:
        total_students += 1
        student_averages.append(calculate_average([dictionaries['math'], dictionaries['science'], dictionaries['english'], dictionaries['history']]))
        
    highest_score = student_averages[0]
    lowest_score = student_averages[0]

    for grade in student_averages:
        if grade > highest_score:
            highest_score = grade
        if grade < lowest_score:
            lowest_score = grade
        letter_grade = get_letter_grade(grade)
        grade_dist[letter_grade] += 1

    class_average = calculate_average(student_averages)

    grade = calculate_average([dictionaries['math'], dictionaries['science'], dictionaries['english'], dictionaries['history']])

    for dictionaries in students:

        grade = calculate_average([dictionaries['math'], dictionaries['science'], dictionaries['english'], dictionaries['history']])

        student_stats.append({
            "name": dictionaries["student_name"],
            "average": grade,
            "grade": get_letter_grade(grade)
        })
    
    return {
        "total_students": total_students,
        "class_average": class_average,
        "highest_average": highest_score,
        "lowest_average": lowest_score,
        "grade_distribution": grade_dist,
        "students": student_stats
    }

# ============================================================
# FUNCTION 5: Write report to a file
# ============================================================

def write_report(report: dict, filepath: str) -> None:
    """
    Write the summary report to a text file.

    Format example:
        ===========================
        STUDENT GRADE REPORT
        ===========================
        Total students: 15
        Class average:  81.3
        Highest average: 95.0
        Lowest average:  55.0

        Grade Distribution:
          A: 5
          B: 4
          ...

        Individual Results:
          Alice Johnson    Avg: 91.5  Grade: A
          ...

    Args:
        report:   The dict returned by generate_report().
        filepath: Path to write the report file.
    """

    students = load_students("data/students.csv")
    report = generate_report(students)
    grade_distribution = report['grade_distribution']
    student_info = report['students']
    
    with open(filepath, "w") as f:
        f.write("*" * 30)
        f.write("\n    STUDENT GRADE REPORT:\n")
        f.write("*" * 30)
        f.write(f"\nTotal students: {report['total_students']}")
        f.write(f"\nClass average: {report['class_average']}%")
        f.write(f"\nHighest average: {report['highest_average']}%")
        f.write(f"\nLowest average: {report['lowest_average']}%\n")
        f.write(f"\nGrade Distribution:")

        for letter, count in grade_distribution.items():
            f.write(f"\n{letter}: {count}\n")

        f.write("\nIndividual Results: \n")

        for info in student_info:
            f.write(f"\n  {info['name']}  {info['average']}%  {info['grade']}")

# ============================================================
# MAIN — do not modify
# ============================================================

def main():
    print("Loading student data...")
    students = load_students("data/students.csv")
    print(f"Loaded {len(students)} students.")

    print("Generating report...")
    report = generate_report(students)

    print("\n--- Summary ---")
    print(f"Total students:   {report['total_students']}")
    print(f"Class average:    {report['class_average']}")
    print(f"Highest average:  {report['highest_average']}")
    print(f"Lowest average:   {report['lowest_average']}")

    print("\nGrade Distribution:")
    for grade, count in sorted(report["grade_distribution"].items()):
        print(f"  {grade}: {count}")

    print("\nTop 5 students:")
    sorted_students = sorted(
        [s for s in report["students"] if s["average"] is not None],
        key=lambda s: s["average"],
        reverse=True
    )
    for s in sorted_students[:5]:
        print(f"  {s['name']:<20} {s['average']:.1f}  ({s['grade']})")

    write_report(report, "grade_report.txt")
    print("\nReport written to grade_report.txt")

if __name__ == "__main__":
    main()
