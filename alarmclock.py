from datetime import datetime
from playsound import playsound

def validate_time(alarm_time):
    if len(alarm_time) != 5:
        return "Invalid time format! Please try again..."
    else:
        if int(alarm_time[0:2]) > 24:
            return "Invalid HOUR format! Please try again..."
        elif int(alarm_time[3:4]) > 59:
            return "Invalid MINUTE format! Please try again..."
        else:
            return "ok"


if __name__ == "__main__":
    alarm_time = input("Enter time in 'HH:MM' format (Enter in military time): ")
    
    validate = validate_time(alarm_time.lower())
    if validate != "ok":
        print(validate)
    else:
        print(f"Setting alarm for {alarm_time}...")
        
    alarm_hour = alarm_time[0:2]
    alarm_min = alarm_time[3:5]
    
    while True:
        now = datetime.now()

        current_hour_and_minute = now.strftime("%H:%M")

        if alarm_time == current_hour_and_minute:
            print("Wake Up!")
            while True:
                playsound('/home/mr-robot/alarm/sounds/funny.mp3')
            

    print(validate_time(alarm_time))

                    #break