# Import the StudentManager class from the student_management.student_manager module so this file can use the app logic.
from student_management.student_manager import StudentManager


# Define the show_menu function to display the available actions to the user.
def show_menu():
    # Print a blank line and then the first menu option.
    print("\n1. Add student")
    # Print the menu option for viewing all students.
    print("2. View students")
    # Print the menu option for searching students.
    print("3. Search student")
    # Print the menu option for updating a student.
    print("4. Update student")
    # Print the menu option for deleting a student.
    print("5. Delete student")
    # Print the menu option for performance analysis.
    print("6. Performance report")
    # Print the option to exit the program.
    print("7. Exit")


# Define the main function that runs the application loop.
def main():
    # Create a StudentManager object so the app can manage student records.
    manager = StudentManager()

    # Keep the menu running until the user chooses to exit.
    while True:
        # Display the menu on each loop iteration.
        show_menu()
        # Ask the user to select an option and store the result in choice.
        choice = input("Enter your choice: ")

        # If the user chooses 1, add a new student.
        if choice == "1":
            # Call the add_student method in the manager.
            manager.add_student()
        # If the user chooses 2, display all students.
        elif choice == "2":
            # Call the view_students method to show every student.
            manager.view_students()
        # If the user chooses 3, search for a student.
        elif choice == "3":
            # Call the search_student method to find matching records.
            manager.search_student()
        # If the user chooses 4, update a student's information.
        elif choice == "4":
            # Call the update_student method.
            manager.update_student()
        # If the user chooses 5, delete a student.
        elif choice == "5":
            # Call the delete_student method.
            manager.delete_student()
        # If the user chooses 6, show the performance report.
        elif choice == "6":
            # Call the performance_report method.
            manager.performance_report()
        # If the user chooses 7, print a thank-you message and exit.
        elif choice == "7":
            # Print a closing message before leaving the program.
            print("Thank you!")
            # Break out of the infinite loop to end the application.
            break
        # If the user enters anything else, show an invalid choice message.
        else:
            # Tell the user the choice was wrong and ask them to try again.
            print("Wrong choice. Try again.")


# This condition ensures the main function runs only when this file is executed directly.
if __name__ == "__main__":
    # Start the application by calling the main function.
    main()
