from tkinter import *

root= Tk()

entry_1= Entry(root,width=50)
entry_1.insert(0,"Enter your name")
entry_1.pack()

def btn_handler():
    greet= "Hello "+ entry_1.get()
    label_1= Label(root, text=greet)
    label_1.pack()

button_1= Button(root, text="Enter", command=btn_handler)
button_1.pack()


root.mainloop()