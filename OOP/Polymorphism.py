class Car:
    def start(self):
        print("engine start")

    def move(self):
        print('Car is running')

    def stop(self):
        print('Brakes applied')


class Clock:
    def move(self):
        print('Tick Tick Tick')

    def stop(self):
        print('Clock Needles Stopped')


class Person:
    def move(self):
        print('Person Now Working')

    def stop(self):
        print('Person Stop to walk')

    def talk(self):
        print('Hello Everyone!')


car = Car()
clock = Clock()
person = Person()

# polymorphism apply
def do_something(x):
    x.move()
    x.stop()

do_something(car)
do_something(clock)
do_something(person)