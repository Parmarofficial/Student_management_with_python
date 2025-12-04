from students import add_student, view_students, update_student, delete_student
from courses import add_courses,view_courses

def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        print("6. add_courses")
        print("7. view_courses")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            age = int(input("Age: "))
            add_student(name, email, phone, age)

        elif choice == "2":
            view_students()

        elif choice == "3":
            sid = int(input("Enter Student ID: "))
            name = input("New Name: ")
            email = input("New Email: ")
            phone = input("New Phone: ")
            age = int(input("New Age: "))
            update_student(sid, name, email, phone, age)

        elif choice == "4":
            sid = int(input("Enter Student ID: "))
            delete_student(sid)

        elif choice == "5":
            break

        elif choice == "6":
            name=input("Enter course name: ")
            add_courses(name)

        elif choice == "7":
            view_courses()

        else:
            print("Invalid choice")

menu()
