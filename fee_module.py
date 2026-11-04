def calculate_fee(credit_hours, fee_per_credit):
    return credit_hours * fee_per_credit

courses = {
    1: {
        "course_name": "Information Technology",
        "credit_hours": 10,
        "fee_per_credit": 150
    },
    2: {
        "course_name": "Software Engineering",
        "credit_hours": 12,
        "fee_per_credit": 180
    },
    3: {
        "course_name": "Data Science",
        "credit_hours": 15,
        "fee_per_credit": 200
    }
}

class Student:
    def __init__(self, student_name, course_choice, course_name,
                 credit_hours, total_fee):
        self.student_name = student_name
        self.course_choice = course_choice
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.total_fee = total_fee

    def display_info(self):
        if self.total_fee > 2000:
            category = "High Fee"
        else:
            category = "Normal Fee"

        print("\nStudent Name:", self.student_name)
        print("Course Choice:", self.course_choice)
        print("Course Name:", self.course_name)
        print("Credit Hours:", self.credit_hours)
        print(f"Total Fee: RM {self.total_fee:.2f}")
        print("Fee Category:", category)
        