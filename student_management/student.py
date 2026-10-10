# Import the datetime module so the student record can store today's date automatically.
import datetime

# Import analysis functions used to calculate average, pass/fail status, and improvement needs.
from student_management.analysis import (
    calculate_average,
    calculate_status,
    needs_improvement,
)


# Define the Student class to represent one student record.
class Student:
    # Define the constructor method that initializes a Student object.
    def __init__(self, student_id, name, age, course, department, year, marks=None, date=None):
        # Store the unique student ID.
        self.id = student_id
        # Store the student's name.
        self.name = name
        # Store the student's age.
        self.age = age
        # Store the student's course.
        self.course = course
        # Store the department in which the student is enrolled.
        self.department = department
        # Store the student's academic year.
        self.year = year
        # Store the marks dictionary, or an empty dictionary if no marks were passed.
        self.marks = marks or {}
        # Store the date as the given value or today’s date if no date was provided.
        self.date = date or str(datetime.date.today())

    # Use @property so average can be accessed like an attribute instead of a method.
    @property
    def average(self):
        # Return the calculated average of all marks.
        return calculate_average(self.marks)

    # Use @property so status can be accessed like an attribute.
    @property
    def status(self):
        # Return whether the student passed or failed based on their marks.
        return calculate_status(self.marks)

    # Use @property so needs_improvement can also be accessed like an attribute.
    @property
    def needs_improvement(self):
        # Return whether the student needs improvement based on marks or average.
        return needs_improvement(self.marks)

    # Define a method that prints the student's full details.
    def show(self):
        # Build a formatted string with each subject and mark separated by commas.
        marks_text = ", ".join(
            f"{subject}: {mark:g}" for subject, mark in self.marks.items()
        )
        # Print each student in a readable line with all important information.
        print(
            f"{self.id} | {self.name} | Age: {self.age} | Course: {self.course} | "
            f"Department: {self.department} | Year: {self.year} | "
            f"Marks: {marks_text or 'None'} | Average: {self.average:.2f} | "
            f"Status: {self.status}"
        )

    # Define a method that converts the student object into a list for CSV saving.
    def to_row(self):
        # Return a list containing all data needed to save the student into a CSV row.
        return [
            # Include the student ID.
            self.id,
            # Include the student's name.
            self.name,
            # Include the age.
            self.age,
            # Include the course name.
            self.course,
            # Include the department.
            self.department,
            # Include the year.
            self.year,
            # Include the mark dictionary.
            self.marks,
            # Include the record date.
            self.date,
        ]
