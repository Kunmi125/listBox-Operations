from tkinter import *


window = Tk()
window.geometry("800x800")
window.configure(background = "black")
window.columnconfigure(0, weight = 1)
window.columnconfigure(1, weight = 1)
window.rowconfigure(0, weight = 1)


frame1 = Frame(window, text = "Listbox Operations", bg = "olive", padx = 10, pady = 10)
frame1.grid(row = 0, column = 0, sticky = "nsew") #sticky means stick to the corners
frame1.columnconfigure(0, weight = 1)
frame1.rowconfigure(0, weight = 1)

items = Scrollbar(frame1, orient = VERTICAL)
foods = ["Pizza", "Burger", "Fries", "Chips", "Sandwhich", "Ice Cream"]
food_stuff = Listbox(frame1, width = 30, height = 30, yscrollcommand = items.set)
food_stuff.grid(row = 0, column = 0)

items.config(command = food_stuff.yview)
items.grid(row = 0, column = 1)

item_entry = Entry(frame1)
item_entry.grid(row = 1, column = 0)

for food in foods:
    food_stuff.insert(END , food)


def add_item():
    new_item = item_entry.get()
    if new_item:
        food_stuff.insert(END, new_item)
        item_entry.delete(0, END)
    



window.mainloop()
