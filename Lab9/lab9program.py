def create_students():
    return [
        ("Surya", 101, (85, 90, 78), "B"),
        ("Jenni", 102, (88, 76, 92), "A"),
        ("Rahul", 103, (70, 65, 80), "C"),
    ]

def display_all_students(students):
    print("\nAll Students:")
    for student in students:
        print(student)

def add_student(students, name, roll, marks, grade):
    student = (name, roll, marks, grade)
    students.append(student)
    print(f"\nStudent {name} added.")

def search_student(students, roll):
    print(f"\nSearching for Roll Number: {roll}")
    for student in students:
        if student[1] == roll:
            print("Student Found:", student)
            return student
    print("Student not found.")
    return None

def calculate_total_marks(students):
    print("\nTotal Marks for Each Student:")
    for student in students:
        total = sum(student[2])
        print(f"{student[0]} (Roll {student[1]}): Total Marks = {total}")

def update_grade(students, roll, new_grade):
    for i in range(len(students)):
        if students[i][1] == roll:
            name, roll_num, marks, _ = students[i]
            students[i] = (name, roll_num, marks, new_grade)
            print(f"\nGrade updated for Roll {roll} to {new_grade}.")
            return
    print("Student not found.")

def remove_student(students, roll):
    for i in range(len(students)):
        if students[i][1] == roll:
            removed_student = students.pop(i)
            print(f"\nRemoved Student: {removed_student}")
            return
    print("Student not found.")


students = create_students()
display_all_students(students)
add_student(students, "David", 104, (82, 75, 89), "B")
search_student(students, 102)
calculate_total_marks(students)
update_grade(students, 103, "B")
remove_student(students, 104)
display_all_students(students)
