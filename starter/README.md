# Student Grade Tracker

## Overview

Student Grade Tracker is a Python-based data processing application that reads student grades from a CSV file, calculates individual and class performance metrics, assigns letter grades, and generates a comprehensive summary report.

This project was created as part of a Python Fundamentals pre-work assignment and demonstrates core concepts including:

- File handling
- CSV data processing
- Exception handling
- Functions and modular programming
- Data aggregation and reporting
- Dictionaries and lists
- Basic statistics

---

## Features

### 1. Load Student Data
Reads student records from a CSV file using Python's built-in `csv` module.

Expected CSV columns:

- `student_name`
- `math`
- `science`
- `english`
- `history`

### 2. Calculate Student Averages

- Converts grade values to numeric format
- Ignores empty or invalid values
- Calculates the average of valid grades
- Rounds averages to one decimal place
- Returns `None` when no valid grades exist

### 3. Assign Letter Grades

| Average | Grade |
|----------|--------|
| 90+ | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |
| None | N/A |

### 4. Generate Class Report

The report includes:

- Total number of students
- Class average
- Highest student average
- Lowest student average
- Grade distribution
- Individual student results

### 5. Export Report to a Text File

The application generates a formatted report and saves it as `grade_report.txt`.

---

## Project Structure

```text
starter/
├── data/
│   └── students.csv
├── grade_report.txt
├── grade_tracker.py
└── README.md
```

## Running the Application

```bash
python grade_tracker.py
```

## Functions

- `load_students(filepath)`
- `calculate_average(grades)`
- `get_letter_grade(average)`
- `generate_report(students)`
- `write_report(report, filepath)`

## Skills Demonstrated

- Python Fundamentals
- CSV Processing
- Exception Handling
- Data Validation
- Report Generation
- File I/O Operations

## Future Improvements

- Export to Excel
- Data visualizations
- Unit testing with pytest
- Interactive UI

## Author

Created as part of the Python Fundamentals – Student Grade Tracker assignment.
