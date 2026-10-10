# Import the csv module to read and write data in CSV format.
import csv
# Import json so subject marks can be stored as a string in the CSV file.
import json
# Import Path to build a correct file path to the data file.
from pathlib import Path

# Import the Student class so student rows can be converted into Student objects.
from student_management.student import Student

# Build the path to the students.csv file in the data folder.
DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "students.csv"
# Define the headers used in the CSV file.
HEADERS = [
    # The student's unique ID.
    "id",
    # The student's name.
    "name",
    # The student's age.
    "age",
    # The student's course.
    "course",
    # The department where the student belongs.
    "department",
    # The academic year of the student.
    "year",
    # A JSON string containing subject marks.
    "subject_marks",
    # The date on which the record was created or last updated.
    "date",
]


# Define a function to load all student records from the CSV file.
def load_students():
    # Create an empty list to hold student objects.
    students = []
    # If the data file does not exist, return an empty list.
    if not DATA_FILE.exists():
        # Return the empty list because there are no saved students.
        return students

    # Open the CSV file for reading with UTF-8 encoding.
    with DATA_FILE.open("r", newline="", encoding="utf-8") as file:
        # Create a CSV dictionary reader that reads rows as dictionaries.
        reader = csv.DictReader(file)
        # Loop through every row in the CSV file.
        for row in reader:
            # If the CSV includes the subject_marks column, use the JSON format.
            if "subject_marks" in (reader.fieldnames or []):
                # Convert the JSON string back into a Python dictionary of subject names and marks.
                marks = json.loads(row.get("subject_marks") or "{}")
                # Read the department value from the row.
                department = row["department"]
                # Read the academic year from the row.
                year = row["year"]
            # Else, this is an older version of the CSV file with a grade field.
            else:
                # Get the grade value from the row if present.
                grade = row.get("grade", "")
                # Start with no marks.
                marks = {}
                # If the grade is numeric, store it as an "Overall" mark.
                if grade.replace(".", "", 1).isdigit():
                    # Create a single-entry marks dictionary for the grade.
                    marks = {"Overall": float(grade)}
                # If no department is available, mark it as Unknown.
                department = "Unknown"
                # If no year is available, mark it as Unknown.
                year = "Unknown"

            # Convert every mark value to a float so calculations work properly.
            marks = {subject: float(mark) for subject, mark in marks.items()}
            # Add a new Student object to the list using the CSV row data.
            students.append(
                # Create a Student object from the parsed data.
                Student(
                    # Store the student ID.
                    row["id"],
                    # Store the student name.
                    row["name"],
                    # Store the age.
                    row["age"],
                    # Store the course title.
                    row["course"],
                    # Use the department value from the CSV row.
                    department,
                    # Use the year value from the CSV row.
                    year,
                    # Pass the loaded marks dictionary.
                    marks,
                    # Store the date from the CSV row.
                    row["date"],
                )
            )

    # Return the list of loaded students.
    return students


# Define a function to save all student records to the CSV file.
def save_students(students):
    # Ensure the data folder exists before saving the file.
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    # Open the CSV file in write mode with UTF-8 encoding.
    with DATA_FILE.open("w", newline="", encoding="utf-8") as file:
        # Create a CSV writer to write rows.
        writer = csv.writer(file)
        # Write the header row to the CSV file.
        writer.writerow(HEADERS)
        # Loop through each student object in the list.
        for student in students:
            # Convert the Student object into a row list.
            row = student.to_row()
            # Convert the marks dictionary to a JSON string because CSV cells store text.
            row[6] = json.dumps(row[6])
            # Write the student data row to the CSV file.
            writer.writerow(row)
