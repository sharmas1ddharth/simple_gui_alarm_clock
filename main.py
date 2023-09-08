from tkinter import *
from tkinter import messagebox
from alarm_clock import AlarmClock
from playsound import playsound

def set_alarm():
    alarm_time = f"{hour.get()}:{minutes.get()}"
    while True:
        response = AlarmClock(alarm_time).check_if_alarm_time()
        if response:
            playsound('alarm.mp3')
            messagebox.showinfo("Alarm", "Time to wake up!")
            break

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x400")
time_format = Label(clock, text="Enter time in 24 hour format", fg="black")
time_format.place(x=60, y=120)

add_time = Label(clock, text="Hour  Min")
add_time.place(x=140)

set_your_alarm = Label(clock, text="When to wake you up", fg="white", bg="black")
set_your_alarm.place(x=0, y=29)

hour, minutes, sec = StringVar(), StringVar(), StringVar()

hour_time = Entry(clock, textvariable=hour, bg='pink')
hour_time.place(x=140, y=30)
minutes_time = Entry(clock, textvariable=minutes, bg='pink')
minutes_time.place(x=180, y=30)

submit = Button(clock, text="Set Alarm", fg='red', command=set_alarm)
submit.place(x=110, y=70)

clock.mainloop()
