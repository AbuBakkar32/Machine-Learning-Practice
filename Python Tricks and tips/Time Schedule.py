import sched
import time
import webbrowser

url = 'www.facebook.com/abubakkar32'


def my_time():
    s.enter(5, 1, my_time, argument=())
    webbrowser.open_new(url)


s = sched.scheduler(time.time, time.sleep)
s.enter(5, 1, my_time(), argument=())
s.run()