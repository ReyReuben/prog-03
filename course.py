class Course:
    def __init__(self, course_id, name, year, section):
        self.course_id = course_id
        self.name = name
        self.year = year
        self.section = section
        self.enrolled_students = []

    def enroll_student(self, student_name):
        self.enrolled_students.append(student_name)

    def display_students(self):
        if not self.enrolled_students:
            print("No students enrolled in this course.")
        else:
            print(f"Students in {self.course_id} - {self.name}:")
            for student in self.enrolled_students:
                print(f"- {student}")
