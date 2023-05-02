class Animal:
    def __init__(self, type, name, sound):
        self._type = type
        self._name = name
        self._sound = sound

    def type(self):
        return self._type

    def name(self):
        return self._name

    def sound(self):
        return self._sound


def print_animal(o):
    if not isinstance(o, Animal):
        raise TypeError('print_animal(): requires an animal')
    print(f'The {o.type()} is named "{o.name()}" and says "{o.sound()}"')


def print_animal_if_is_instance(i):
    if isinstance(i, Animal):
        print(f'The {i.type()} is named "{i.name()}" and says "{i.sound()}"')
    else:
        raise TypeError('print_animal(): requires an animal')


def main():
    print_animal(Animal('kitten', 'fluffy', 'meow'))
    print_animal(Animal('duck', 'Roland', 'quack'))
    print_animal(Animal('dino', 'jack', 'hello'))
    print_animal_if_is_instance(Animal('kitten', 'fluffy', 'meow'))
    print_animal_if_is_instance(Animal('dino', 'jack', 'hello'))
    print_animal_if_is_instance(Animal('duck', 'Roland', 'quack'))


if __name__ == '__main__':
    main()
