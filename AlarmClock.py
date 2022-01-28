import os
import datetime
from playsound import playsound

os. system('clear')
alarm_Hour = int(input("Set hour of your alarm - "))
alarm_Min = int(input("Set minute of your alarm - "))
meridiem = input("am /pm ? - ")
os. system('clear')
print("Waiting for alarm : ",alarm_Hour,alarm_Min,meridiem)
if (meridiem == "pm"):
        alarm_Hour = alarm_Hour + 12
while True:
    if(alarm_Hour == datetime.datetime.now().hour and alarm_Min == datetime.datetime.now().minute) :
        print(" --- It's time to wake up --- ")
        playsound('rooster-crowing.mp3')
        break
