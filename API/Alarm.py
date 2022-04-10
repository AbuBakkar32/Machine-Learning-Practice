import time
from datetime import datetime

from playsound import playsound
import webbrowser

class Alarm:
    def __init__(self, hour, minute, second, period):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.period = period
        self.set_alarm()

    def set_alarm(self):
        print("Setting up alarm..")
        while True:
            now = datetime.now()
            current_hour = now.strftime("%I")
            current_minute = now.strftime("%M")
            current_seconds = now.strftime("%S")
            current_period = now.strftime("%p")
            if (self.period == current_period and self.hour == current_hour \
                    and self.minute == current_minute \
                    and self.second == current_seconds):
                try:
                    while True:
                        print("Alarm ringing..")
                        print(f"Wake Up! Its {alarm_time.upper()}")
                        webbrowser.open("audio.mp3")
                        time.sleep(28)
                except:
                    pass


if __name__ == '__main__':
    alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
    alarm_hour = alarm_time[0:2]
    alarm_minute = alarm_time[3:5]
    alarm_seconds = alarm_time[6:8]
    alarm_period = alarm_time[9:11].upper()
    Alarm(alarm_hour, alarm_minute, alarm_seconds, alarm_period)

