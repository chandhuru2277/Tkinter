from tkinter import *

root= Tk()

def button_1_handlder():
    label_1= Label(root, text="This is my first paragraph",fg="yellow", bg="black")
    label_1.pack()

button_1= Button(root, text="Click me", padx=10, pady=10,fg="white", bg="black",command=button_1_handlder)
button_1.pack()

root.mainloop()