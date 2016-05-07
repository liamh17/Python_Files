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
        self.instruction = Label(self, text = "Enter your first value")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.instruction = Label(self, text = "Enter your second value")
        self.instruction.grid(row = 0, column = 1, columnspan = 2, sticky = W)

        self.valueA = Entry(self) 
        self.valueA.grid(row = 1, column = 0, sticky = W)
        self.valueB = Entry(self) 
        self.valueB.grid(row = 1, column = 1 , sticky = W)

        self.add_button = Button(self, text = "(+) Add", command = self.add)
        self.add_button.grid(row = 2, column = 0, sticky = W)

        self.subtract_button = Button(self, text = "(-) Subtract", command = self.subtract)
        self.subtract_button.grid(row = 3, column = 0, sticky = W)

        self.multiply_button = Button(self, text = "(*) Multiply", command = self.multiply)
        self.multiply_button.grid(row = 4, column = 0, sticky = W)

        self.divide_button = Button(self, text = "(÷) Divide", command = self.divide)
        self.divide_button.grid(row = 5, column = 0, sticky = W)

        #self.close_button = Button(self, text = "Close", command = self.quit)
        #self.close_button.grid(row = 2, column = 0, sticky = E)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 7, column = 0, columnspan = 2, sticky = W)

    def quit(self):
        self.destroy()
        
    def add(self):
        """ Display message based on password typed in """
        addend1 = int(self.valueA.get())
        addend2 = int(self.valueB.get())
        
        sum = addend1 + addend2

        sum = str(sum)
        addend1 = str(addend1)
        addend2 = str(addend2) 

        message = "" + addend1 + " + " + addend2 + " = " + sum
        self.text.delete(0.0, END) 
        self.text.insert(0.0, message)

    def subtract(self):
        minuend = int(self.valueA.get())
        subtrahend = int(self.valueB.get())
        difference = minuend - subtrahend

        difference = str(difference)
        minuend = str(minuend)
        subtrahend = str(subtrahend) 

        message = "" + minuend + " - " + subtrahend + " = " + difference
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def multiply(self):
        factor1 = int(self.valueA.get())
        factor2 = int(self.valueB.get())
        product = factor1 * factor2

        product = str(product)
        factor1 = str(factor1)
        factor2 = str(factor2)

        message = "" + factor1 + " * " + factor2 + " = " + product
        self.text.delete(0.0, END)
        self.text.insert(0.0, message) 

    def divide(self):
        dividend = int(self.valueA.get())
        divisor = int(self.valueB.get())
        quotient = dividend / divisor

        quotient = str(quotient)
        dividend = str(dividend)
        divisor = str(divisor) 

        message = "" + dividend + " ÷ " + divisor + " = " + quotient
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        
root = Tk()
root.title("Calculator entry")
root.geometry("400x250")
app = Application(root)

root.mainloop()
        
