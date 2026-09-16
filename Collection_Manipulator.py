students = []

while True:
    print("\nWelcome to the Student Data Organizer!")

    print("\nSelect an option:")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Student
    if choice == 1:
        print("\nEnter student details:")

        student_id = int(input("Student ID: "))
        name = input("Name: ")
        age = int(input("Age: "))
        grade = input("Grade: ")
        dob = input("Date of Birth (YYYY-MM-DD): ")
        subjects = input("Subjects (comma-separated): ")

        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "grade": grade,
            "dob": dob,
            "subjects": subjects
        }

        students.append(student)

        print("\nStudent added successfully!")

    # 2. Display All Students
    elif choice == 2:
        print("\n--- Display All Students ---")

        if len(students) == 0:
            print("No students found.")
        else:
            for student in students:
                print(
                    f"Student ID: {student['id']} | "
                    f"Name: {student['name']} | "
                    f"Age: {student['age']} | "
                    f"Grade: {student['grade']} | "
                    f"Subjects: {student['subjects']}"
                )

    # 3. Update Student Information
    elif choice == 3:
        student_id = int(input("\nEnter Student ID to update: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                student["name"] = input("Enter new name: ")
                student["age"] = int(input("Enter new age: "))
                student["grade"] = input("Enter new grade: ")
                student["dob"] = input("Enter new Date of Birth (YYYY-MM-DD): ")
                student["subjects"] = input("Enter new subjects: ")

                print("Student information updated successfully!")
                found = True
                break

        if found == False:
            print("Student not found.")

    # 4. Delete Student
    elif choice == 4:
        student_id = int(input("\nEnter Student ID to delete: "))

        found = False

        for student in students:
            if student["id"] == student_id:
                students.remove(student)
                print("Student deleted successfully!")
                found = True
                break

        if found == False:
            print("Student not found.")

    # 5. Display Subjects Offered
    elif choice == 5:
        print("\n--- Subjects Offered ---")
        print("1. Math")
        print("2. Science")
        print("3. English")
        print("4. Python")
        print("5. Data Science")
        print("6. Machine Learning")
        print("7. Artificial Intelligence")
        print("8. SQL")

    # 6. Exit
    elif choice == 6:
        print("\nThank you for using Student Data Organizer!")
        break

    else:
        print("\nInvalid choice. Please try again.")