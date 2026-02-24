# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   DS,2/21/2026,Edited Script
#   DS,2/22/2026,Added Structured Error Handling
# ------------------------------------------------------------------------------------------ #

# TODO: Import the json
import json # import code from Python's JSON module

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''

FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = None  # Holds a reference to an opened file.
menu_choice: str = ''  # Hold the choice made by the user.
student_data: dict[str,str] = {}  # one row of student data (TODO: Change this to a Dictionary)
students: list = []  # a table of student data
#csv_data: str = ''  # Holds combined CSV data. Note: Remove later since it is NOT needed with the JSON File

# When the program starts, read the json file data into students
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
except FileNotFoundError as e:
    print(f"{FILE_NAME} not found.")
except JSONDecodeError:
    print("Data in file not valid.")
except Exception as e:
    print(f"There was an error opening the file {FILE_NAME}.")
    print(e,e.__doc__) # Why was the __doc__ text purple in the class video but not here?
finally:
    if file is not None and file.closed == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    """The assignment calls for structured error handling on first and last name entry
    and the course video shows a check for letters only, so that is included here, 
    but many names have non-letters in them, most commonly hyphens, spaces, and apostrophes."""
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha(): #This is a bad assumption for names.
                raise ValueError("First name must only contain letters.")
        except ValueError as e:
            print("Invalid first name entry. Continuing.")
        try:
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha(): #Also a bad assumption.
                raise ValueError("Last name must only contain letters.")
        except ValueError as e:
            print("Invalid last name entry. Continuing.")
        course_name = input("Please enter the name of the course: ")
        student_data = {"FirstName": student_first_name, "LastName": student_last_name, "CourseName": course_name}
        students.append(student_data)
        print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Print comma separated values for each row in students
        print("-"*50)
        print("student first name, student last name, course name") # print headers
        for student in students:
            print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file)
            print("The following data was saved to file!")
            print("student first name, student last name, course name")  # need to print headers
            for student in students:
                print(f"{student['FirstName']}, {student['LastName']}, {student['CourseName']}")
        except FileNotFoundError as e: #In case the file was deleted while the program was running.
            print(f"{FILE_NAME} not found.")
        except Exception as e:
            print(f"There was an error opening the file {FILE_NAME}.")
            print(e, e.__doc__)
        finally:
            if file is not None and file.closed == False:
                file.close()

        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
