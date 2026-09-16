## 📊 Student Data Organizer

* Author: Drashti Vasani
* Course/Project: Python Practical Assignment
-------

A Python-based console application designed to manage student
information. The program allows users to add, display, update, and
delete student records, as well as view the subjects offered.

## 🎯 Project Objectives

👨‍🎓 Student Data Management: Store student information using
Python lists and dictionaries.

📝 Data Entry: Collect student details dynamically using
input().

🔍 Student Record Management: Display, update, and delete
student information.

📚 Subject Management: Display a list of subjects offered by the
program.

-------

## ✨ Features & Functionality

1. 📝 Add Student

The program collects:
* Student ID
* Name
* Age
* Grade
* Date of Birth
* Subjects

The student information is stored in a dictionary and added to the
students list.

2. 📋 Display All Students

The program displays all stored student records, including:
* Student ID
* Name
* Age
* Grade
* Subjects

3. ✏️ Update Student Information

The program asks for the Student ID and allows the user to update:
* Name
* Age
* Grade
* Date of Birth
* Subjects

4. 🗑️ Delete Student

The program asks for the Student ID and removes the matching student
record from the list.

5. 📚 Display Subjects Offered

The program displays the following subjects:
* Math
* Science
* English
* Python
* Data Science
* Machine Learning
* Artificial Intelligence
* SQL

6. 🚪 Exit

The program continues running until the user selects the Exit option.

-------

## 💻 Technologies Used

* Python 3
* Visual Studio Code
* Git & GitHub

-------

## 📚 Concepts Covered

* input()
* Variables
* Lists
* Dictionaries
* str, int
* Type conversion
* if/elif/else
* while loop
* for loop
* len()
* append()
* remove()
* break
* Boolean variables
* f-strings
* Console output

-------

## 📂 Project Files

Student-Data-Organizer/

│
├── Collection_Manipulator.py
├── README.md
├── output_add_student.png
├── output_update_delete.png
└── output_subjects_exit.png

-------

## 🖥️ Sample Output

1. Add Student and Display All Students

Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1

Enter student details:
Student ID: 12661
Name: drashti
Age: 20
Grade: a+
Date of Birth (YYYY-MM-DD): 12-11-2006
Subjects (comma-separated): science

Student added successfully!

Enter your choice: 2

--- Display All Students ---
Student ID: 12661 | Name: drashti | Age: 20 | Grade: a+ | Subjects: science



2. Update and Delete Student

Enter your choice: 3

Enter Student ID to update: 12661
Enter new name: mahi
Enter new age: 21
Enter new grade: a+
Enter new Date of Birth (YYYY-MM-DD): 12-12-2003
Enter new subjects: math
Student information updated successfully!

Enter your choice: 4

Enter Student ID to delete: 12661
Student deleted successfully!



3. Display Subjects Offered and Exit

Enter your choice: 5

--- Subjects Offered ---
1. Math
2. Science
3. English
4. Python
5. Data Science
6. Machine Learning
7. Artificial Intelligence
8. SQL

Enter your choice: 6

Thank you for using Student Data Organizer!

-------



## ▶️ How to Run

Open the project in Visual Studio Code.

Open the Collection_Manipulator.py file.

Open the VS Code terminal.

Run:

python Collection_Manipulator.py

Select an option from the menu and follow the instructions.

-------

## 💾 Data Storage

Student information is stored temporarily in a Python list while the
program is running.

Example:

students = []

Each student is stored as a dictionary:

student = {
    "id": student_id,
    "name": name,
    "age": age,
    "grade": grade,
    "dob": dob,
    "subjects": subjects
}

The data is not stored permanently in a database or external file.

-------

## 🚀 Future Improvements

* Add permanent file or database storage

* Add student search functionality

* Add input validation

* Add more subjects

* Add a graphical user interface

* Add sorting and filtering of student records

-------