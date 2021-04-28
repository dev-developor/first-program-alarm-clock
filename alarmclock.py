from datetime import datetime
from playsound import playsound

class Alarm:
    def __init__ (self,alarm_times):
        self.alarm_time_list = []
        self.main()          

    def get_alarms(self):
        #Returns what the list generator makes 
        return self.alarm_time_list
    
    def validate_time(self):
        #Takes input and validates it until it gets to the nd of the list but until then it will 'continue' to loop
        for time_index in self.alarm_time_list:
            #length of input
            if len(time_index) != 5:
                return "Invalid time format! Please try again..."
                continue
            else:
                if int(time_index[0:2]) > 24:
                    #hours
                    return "Invalid HOUR format! Please try again..."
                    continue
                elif int(time_index[3:5]) > 59:
                    #minutes
                    return "Invalid MINUTE format! Please try again..."
                    continue
                else:
                    current_time_index = self.alarm_time_list.index(time_index)
                    if self.alarm_time_list[current_time_index] == self.alarm_time_list[-1]:
                        return "ok"
                    else:
                        continue
                    
#             for item in self.alarm_time_list:
#                 if item == self.alarm_time_list.index[:-1]:
#                     print("end of list")    

    def time_checker(self):
        #See's when to sound the alarm
        while True:
            now = datetime.now()

            current_hour_and_minute = now.strftime("%H:%M")
            for time_index in self.alarm_time_list:
                if time_index == current_hour_and_minute:
                    selected_time = self.alarm_time_list.index(time_index)
                    self.alarm_time_list.pop(selected_time)
                    playsound('/home/mr-robot/alarm/sounds/funny.mp3')
                    
    def main (self):
        #list generator
        seperate_times = alarm_times.split(" ")
        for time_stamp in seperate_times:
            single_alarm_time = time_stamp
            self.alarm_time_list.append(single_alarm_time)
        
        #check to see if user input came back as valid
        if self.validate_time() != "ok":
            print(self.validate_time())
        else:
            #print the alarm times the user inputed
            times = self.get_alarms()
            print("Setting alarm for... ",end='')
            for time in times:
                print("{}, ".format(time),end='')
                
        #runs the functionto see when to set off the alarm
        self.time_checker()
        


if __name__ == '__main__':
    #Starts the program by asking for input then puts the input into the class
    alarm_times = input("Enter a single alarm time in a HH:MM format in military time if you're making a list do 12:32 10:12 20:54 etc...: ")
    alarm_class = Alarm(alarm_times)