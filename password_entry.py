from tkinter import *

class Application(Frame):
    """ GUI Application with buttons. """

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

        if content == "gab":
            message = "Access granted." 
            #print("Rerun script.")
        else:
            message = "Access denied."
            #print("Rerun script.")
        #row, column (first parameter)
        self.text.delete(0.0, END) 
        self.text.insert(0.0, message)
        
root = Tk()
root.title("Password entry")
root.geometry("250x150")
app = Application(root)

root.mainloop()
        
