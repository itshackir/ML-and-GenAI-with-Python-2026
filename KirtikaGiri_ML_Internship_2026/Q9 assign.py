def read_student_details():
    file = open("student.txt", "r")

    content = file.read()

    print("\nStudent Details:")
    print(content)

    file.close()

read_student_details()