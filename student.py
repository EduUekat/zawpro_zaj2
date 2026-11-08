class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  # lista ocen

    def is_passed(self):
        if not self.marks:
            return False
        average = sum(self.marks) / len(self.marks)
        return average > 49

    def __str__(self):
        return f"Student: {self.name}, Oceny: {self.marks}"
