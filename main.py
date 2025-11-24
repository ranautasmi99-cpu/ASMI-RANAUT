# main.py

from utils.validation import validate_integer, validate_non_empty
from utils.file_ops import (
    add_student, 
    get_all_students, 
    search_student, 
    delete_student,
    update_student
)

def add_student_menu():
    print("\n--- Add New Student ---")
    student_id = validate_integer("Enter Student ID: ")
    name = validate_non_empty("Enter Name: ")
    branch = validate_non_empty("Enter Branch: ")
    year = validate_integer("Enter Year: ")

    record = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "year": year
    }

    add_student(record)
    print("Student added successfully!\n")

def view_all_menu():
    print("\n--- All Student Records ---")
    students = get_all_students()
    if not students:
        print("No records found.\n")
        return
    
    for s in students:
        print(f"ID: {s['id']} | Name: {s['name']} | Branch: {s['branch']} | Year: {s['year']}")
    print()

def search_menu():
    print("\n--- Search Student ---")
    student_id = validate_integer("Enter Student ID to search: ")
    student = search_student(student_id)
    if student:
        print(f"\nFOUND:\nID: {student['id']}\nName: {student['name']}\nBranch: {student['branch']}\nYear: {student['year']}\n")
    else:
        print("Student not found.\n")

def delete_menu():
    print("\n--- Delete Student ---")
    student_id = validate_integer("Enter Student ID to delete: ")
    if delete_student(student_id):
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")

def update_menu():
    print("\n--- Update Student ---")
    student_id = validate_integer("Enter Student ID to update: ")
    student = search_student(student_id)

    if not student:
        print("Student not found.\n")
        return

    print("Enter new details (leave blank to keep existing):")
    new_name = input("New Name: ").strip() or student["name"]
    new_branch = input("New Branch: ").strip() or student["branch"]
    new_year = input("New Year: ").strip() or student["year"]

    updated_record = {
        "id": student_id,
        "name": new_name,
        "branch": new_branch,
        "year": int(new_year)
    }

    update_student(student_id, updated_record)
    print("Student updated successfully!\n")


def main():
    while True:
        print("===== STUDENT RECORD SYSTEM =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = validate_integer("Enter your choice: ")

        if choice == 1:
            add_student_menu()
        elif choice == 2:
            view_all_menu()
        elif choice == 3:
            search_menu()
        elif choice == 4:
            update_menu()
        elif choice == 5:
            delete_menu()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()
