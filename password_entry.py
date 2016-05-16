from tkinter import *
import random
import os
import warnings
import winsound
import time
import sys
from subprocess import *

class Application(Frame):
    """ GUI Application with buttons. """
    global password
    password = random.randint(1, 10)
    password = abs(password)

    password_hint = password + 10
    password_hint = str(password_hint)

    print('Password hint, ' + password_hint + ' - 9 - 1') 
    
    def __init__(self, master):
        """ Init the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry """
        self.instruction = Label(self, text = "Enter the password")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)

        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)

        self.submit_button = Button(self, text = "Submit", command = self.reveal)
        self.submit_button.grid(row = 2, column = 0, sticky = W)

        #self.close_button = Button(self, text = "Close", command = self.quit)
        #self.close_button.grid(row = 2, column = 0, sticky = E)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)

    def quit(self):
        self.destroy() 
        
    def reveal(self):
        """ Display message based on password typed in """
        content = self.password.get()
        content = int(content)

        if content == password:
            message = "Access granted."

            os.system('start chrome liamh17.github.io')
            
        else:
            message = "Access denied."

            os.system("start chrome liamh17.github.io")
            
            winsound.Beep(600, 800)
            time.sleep(.2)
            winsound.Beep(600, 800)
            time.sleep(.2)
            winsound.Beep(600, 800)

            #espeak.synth('Acces denied, try again')
            #os.system('shutdown -r -t 30 -c "Wrong password. Goodbye.."')
            
        #row, column (first parameter)
        self.text.delete(0.0, END) 
        self.text.insert(0.0, message)
        
root = Tk()
root.title("Password entry")
root.geometry("250x150")
app = Application(root)

root.mainloop()
        
