# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 17:16:09 2021

@author: sairam
"""

import tkinter
import datetime
import time
import winsound
def reminder(set_reminder_timer,set_reason):
    while(True):
        time.sleep(1) #delay execution for 1 second
        current_time=datetime.datetime.now() #gives current date and time
        now=current_time.strftime("%H:%M:%S")
        date=current_time.strftime("%d/%m/%y")
        print("The Set Date is:",date)
        print(now)
        if(now==set_reminder_timer):
            timeup(set_reminder_timer,set_reason)
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break
            

def actual_time():
    set_reminder_timer=f"{hour.get()}:{min.get()}:{sec.get()}"
    set_reason=appointment.get()
    reminder(set_reminder_timer,set_reason)

def timeup(set_reminder_timer,set_reason):
    rem=tkinter.Tk()
    rem.title("Reminder")
    rem.geometry("400x100")
    res=tkinter.Label(rem,text="It's time",fg="red",font="Arial").place(x=110,y=10)
    res=tkinter.Label(rem,text=set_reason,fg="red",font="Arial").place(x=110,y=30)
    res=tkinter.Label(rem,text=set_reminder_timer,fg="red",font="Arial").place(x=110,y=50)
    
    
clock=tkinter.Tk()
clock.title("Reminder")
clock.geometry("400x200")
time_format=tkinter.Label(clock,text="Enter time in 24 hour format!",fg="red",bg="black",font="Arial").place(x=60,y=120)
addTime=tkinter.Label(clock,text="Hour Min Sec",font=60).place(x=110)
setYourAlarm=tkinter.Label(clock,text="Time",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(x=5,y=29)
reason=tkinter.Label(clock,text="Appointment",fg="blue",relief="solid",font=("Helevetica",7,"bold")).place(x=5,y=59)

hour=tkinter.StringVar()
min=tkinter.StringVar()
sec=tkinter.StringVar()
appointment=tkinter.StringVar()
hourTime=tkinter.Entry(clock,textvariable=hour,bg="pink",width=8).place(x=110,y=30)
minTime=tkinter.Entry(clock,textvariable=min,bg="pink",width=8).place(x=150,y=30)
secTime=tkinter.Entry(clock,textvariable=sec,bg="pink",width=8).place(x=190,y=30)
appt=tkinter.Entry(clock,textvariable=appointment,bg="pink",width=45).place(x=110,y=60)

submit=tkinter.Button(clock,text="Set alarm",fg="red",width=10,command=actual_time).place(x=110,y=90)
clock.mainloop()


          
            
        
