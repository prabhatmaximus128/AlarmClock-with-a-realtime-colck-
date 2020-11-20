from tkinter import *
import datetime
import time
import winsound
from time import strftime

def timecur(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, timecur)
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The Set Date is:",date)
        print(now)
        if now == set_alarm_timer:
            print("Wake up")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def Current_Time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm clock")
clock.iconbitmap(r"Graphicloads-Flat-Finance-Global.ico")
clock.geometry("400x400")
time_format=Label(clock, text= "Input Time in 24 Hour Format", fg="red",font=('calibri', 20, 'bold')).place(x=30,y=270)
HourLBL = Label(clock,text = "HOUR",font=('calibri', 20, 'bold')).place(x = 40,y=100)
MinuteLBL = Label(clock,text = "MINUTE",font=('calibri', 20, 'bold')).place(x = 150, y=100)
SecondLBL = Label(clock,text = "SECOND",font=('calibri', 20, 'bold')).place(x = 280, y=100)

#Variables To Set The Alarm
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time Using Set Alarm Variable From Above To Set The Alarm
hourTime= Entry(clock,textvariable = hour,bg = "Green",width = 15).place(x=30,y=150)
minTime= Entry(clock,textvariable = min,bg = "Green",width = 15).place(x=150,y=150)
secTime = Entry(clock,textvariable = sec,bg = "Green",width = 15).place(x=280,y=150)

#Using Users Input
submit = Button(clock,text = "Set",bg="red",fg="Yellow",width = 10,command = Current_Time).place(x =160,y=210)

lbl = Label(clock, font = ('calibri', 40, 'bold'),foreground = 'red') 
  
# Placing clock at the centre 
# of the tkinter window 
lbl.place(x=60, y=10)
timecur() 

clock.mainloop()

