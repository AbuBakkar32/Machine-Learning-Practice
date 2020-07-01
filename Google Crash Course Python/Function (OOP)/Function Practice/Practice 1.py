class Elevator:
    def __init__(self, bottom, top, current):
        self.bottom = bottom
        self.top = top
        self.current = current
        pass

    def up(self):
        if self.current < self.top:
            self.current = self.current + 1
        else:
            self.current

    def down(self):
        if self.current > self.bottom:
            self.current = self.current - 1
        else:
            self.current

    def go_to(self, floor):
        self.current = floor


elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)

elevator.down()
print(elevator.current)

elevator.go_to(10)
print(elevator.current)

# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator.current)

