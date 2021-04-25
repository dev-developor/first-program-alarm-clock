from datetime import datetime
from playsound import playsound

class Alarm:
    def __init__ (self, alarm_time):
        self.alarm_time = alarm_time

    def validate_time(self):
        alarm_hour = self.alarm_time[0:2]
        alarm_min = self.alarm_time[3:5]

        if len(self.alarm_time) != 5:
            return "Invalid time format! Please try again..."
        else:
            if int(self.alarm_time[0:2]) > 24:
                return "Invalid HOUR format! Please try again..."
            elif int(self.alarm_time[3:4]) > 59:
                return "Invalid MINUTE format! Please try again..."
            else:
                return "ok"

    def time_checker(self):
        while True:
            now = datetime.now()

            current_hour_and_minute = now.strftime("%H:%M")

            if self.alarm_time == current_hour_and_minute:
                print("Wake Up!")
                while True:
                    playsound('/home/mr-robot/alarm/sounds/funny.mp3')

    def get_time (self):
        return self.alarm_time

if __name__ == '__main__':
    alarm_time = input("")

    a = Alarm(alarm_time)

    if a.validate_time() != "ok":
        print(a.validate_time())
    else:
        print("Setting alarm for {}...".format(a.get_time()))

    a.time_checker()