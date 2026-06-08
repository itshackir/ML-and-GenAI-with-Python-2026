class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name :", self.name)
        print("Student Marks:", self.marks)

name = input("Enter Student Name: ")
marks = int(input("Enter Student Marks: "))

student1 = Student(name, marks)

student1.display()