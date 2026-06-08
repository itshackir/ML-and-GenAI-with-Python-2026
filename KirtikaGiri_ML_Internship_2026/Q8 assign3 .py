def store_student_details():
    file = open("student.txt", "w")

    name = input("Enter Student Name: ")
    marks = input("Enter Student Marks: ")

    file.write("Name: " + name + "\n")
    file.write("Marks: " + marks)

    file.close()

    print("Student details stored successfully.")

store_student_details()