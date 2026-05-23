print("=== Student Grade Management System ===")

students = {}

# Number of students
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks: "))

    # Grade calculation
    if marks >= 90:
        grade = "A+"
    elif marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"

    students[name] = {
        "Marks": marks,
        "Grade": grade
    }

# Display results
print("\n=== Student Results ===")

for name, details in students.items():
    print(f"Name: {name}")
    print(f"Marks: {details['Marks']}")
    print(f"Grade: {details['Grade']}")
    print("-" * 25)