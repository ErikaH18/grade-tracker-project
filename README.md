# Student Grade Tracker

## What This Program Does

A Python program that reads student grade data from a CSV file, calculates averages, assigns letter grades, and writes a formatted summary report to a text file.

## Setup

No external packages needed — this uses only Python's built-in `csv` module.

1. Clone this repo 
2. Run the script `python3 grade_tracker.py`

## Files
```
.
├── data/
│   └── students.csv     ← input data (student names and grades)
├── grade_tracker.py     ← main program (all functions implemented)
├── requirements.txt     ← empty (no external packages)
└── README.md
```

## Usage

running `python3 grade_tracker.py` will:

1. Load student data from `data/students.csv`
2. Generate a class report (totals, averages, grade distribution)
3. Print a summary to the terminal, including the top 5 students
4. Write the full report to `grade_report.txt`

## Sample terminal output

```
Loading student data...
Loaded 15 students.
Generating report...

--- Summary ---
Total students:   15
Class average:    79.4
Highest average:  95.2
Lowest average:   58.2

Grade Distribution:
  A: 3
  B: 4
  C: 5
  D: 2
  F: 1
  N/A: 0

Top 5 students:
  Eve Williams         95.2  (A)
  Noah Garcia          93.0  (A)
  Alice Johnson        91.5  (A)
  Jack Taylor          89.0  (B)
  Grace Lee            86.8  (B)

Report written to grade_report.txt
```

## Error Handling

- **Missing file:** if `data/students.csv` doesn't exist, the program prints an error message and continues without crashing, producing an empty report instead.
- **Missing grades:** blank grade values are skipped; the average is calculated using only the valid grades present.
- **No valid grades:** if a student has no valid grades at all their average is `None` and their letter grade is `N/A`.