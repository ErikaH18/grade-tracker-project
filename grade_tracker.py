# Grade tracker 
import csv
filepath = "data/students.csv"
def load_students(filepath):
    """Reads the CSV file at filepath and returns a list of dictionaries. Returns an empty list if the file is not found."""
    students = []
    try:
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
        return students
    except FileNotFoundError:
        print(f"Error: Could not find file at '{filepath}'.")
        students = []
        return students

def calculate_average(grades):
    """Takes a list of grade strings, skips empty ones, returns average as a float rounded by 1 decimal, returns None if no valid grades."""
    numeric_grades = []
    for grade in grades:
        if grade != "":
            numeric_grades.append(float(grade))
    if not numeric_grades:
        return None
    else:  
        average = round(sum(numeric_grades) / len(numeric_grades), 1)    
        return average

def get_letter_grade(average):
    """Converts a numeric average into a letter grade. Returns 'N/A' if average is None."""
    if average is None:
        return "N/A"
    elif average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def generate_report(students):
    """Creates a report from the full student list and return a summary dictionary"""
    students_summary = []
    grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0, "N/A": 0}
    if not students:
        print("No students yet.")
        return {
            "total_students": 0,
            "class_average": 0,
            "highest_average": 0,
            "lowest_average": 0,
            "grade_distribution": grade_counts,
            "students": students_summary
        }
    for student in students:
        grades = [student['math'], student['science'], student['english'], student['history']]
        average = calculate_average(grades)
        letter_grade = get_letter_grade(average)    
        students_summary.append({"name": student['student_name'], "average": average, "grade": letter_grade})
    
    averages = [s["average"] for s in students_summary if s["average"] is not None]
    if not averages:
        class_average = 0
        highest_student_average = 0
        lowest_student_average = 0
    else:
        class_average = sum(averages) / len(averages)
        highest_student_average = max(averages)
        lowest_student_average = min(averages)

    for student in students_summary:
        letter = student['grade']
        grade_counts[letter] += 1
    report = {
        "total_students": len(students),
        "class_average": round(class_average, 1),
        "highest_average": highest_student_average,
        "lowest_average": lowest_student_average,
        "grade_distribution": grade_counts,
        "students": students_summary
    }    
    return report
def write_report(report, filepath):
    """ """
    with open(filepath, "w") as file:
        file.write("STUDENTS REPORT".center(40) + "\n")
        file.write("=" * 40 + "\n\n")
        file.write("-- Class-level statistics --\n\n")
        file.write(f"Total students: {report['total_students']}\n")
        file.write(f"Class average: {report['class_average']}\n")
        file.write(f"Highest average: {report['highest_average']}\n")
        file.write(f"Lowest average: {report['lowest_average']}\n\n")

        file.write("-- Grade Distribution --\n\n")
        for grade, count in report['grade_distribution'].items():
            file.write(f"{grade}: {count}\n")

        file.write("\n-- Individual Student results--\n\n")
        for student in report['students']:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Average: {student['average']}\n")
            file.write(f"Letter grade: {student['grade']}\n")
            file.write("\n")
    return

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