from datetime import datetime
from playsound import playsound

class Alarm:
    def __init__ (self,alarm_times):
        self.alarm_time_list = []
        seperate_times = alarm_times.split(",")
        for time_stamp in seperate_times:
            single_alarm_time = time_stamp
            self.alarm_time_list.append(single_alarm_time)
    
    def get_alarms(self):
        return self.alarm_time_list
    
    def validate_time(self):
        for time_index in self.alarm_time_list:
            if len(time_index) != 5:
                return "Invalid time format! Please try again..."
            else:
                if int(time_index[0:2]) > 24:
                    return "Invalid HOUR format! Please try again..."
                elif int(time_index[3:4]) > 59:
                    return "Invalid MINUTE format! Please try again..."
                else:
                    return "ok"

    def time_checker(self):
        while True:
            now = datetime.now()

            current_hour_and_minute = now.strftime("%H:%M")
            for time_index in self.alarm_time_list:
                if time_index == current_hour_and_minute:
                    print("alarm sound")
                    x = self.alarm_time_list.index(time_index)
                    self.alarm_time_list.pop(x)
                    playsound('/home/mr-robot/alarm/sounds/funny.mp3')


if __name__ == '__main__':
    alarm_times = input("Enter a list of times your your alarm should go off in HH:MM format. ")

    a = Alarm(alarm_times)


    if a.validate_time() != "ok":
        print(a.validate_time())
    else:
        times = a.get_alarms()
        print("Setting alarm for...",end='')
        for time in times:
            print("{} ".format(time),end='')
        
    a.time_checker()