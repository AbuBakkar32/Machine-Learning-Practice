class Person:
    def __init__(self, name, age):
        self.name = name
        if 20 < age < 80:
            self._age = age
        else:
            raise ValueError('Sorry its not contain the value between 20 t0 80')

    def display(self):
        print(self.name, self._age)

    def set_age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError('Sorry its not contain the value between 20 t0 80')

    def get_age(self):
        print(self._age)


if __name__ == '__main__':
    p = Person('Rakib', 24)
    p.display()


