from tkinter import *
from PIL import Image, ImageTk
from datetime import date, datetime
from tkinter import messagebox
from playsound import playsound

window = Tk()
window.config(bg="white")

var = StringVar()
alarm = None
stop = False
def showTime():
    now = datetime.now()
    now1 = now.strftime("%B %d, %Y %H:%M:%S")
    com_alarm = now.strftime("%H:%M")
    if alarm == com_alarm and stop== False:
        print("beep")
        playsound("welcome2.mp3")
    var.set(now1)
    timeshow.after(1000, showTime) 

def set_alarm_fun():
    global alarm, stop
    temp = setEntry.get()
    if ':' in temp:
        alarm = temp
        stop = False
    else:
        messagebox.showerror("Wrong Input","Enter in 00:00 format")

def stop_alarm_fun():
    global stop
    stop = True

frame = Frame(window, bg="white")
frame.grid(row=0, column=0, padx=120, pady=10)

heading = Label(frame, text ="Alarm Clock", font=('Comic Sans MS',20),bg="white")
heading.grid(row=0, column=0, columnspan=2, sticky=EW,)

img = Image.open('alarm.jpg').resize((250,250))
render = ImageTk.PhotoImage(img)
imageLabel = Label(frame, image=render, bg="white")
imageLabel.grid(row=1, column=0, columnspan=2, sticky=EW)

timeshow = Label(frame, font=('Comic Sans MS',18),bg="white", textvariable=var)
timeshow.grid(row=2, column=0,columnspan=2, sticky=EW,pady=5)
showTime()

setLabel = Label(frame, text="Set Alarm", font=('Comic Sans MS',15),bg="white")
setLabel.grid(row=3, column=0,sticky=EW)

setEntry = Entry(frame,  font=('Comic Sans MS',15),bg="white", width=10)
setEntry.grid(row=3, column = 1,padx=3,sticky=EW)

setBtn = Button(frame, text= "Set Alarm", font=('Comic Sans MS',14),bg="#9c88ff", bd=0, command=set_alarm_fun)
setBtn.grid(row = 4, column=0,pady=3,sticky=EW)

stopBtn = Button(frame, text= "Stop Alarm", font=('Comic Sans MS',14),bg="#9c88ff", fg="white",bd=0, command=stop_alarm_fun)
stopBtn.grid(row = 4, column=1,padx=3,sticky=EW)

window.geometry('600x500')
window.title("My Alarm clock")
window.resizable(False, False)
window.mainloop()