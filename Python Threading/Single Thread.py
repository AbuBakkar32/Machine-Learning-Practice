import threading


def func():
    print("Starting of thread :", threading.current_thread().getName())


def func1():
    print("Starting of thread :", threading.current_thread().getName())


my_thread = threading.Thread(target=func)
my_thread.start()

my_thread1 = threading.Thread(target=func1)
my_thread1.start()
