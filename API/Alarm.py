import time
from datetime import datetime
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
                        print(f"Wake Up! Its {alarm.upper()}")
                        webbrowser.open("audio.mp3")
                        time.sleep(25)
                except:
                    pass


if __name__ == '__main__':
    alarm = input("Enter the time of alarm to be set:HH:MM:SS\n")
    hour = alarm[0:2]
    minute = alarm[3:5]
    seconds = alarm[6:8]
    period = alarm[9:11].upper()
    Alarm(hour, minute, seconds, period)
