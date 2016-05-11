# Tip calculator
from tkinter import *

def get_tip():
    total = int(total_entry.get())
    perc = int(perc_entry.get())

    tip = total * (perc / 100)
    tip = str(tip)
    total = str(total)
    perc = str(perc)
    
    MESSAGE = "Total = $" + total + ", Percentage = " + perc + "%, Tip = $" + tip
    tip_text.delete(0.0, END)
    tip_text.insert(0.0, MESSAGE)
    
root = Tk() 
root.title("Tip Calculator v1")
root.geometry("450x200")

frame = Frame(root)
frame.grid()

tip_button = Button(frame, text = "Tip", command = get_tip)
tip_button.grid(row = 4, column = 0, sticky = W)

total_instruct = Label(frame, text = "Enter total: ")
total_instruct.grid(row = 0, column = 0, sticky = W)
perc_instruct = Label(frame, text = "Enter percentage: ")
perc_instruct.grid(row = 0, column = 1, sticky = W)

total_entry = Entry(frame)
total_entry.grid(row = 1, column = 0, sticky = W)
perc_entry = Entry(frame)
perc_entry.grid(row = 1, column = 1, sticky = W)

tip_text = Text(frame, width = 55, height = 5, wrap = WORD)
tip_text.grid(row = 5, column = 0, columnspan = 3, sticky = W) 
