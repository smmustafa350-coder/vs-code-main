# ============================================
# Student Marks Management System
# Python Minor Project
# ============================================

# Dynamic Arrays (Lists)

student_names = []

subject1 = []   # English
subject2 = []   # Mathematics
subject3 = []   # Science
subject4 = []   # Computer
subject5 = []   # Social Science


# -------------------------------
# Function to Validate Marks
# -------------------------------

def input_marks(subject_name):
    while True:
        try:
            marks = float(input(f"Enter marks in {subject_name} (0-100): "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100.")

        except ValueError:
            print("Invalid input! Enter numeric value.")


# -------------------------------
# Grade Function
# -------------------------------

def calculate_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# -------------------------------
# Add Student
# -------------------------------

def add_student():

    print("\n========== ADD STUDENT ==========\n")

    name = input("Enter Student Name: ")

    english = input_marks("English")
    maths = input_marks("Mathematics")
    science = input_marks("Science")
    computer = input_marks("Computer")
    social = input_marks("Social Science")

    student_names.append(name)

    subject1.append(english)
    subject2.append(maths)
    subject3.append(science)
    subject4.append(computer)
    subject5.append(social)

    print("\nStudent Added Successfully!\n")


# -------------------------------
# Display Students
# -------------------------------

def display_students():

    if len(student_names) == 0:
        print("\nNo student records found.\n")
        return

    print("\n================ STUDENT RECORDS ================\n")

    print("{:<15}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<10}{:<6}".format(
        "Name",
        "Eng",
        "Math",
        "Sci",
        "Comp",
        "Soc",
        "Total",
        "Percent",
        "Grade"
    ))

    print("-" * 90)

    for i in range(len(student_names)):

        total = (
            subject1[i] +
            subject2[i] +
            subject3[i] +
            subject4[i] +
            subject5[i]
        )

        percentage = total / 5

        grade = calculate_grade(percentage)

        print("{:<15}{:<8}{:<8}{:<8}{:<8}{:<8}{:<8}{:<10.2f}{:<6}".format(
            student_names[i],
            subject1[i],
            subject2[i],
            subject3[i],
            subject4[i],
            subject5[i],
            total,
            percentage,
            grade
        ))


# -------------------------------
# Search Student
# -------------------------------

def search_student():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    name = input("Enter Student Name to Search: ")

    if name in student_names:

        i = student_names.index(name)

        total = (
            subject1[i] +
            subject2[i] +
            subject3[i] +
            subject4[i] +
            subject5[i]
        )

        percentage = total / 5

        grade = calculate_grade(percentage)

        print("\nStudent Found\n")

        print("Name :", student_names[i])
        print("English :", subject1[i])
        print("Mathematics :", subject2[i])
        print("Science :", subject3[i])
        print("Computer :", subject4[i])
        print("Social Science :", subject5[i])
        print("Total :", total)
        print("Percentage :", round(percentage,2))
        print("Grade :", grade)

    else:
        print("\nStudent Not Found.")# -------------------------------
# Update Student Marks
# -------------------------------

def update_student():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    name = input("Enter Student Name to Update: ")

    if name in student_names:

        i = student_names.index(name)

        print("\nEnter New Marks")

        subject1[i] = input_marks("English")
        subject2[i] = input_marks("Mathematics")
        subject3[i] = input_marks("Science")
        subject4[i] = input_marks("Computer")
        subject5[i] = input_marks("Social Science")

        print("\nRecord Updated Successfully!")

    else:
        print("\nStudent Not Found.")


# -------------------------------
# Delete Student
# -------------------------------

def delete_student():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    name = input("Enter Student Name to Delete: ")

    if name in student_names:

        i = student_names.index(name)

        student_names.pop(i)

        subject1.pop(i)
        subject2.pop(i)
        subject3.pop(i)
        subject4.pop(i)
        subject5.pop(i)

        print("\nStudent Record Deleted Successfully!")

    else:
        print("\nStudent Not Found.")


# -------------------------------
# Highest Scorer
# -------------------------------

def highest_scorer():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    highest_total = -1
    highest_index = 0

    for i in range(len(student_names)):

        total = (
            subject1[i] +
            subject2[i] +
            subject3[i] +
            subject4[i] +
            subject5[i]
        )

        if total > highest_total:
            highest_total = total
            highest_index = i

    percentage = highest_total / 5

    print("\n========== HIGHEST SCORER ==========")
    print("Name :", student_names[highest_index])
    print("Total :", highest_total)
    print("Percentage :", round(percentage, 2))
    print("Grade :", calculate_grade(percentage))


# -------------------------------
# Top 5 Students
# -------------------------------

def top_five_students():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    result = []

    for i in range(len(student_names)):

        total = (
            subject1[i] +
            subject2[i] +
            subject3[i] +
            subject4[i] +
            subject5[i]
        )

        percentage = total / 5

        result.append((percentage, student_names[i]))

    result.sort(reverse=True)

    print("\n========== TOP 5 STUDENTS ==========")

    limit = min(5, len(result))

    for i in range(limit):

        print(i + 1, ".", result[i][1], "-", round(result[i][0], 2), "%")


# -------------------------------
# Subject Wise Highest Marks
# -------------------------------

def subject_highest():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    print("\n======= SUBJECT-WISE HIGHEST MARKS =======")

    print("English :", max(subject1))
    print("Mathematics :", max(subject2))
    print("Science :", max(subject3))
    print("Computer :", max(subject4))
    print("Social Science :", max(subject5))


# -------------------------------
# Class Average Percentage
# -------------------------------

def class_average():

    if len(student_names) == 0:
        print("\nNo Records Found.")
        return

    total_percentage = 0

    for i in range(len(student_names)):

        total = (
            subject1[i] +
            subject2[i] +
            subject3[i] +
            subject4[i] +
            subject5[i]
        )

        total_percentage += total / 5

    average = total_percentage / len(student_names)

    print("\nClass Average Percentage :", round(average, 2), "%")


# -------------------------------
# Main Menu
# -------------------------------

while True:

    print("\n")
    print("=" * 50)
    print("     STUDENT MARKS MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Highest Scorer")
    print("7. Top 5 Students")
    print("8. Subject-wise Highest Marks")
    print("9. Class Average Percentage")
    print("10. Exit")

    choice = input("\nEnter Your Choice : ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        highest_scorer()

    elif choice == "7":
        top_five_students()

    elif choice == "8":
        subject_highest()

    elif choice == "9":
        class_average()

    elif choice == "10":
        print("\nThank You for Using Student Marks Management System.")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")