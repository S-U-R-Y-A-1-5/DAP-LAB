students = {
    "Rahul": 85,
    "Navya": 72,
    "Jenni": 88,
    "Abhishek": 90
}
name = input("Enter the student's name: ")
if name in students:
    print(f"{name}'s marks: {students[name]}")
else:
    print("Student not found.")
