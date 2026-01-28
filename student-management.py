class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print("-" * 30)


class StudentManagementSystem:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print(" Student added successfully!")

    def view_students(self):
        if not self.students:
            print(" No students found.")
        else:
            for student in self.students:
                student.display_details()

    def search_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                print("Student Found:")
                student.display_details()
                return
        print("Student not found.")


def main():
    sms = StudentManagementSystem()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            sid = int(input("Enter ID: "))
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            course = input("Enter Course: ")
            student = Student(sid, name, age, course)
            sms.add_student(student)

        elif choice == "2":
            sms.view_students()

        elif choice == "3":
            sid = int(input("Enter Student ID to search: "))
            sms.search_student(sid)

        elif choice == "4":
            print(" Exiting...")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
