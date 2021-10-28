from tkinter import*
from tkinter.ttk import*
from time import strftime

root=Tk()
root.title("Digital Clock")
def clock():
    string = strftime('%H:%M:%p')
    Label.config(text=string)
    Label.after(1000, clock)

Label=Label(root, font=("LIBRARY-3-AM-soft", 100), background='black', foreground='green')
Label.pack(anchor='center')
clock()
root.mainloop()
