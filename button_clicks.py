# OOP GUI
from tkinter import *

class Application(Frame):
    """ A GUI application with three buttons."""

    def __init__(self, master):
        """ Initialize the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.button_clicks = 0 # Count number of button clicks 
        self.create_widgets()

    def create_widgets(self):
        """ Create button displaying number of clicks """
        self.button = Button(self)
        self.button["text"] = "Total Clicks: 0"
        self.button["command"] = self.update_count
        self.button.grid() 

    def update_count(self):
        """ Increate the click count and display new total """
        self.button_clicks += 1
        self.button["text"] = "Total clicks: " + str(self.button_clicks)

        if self.button_clicks > 5:
            print('Too many clicks!')
            self.destroy()
            self.inconify()
root = Tk()
root.title("Button testing")
root.geometry("200x85")

app = Application(root)

root.mainloop()

