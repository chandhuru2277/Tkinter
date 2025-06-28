from tkinter import *

root = Tk()
label_1 = Label(root, text="Hello world").grid(row=0, column=0)
label_2 = Label(root, text="Everything alright Now").grid(row=1, column=2)
label_3 = Label(root, text="Thank you :)").grid(row=3, column=3)

root.mainloop()
