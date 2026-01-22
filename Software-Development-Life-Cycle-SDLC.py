class Student:
    def __init__(self, name, score1, score2, score3):
        self.name = name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.average = 0
        self.grade = ""

    def calculate_average(self):
        self.average = (self.score1 + self.score2 + self.score3) / 3

    def calculate_grade(self):
        if self.average >= 70:
            self.grade = "A"
        elif self.average >= 60:
            self.grade = "B"
        elif self.average >= 50:
            self.grade = "C"
        elif self.average >= 45:
            self.grade = "D"
        else:
            self.grade = "F"

    def display_result(self):
        print("\nStudent Name:", self.name)
        print("Average Score:", self.average)
        print("Grade:", self.grade)


def add_student():
    name = input("Enter student name: ")
    score1 = int(input("Enter score 1: "))
    score2 = int(input("Enter score 2: "))
    score3 = int(input("Enter score 3: "))

    student = Student(name, score1, score2, score3)
    student.calculate_average()
    student.calculate_grade()
    student.display_result()


add_student()
