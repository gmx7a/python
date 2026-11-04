import fee_module

students = []

while True:
    print("\nStudent Course Fee Management System")
    print("1 - Information Technology")
    print("2 - Software Engineering")
    print("3 - Data Science")

    student_name = input("\nEnter student name: ").strip()

    if student_name == "":
        print("Student name cannot be empty.")
        continue

    try:
        course_choice = int(input("Enter course choice (1-3): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if course_choice not in fee_module.courses:
        print("Invalid course choice.")
        continue

    course = fee_module.courses[course_choice]

    total_fee = fee_module.calculate_fee(
        course["credit_hours"],
        course["fee_per_credit"]
    )

    student = fee_module.Student(
        student_name,
        course_choice,
        course["course_name"],
        course["credit_hours"],
        total_fee
    )

    students.append(student)
    student.display_info()

    again = input("\nAdd another student? (y/n): ").strip().lower()

    if again != "y":
        break

print("\n========All Student Records========")

for student in students:
    student.display_info()