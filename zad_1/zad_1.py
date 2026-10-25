class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # lista ocen

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 50

    def __str__(self):
        return f"Student: {self.name}, Oceny: {self.marks}"


student_passed = Student("Anna Kowalska", [100, 80, 150])  # 110
student_failed = Student("Jan Nowak", [110, 10, 0])  # 40

print(f"{student_passed.name} zdała test: {student_passed.is_passed()}")
print(f"{student_failed.name} zdał test: {student_failed.is_passed()}")
