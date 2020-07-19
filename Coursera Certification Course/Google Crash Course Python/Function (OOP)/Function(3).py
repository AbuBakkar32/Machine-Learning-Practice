class Circel:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circel.pi

    def set_radius(self, new_radius):
        self.radius = new_radius


myc = Circel(3)
myc.set_radius(100)
print(myc.area())
