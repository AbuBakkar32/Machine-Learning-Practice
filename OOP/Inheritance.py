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


#############################################################################################

class Mother:
    def cook(self):
        print('Can cook pasta')


class Father:
    def cook(self):
        print('Can cook noodles')


class Daughter(Father, Mother):
    pass


class Son(Mother, Father):
    def cook(self):
        super().cook()
        print('Can cook butter chicken')


d = Daughter()
s = Son()

d.cook()
print()
s.cook()