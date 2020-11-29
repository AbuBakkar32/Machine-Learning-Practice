import time
import threading


def fun1():
    for i in range(15):
        print(threading.current_thread().getName(), i)
        time.sleep(.5)
    print('\n')


def fun2():
    for i in range(5):
        print(threading.current_thread().getName(), i)
        time.sleep(.5)
    print('\n')


th1 = threading.Thread(target=fun1)
th2 = threading.Thread(target=fun2)

th1.start()
th2.start()
th2.join()

print("Total Active Thread=", threading.active_count())

for i in range(2):
    time.sleep(.5)
    print(threading.current_thread().getName(), "Finished")
