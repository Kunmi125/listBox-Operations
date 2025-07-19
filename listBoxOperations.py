from tkinter import *


window = Tk()
window.geometry("800x800")
window.configure(background = "black")

frame1 = Frame(window, bg = "olive", padx = 10, pady = 10)
frame1.pack()

title = Label(frame1, text = "Listbox Operations", font = ("Bold", 12))
title.pack(padx = 3, pady = 3)







window.mainloop()