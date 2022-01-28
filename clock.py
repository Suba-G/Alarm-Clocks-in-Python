from tkinter import *
import datetime
import os
import time
from tkinter import messagebox
from playsound import playsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        os.system('clear')
        print("The Set Date is:",date)
        print(now)
        
        if now == set_alarm_timer:
            os.system('clear')
            print(" --- It's Time to Wake up! --- ")
            playsound('rooster-crowing.mp3')
            clock.destroy()
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.configure(bg='cyan')
clock.title("Alarm Clock")
clock.geometry("400x200")
time_format=Label(clock, text= "Enter time in 24 hour format!", fg="blue",bg="gray",font="Arial").place(x=80,y=145)
addTime = Label(clock,text = "Hour    Min     Sec",font=60,bg='cyan').place(x = 100,y=35)
setYourAlarm = Label(clock,text = " Set Alarm Time in format 00:00:00",fg="red",bg='gray',relief = "solid",font=("Helevetica",8,"bold")).place(x=2, y=10)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 10).place(x=80,y=55)
minTime= Entry(clock,textvariable = min,bg = "pink",width = 15).place(x=140,y=55)
secTime = Entry(clock,textvariable = sec,bg = "pink",width = 15).place(x=200,y=55)

#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",bg="gray",width = 10,font=("Helevetica",10,"bold"),command = actual_time).place(x =125,y=95)



clock.mainloop()
#Execution of the window.