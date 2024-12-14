from course import Course

def add_course(courses):
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    year = int(input("Enter year level: "))
    section = input("Enter section: ")
    course = Course(course_id, name, year, section)
    courses[course_id] = course
    print(f"Course {course_id} - {name} added successfully!")


def enroll_student(courses):
    course_id = input("Enter course ID: ")
    if course_id not in courses:
        print("Course not found!")
        return
    student_name = input("Enter student name: ")
    courses[course_id].enroll_student(student_name)
    print(f"Student {student_name} enrolled in course {course_id} successfully!")


def display_courses(courses):
    if not courses:
        print("No courses available.")
    else:
        print("Courses:")
        for course in courses.values():
            print(f"- {course.course_id}: {course.name} (Year {course.year}, Section {course.section})")


def display_students_in_course(courses):
    course_id = input("Enter course ID: ")
    if course_id not in courses:
        print("Course not found!")
        return
    courses[course_id].display_students()


def main():
    courses = {}

    while True:
        print("\nCourse Enrollment Menu:")
        print("1. Add Course")
        print("2. Enroll Student")
        print("3. Display Courses")
        print("4. Display Students in Course")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_course(courses)
        elif choice == '2':
            enroll_student(courses)
        elif choice == '3':
            display_courses(courses)
        elif choice == '4':
            display_students_in_course(courses)
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
