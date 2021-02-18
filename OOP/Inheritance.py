class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):  # WorkingStudent() is a child of Student()
    def __init__(self, name, school, salary):
        super().__init__(name, school)  # parent class of Student()
        self.salary = salary


sarah = WorkingStudent('Sarah', 'Oxford', 10)

sarah.marks.append(30)
sarah.marks.append(28)
sarah.marks.append(28)

print(f"{sarah.name} get {sarah.salary} mark and his average value is {round(sarah.average(), 2)}")

