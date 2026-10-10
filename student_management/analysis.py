# Define the minimum score required to pass a subject.
PASS_MARK = 40
# Define the minimum average score that counts as acceptable performance.
IMPROVEMENT_AVERAGE = 50


# Define a function to calculate the average of all subject marks.
def calculate_average(marks):
    # If the marks dictionary is empty, return 0 to avoid division by zero.
    if not marks:
        # Return 0 when there are no marks.
        return 0
    # Add all values together and divide by how many subjects exist.
    return sum(marks.values()) / len(marks)


# Define a function to decide whether a student passes or fails.
def calculate_status(marks):
    # If no marks are available, return a message saying there are no marks.
    if not marks:
        # Return a status indicating the student has no marks recorded.
        return "No marks"
    # Check whether every mark is at least the passing threshold.
    if all(mark >= PASS_MARK for mark in marks.values()):
        # Return Pass if all subject marks meet the minimum passing standard.
        return "Pass"
    # Return Fail if at least one subject mark is below the passing standard.
    return "Fail"


# Define a function to check whether a student should receive improvement support.
def needs_improvement(marks):
    # Return True if the student failed any subject or has an average below the improvement threshold.
    return calculate_status(marks) == "Fail" or calculate_average(marks) < IMPROVEMENT_AVERAGE
