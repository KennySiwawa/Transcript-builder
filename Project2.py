# Project2_Siwawa.py
# Name: Kenny Siwawa
# Date: July 28, 2025
# Description: Build an unofficial transcript using a data dictionary with validation and display
# Academic Integrity Acknowledgment: I certify that this code is my own work and I have not copied it in whole or part from another source.

def fill_data(course_data):
    """
    Fill the data dictionary with course and grade entries.
    Ensures grade validity and enables grade updates for existing courses.
    """
    valid_grades = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
    continue_entry = 'y'

    print("\n=== Course Entry Section ===")
    print("Enter course codes (e.g., CS101, MATH201) and corresponding letter grades.") # Example course codes and grades too help user understand the format
    print("Valid grades:", ', '.join(valid_grades)) # Printing valid grades for reference to user helps them avoid entering invalid grades

    while continue_entry == 'y':
        course = input("\nEnter a course code (or 'quit' to exit): ").strip().upper()
        
        if course == 'QUIT':
            break
            
        # Validate course code - we need toensure it's not empty and has minimum length
        while not course or len(course) < 2:
            print("\033[31mInvalid course code. Please enter a valid course code (at least 2 characters).\033[0m") # Red color for invalid course code
            course = input("Enter a course code (or 'quit' to exit): ").strip().upper()
            if course == 'QUIT':  # allows the user ro be able to exit the course entry section
                break
            
        grade = input(f"Letter grade for {course}: ").strip().upper() # in this casestrip() removes whitespace from the beginning and end of the input

        # Validate grade input, if invalid, ask user to re-enter and print valid grades for them to use as reference
        while grade not in valid_grades:
            print(f"\033[31m'{grade}' is not a valid letter grade. Please re-enter.\033[0m") # Red color for invalid grade
            print(f"Valid grades: {', '.join(valid_grades)}")
            grade = input(f"Letter grade for {course}: ").upper()

        # Check if course is already in the transcript, if so, ask user if they want to update the grade and also print the existing grade for them to use as reference
        if course in course_data:
            update = input("This course is already listed on the transcript. Update the grade? [y/n]: ").lower()
            if update == 'y':
                course_data[course] = grade
                print(f"\033[32m✓ {course} grade updated to {grade}\033[0m")  # Green color for success
            else:
                print(f"\033[34mKeeping existing grade '{course_data[course]}' for {course}\033[0m")  # Blue for unchanged grade
        else:
            course_data[course] = grade
            print(f"\033[32m✓ {course} added with grade {grade}\033[0m") # Green color for added course

        continue_entry = input("\nEnter another course? [y/n]: ").lower().strip() # in this case strip() removes whitespace from the beginning and end of the input
        while continue_entry not in ['y', 'n']:
            print("\033[31mInvalid response. Please enter 'y' or 'n'.\033[0m") # Red color for invalid response
            continue_entry = input("Enter another course? [y/n]: ").lower().strip()

def display_report(course_data, student_name, student_major):
    """
    Display the formatted transcript report
    """
    print("\nCounty College of Morris")
    print(f"Transcript for  {student_name}")
    print(f"Major:  {student_major}\n")
    print("Course       Grade")
    print("---------------------")
    # Define the desired grade order from best to worst as shown in 'example output'. (which is typically how grades are sorted in a transcript)
    grade_order = ['A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'D', 'F']
    # Sort courses by grade
    for course, grade in sorted(course_data.items(), key=lambda x: grade_order.index(x[1])): # lambda function is used here to sort the courses by grade
        print(f"{course:<12}{grade}") # <12 means we left-align the course code and also right-align the grade


def main():
    """
    Main function to run the transcript application
    """
    print("="*50)
    print("County College of Morris - Transcript Builder")
    print("="*50)
    print("This program helps you create an unofficial transcript.")
    print("You can enter multiple courses and their corresponding grades.")
    print("="*50)
    
    name = input("Enter your full name: ").strip()
    major = input("Enter your major: ").strip()
    data = {}
    fill_data(data)
    
    if data:
        display_report(data, name, major)
        print("\n\033[32m✓ Transcript generated successfully!\033[0m")
    else:
        print("\n\033[33mNo courses were entered. Transcript is empty.\033[0m")
    
    print("\nThank you for using the Transcript Builder!")


# Conditional call to main - ensures the script only runs when executed directly
if __name__ == "__main__":
    main()


