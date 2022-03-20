import time


class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    calculate the total execution time of the program
    """

    def __enter__(self):
        self.start = time.time()
        self.end = 0.0
        return lambda: self.end - self.start

    def __exit__(self, *args):
        self.end = time.time()


with Time() as t:
    for i in range(1, 100000):
        b = i * i
print(f'total time taken: {t()} seconds')
