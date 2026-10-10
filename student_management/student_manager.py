# Import the random module to generate random student IDs.
import random

# Import PASS_MARK from the analysis module to check subject pass conditions.
from student_management.analysis import PASS_MARK
# Import functions for loading and saving student records.
from student_management.file_handler import load_students, save_students
# Import the Student class so new student objects can be created.
from student_management.student import Student

# Define how many subjects each student record should contain.
SUBJECT_COUNT = 4


# Define the StudentManager class that handles all student operations.
class StudentManager:
    # Define the constructor to load students when the manager is created.
    def __init__(self):
        # Load all existing student records from the CSV file.
        self.students = load_students()

    # Define a method to save the current list of students to storage.
    def save(self):
        # Call the file handler to write the students to the CSV file.
        save_students(self.students)

    # Define a method to find a student by their ID.
    def find_student(self, student_id):
        # Loop through all loaded students.
        for student in self.students:
            # If the current student matches the given ID, return that record.
            if student.id == student_id:
                # Return the matching student object.
                return student
        # Return None when no matching student is found.
        return None

    # Define a method that creates a new unique student ID.
    def make_id(self):
        # Keep generating IDs until a unique one is found.
        while True:
            # Generate a random 4-digit number and convert it to a string.
            student_id = str(random.randint(1000, 9999))
            # If this ID is not already used, return it.
            if self.find_student(student_id) is None:
                # Return the unique ID.
                return student_id

    # Use @staticmethod because this method does not depend on instance data.
    @staticmethod
    def read_number(prompt, integer=False, minimum=0, maximum=100):
        # Keep asking until the user enters a valid number within range.
        while True:
            # Try to read and validate the input.
            try:
                # If integer is True, convert input to an integer.
                if integer:
                    # Read an integer value from the user.
                    value = int(input(prompt))
                # Otherwise, read a floating-point number.
                else:
                    # Read a decimal value from the user.
                    value = float(input(prompt))
                # Check if the value falls within the allowed minimum and maximum.
                if minimum <= value <= maximum:
                    # Return the valid number.
                    return value
            # Catch invalid number input such as letters or symbols.
            except ValueError:
                # Ignore the error and ask again.
                pass
            # Tell the user the acceptable range after an invalid entry.
            print(f"Enter a number from {minimum} to {maximum}.")

    # Define a method to read the subject names and marks for a new student.
    def read_marks(self):
        # Create a dictionary to store subject names and their marks.
        marks = {}
        # Print a message telling the user how many subjects are required.
        print(f"Enter exactly {SUBJECT_COUNT} subjects and their marks.")
        # Loop once for each subject to gather input.
        for number in range(1, SUBJECT_COUNT + 1):
            # Ask the user for the subject name and remove surrounding spaces.
            subject = input(f"Subject {number}: ").strip()
            # Store the subject name and mark in the marks dictionary.
            marks[subject] = self.read_number(
                # Ask the user for the numeric mark for this subject.
                f"Marks for subject {number} (0-100): "
            )
        # Return the completed marks dictionary.
        return marks

    # Define a method to add a new student to the list.
    def add_student(self):
        # Create a new Student object from the collected data.
        student = Student(
            # Generate a unique student ID.
            self.make_id(),
            # Read and trim the student name.
            input("Enter name: ").strip(),
            # Read a valid age from the user.
            self.read_number("Enter age: ", integer=True, minimum=1, maximum=120),
            # Read and trim the course name.
            input("Enter course: ").strip(),
            # Read and trim the department name.
            input("Enter department: ").strip(),
            # Read and trim the academic year.
            input("Enter academic year: ").strip(),
            # Read all subject marks.
            self.read_marks(),
        )
        # Add the new student to the in-memory list.
        self.students.append(student)
        # Save the updated list to disk.
        self.save()
        # Print a confirmation message with the new student's ID.
        print("Student added. ID is", student.id)

    # Define a method to display every student in the system.
    def view_students(self):
        # If the list is empty, print a message and stop.
        if not self.students:
            # Tell the user no students are currently stored.
            print("No students found.")
            # Exit the method.
            return
        # Loop through each student in the list.
        for student in self.students:
            # Print the student's information.
            student.show()

    # Define a method to search for students based on name, course, department, year, or status.
    def search_student(self):
        # Ask the user for a search term and convert it to lowercase for case-insensitive search.
        search_term = input(
            "Search name, course, department, year, or status: "
        ).lower()
        # Create a list to store all matching students.
        matches = []
        # Loop through every student in the system.
        for student in self.students:
            # Combine important student information into one lowercase string.
            details = " ".join(
                [
                    # Add the student name.
                    student.name,
                    # Add the course.
                    student.course,
                    # Add the department.
                    student.department,
                    # Add the academic year.
                    student.year,
                    # Add the current status.
                    student.status,
                ]
            ).lower()
            # If the user's search term appears in the combined details, mark it as a match.
            if search_term in details:
                # Add the student to the matches list.
                matches.append(student)

        # If no student matched the search, print a message and stop.
        if not matches:
            # Tell the user no student was found.
            print("Student not found.")
            # Exit the method.
            return
        # Loop through all matches and display them.
        for student in matches:
            # Show the student's details.
            student.show()

    # Define a method to generate a performance report.
    def performance_report(self):
        # If there are no students, print a message and stop.
        if not self.students:
            # Tell the user there are no students to report on.
            print("No students found.")
            # Exit the method.
            return

        # Print the heading for the performance report.
        print("\nPerformance report")
        # Sort students by average, from highest to lowest.
        ranked_students = sorted(
            self.students, key=lambda student: student.average, reverse=True
        )
        # Loop through the students ranked by performance.
        for student in ranked_students:
            # Print the student's name, average, and current status.
            print(f"{student.name}: {student.average:.2f} | {student.status}")

        # Print a heading for students needing improvement.
        print("\nStudents needing improvement:")
        # Create a list of students identified as needing improvement.
        students_needing_help = [
            student for student in self.students if student.needs_improvement
        ]
        # If there are no students needing improvement, print None and exit.
        if not students_needing_help:
            # Print None to indicate no students are behind.
            print("None")
            # Exit the method.
            return

        # Loop through students who need help.
        for student in students_needing_help:
            # Find subject names where the score is below the pass mark.
            weak_subjects = [
                # Store the subject name if it is below PASS_MARK.
                subject
                for subject, mark in student.marks.items()
                if mark < PASS_MARK
            ]
            # Build a readable reason text using failing subjects or a low average.
            reason = ", ".join(weak_subjects) or "low average"
            # Print the student's name, average, and reason for improvement.
            print(f"{student.name} ({student.average:.2f}) - {reason}")

    # Define a method to update a student's information.
    def update_student(self):
        # Ask the user for the student ID and remove spaces around it.
        student_id = input("Enter student ID: ").strip()
        # Find the student with the matching ID.
        student = self.find_student(student_id)
        # If no student is found, print a message and stop.
        if student is None:
            # Tell the user the student does not exist.
            print("Student not found.")
            # Exit the method.
            return

        # Ask for the new name and remove spaces around it.
        student.name = input("Enter new name: ").strip()
        # Ask for the new age and validate it.
        student.age = self.read_number(
            "Enter new age: ", integer=True, minimum=1, maximum=120
        )
        # Ask for the new course and remove spaces.
        student.course = input("Enter new course: ").strip()
        # Ask for the new department and remove spaces.
        student.department = input("Enter new department: ").strip()
        # Ask for the new academic year and remove spaces.
        student.year = input("Enter new academic year: ").strip()
        # Read all new marks for the student.
        student.marks = self.read_marks()
        # Save the updated student record.
        self.save()
        # Confirm that the update was completed.
        print("Student updated.")

    # Define a method to delete a student from the list.
    def delete_student(self):
        # Ask the user for the ID of the student to delete.
        student_id = input("Enter student ID: ").strip()
        # Find the matching student.
        student = self.find_student(student_id)
        # If no matching student was found, print a message and stop.
        if student is None:
            # Tell the user the student does not exist.
            print("Student not found.")
            # Exit the method.
            return

        # Remove the student from the in-memory list.
        self.students.remove(student)
        # Save the updated student list.
        self.save()
        # Print a success message after deletion.
        print("Student deleted.")
