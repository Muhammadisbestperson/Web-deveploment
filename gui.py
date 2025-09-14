from tkinter import *
from datetime import date


root =Tk()
root.title("Getting started with widgets")
root.geometry('400x300')

lbl=Label(text="Hey There!" , fg='white', bg="#CC57C6", height=1,width=300)
name_lbl = Label(text="Full name",bg="#3678D5")
name_entry=Entry()

def display():
    name =name_entry.get()
    global message
    message="Welome to the Application! \nToday's date is:"
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())

btn=Button(text="Begin",command=display, height=1, bg= "#1261A0")

text_box=Text(height=3)
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()