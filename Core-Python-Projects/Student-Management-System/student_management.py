import os
import json


def load_data():
    if not os.path.exists("students.json"):
        return []

    with open("students.json", "r") as file:
        return json.load(file)


def save_data(data):
    with open("students.json", "w") as file:
        json.dump(data, file, indent=4)


def add_student():
    students = load_data()
    roll_no = input("Roll no:")
    name = input("Name:")
    age = input("Age:")
    course = input("Course:")

    student = {"roll_no": roll_no, "name": name, "age": age, "course": course}

    students.append(student)
    save_data(students)
    print("Student Added Successfully\n")


def view_student():
    students = load_data()
    if not students:
        print("No Students Record Found\n")
        return

    print("\n-------STUDENTS LIST-------")

    for student in students:
        print(
            f"Roll No:{student['roll_no']}, Name:{student['name']}, Age:{student['age']}, Course:{student['course']}"
        )
        print()


def search_student():
    students = load_data()
    roll_no = input("Enter Roll No to Search: ")
    found = False

    for student in students:
        if student["roll_no"] == roll_no:
            print(
                f"\n Found- Roll No:{student['roll_no']}, Name:{student['name']}, Age:{student['age']}, Course:{student['course']}"
            )
            found = True
            break

    else:
            print("Student not found\n")


def update_student():
    students = load_data()
    roll_no = input("Enter Roll No to Update Student: ")
    for s in students:
        if s["roll_no"] == roll_no:
            s["name"] = input("New Name: ")
            s["age"] = input("New Age: ")
            s["course"] = input("New Course: ")

            save_data(students)

            print("Student Updated Successfully\n")
            return

        print("\nStudent not found")


def delete_student():
    students = load_data()
    roll_no = input("Enter Roll No to Delete: ")

    new_list = [student for student in students if student["roll_no"] != roll_no]

    if len(new_list) == len(students):
        print("\n Student not found")

    else:

        save_data(new_list)

        print("Student Delete Successfully")


def main():
    while True:
        print("\n------STUDENT MANAGEMENT SYSTEM-------")

        print("1. Add Student")
        print("2. View All Student")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter Your Choice (1-6):")

        if choice == "1":
            add_student()
        if choice == "2":
            view_student()
        if choice == "3":
            search_student()
        if choice == "4":
            update_student()
        if choice == "5":
            delete_student()
        if choice == "6":

            print("Closing Program.....")
            break
    else:
        print("Invalid choice! Try again")


if __name__ == "__main__":
    main()
