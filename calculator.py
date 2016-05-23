from tkinter import *
import math

class Application(Frame):
    """ GUI Application with buttons. """

    def __init__(self, master):
        """ Init the Frame """  
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry """
        self.instruction = Label(self, text = "Enter your first value:")
        self.instruction.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.instruction = Label(self, text = "Enter your second value:")
        self.instruction.grid(row = 0, column = 1, columnspan = 2, sticky = W)
        self.instruction = Label(self, text = "Enter your third value:")
        self.instruction.grid(row = 0, column = 2, columnspan = 2, sticky = W)

        self.valueA = Entry(self) 
        self.valueA.grid(row = 1, column = 0, sticky = W)
        self.valueB = Entry(self) 
        self.valueB.grid(row = 1, column = 1 , sticky = W)
        self.valueC = Entry(self)
        self.valueC.grid(row = 1, column = 2, sticky = W)       

        self.add_button = Button(self, text = "(+) Add", command = self.add)
        self.add_button.grid(row = 2, column = 0, sticky = W)
        self.subtract_button = Button(self, text = "(-) Subtract", command = self.subtract)
        self.subtract_button.grid(row = 3, column = 0, sticky = W)
        self.multiply_button = Button(self, text = "(*) Multiply", command = self.multiply)
        self.multiply_button.grid(row = 4, column = 0, sticky = W)
        self.divide_button = Button(self, text = "(÷) Divide", command = self.divide)
        self.divide_button.grid(row = 5, column = 0, sticky = W)

        self.rect_area_button = Button(self, text = "Rect Area", command = self.rectangle_area)
        self.rect_area_button.grid(row = 2, column = 1, sticky = W)
        self.rect_perim_button = Button(self, text = "Rect Perim", command = self.rectangle_perim)
        self.rect_perim_button.grid(row = 3, column = 1, sticky = W)

        self.circle_circum_button = Button(self, text = "Circle Circum", command = self.circle_circum)
        self.circle_circum_button.grid(row = 4, column = 1, sticky = W)
        self.circle_area_button = Button(self, text = "Circle Area", command = self.circle_area)
        self.circle_area_button.grid(row = 5, column = 1, sticky = W)
        
        self.tri_area_button = Button(self, text = "Tri Area", command = self.tri_area) 
        self.tri_area_button.grid(row = 2, column = 2, sticky = W)
        self.tri_perim_button = Button(self, text = "Trip Perim", command = self.tri_perim)
        self.tri_perim_button.grid(row = 3, column = 2, sticky = W)

        self.pythag_c_button = Button(self, text = "Pythag sC", command = self.pythag_c)
        self.pythag_c_button.grid(row = 4, column = 2, sticky = W)
        self.pythag_a_button = Button(self, text = "Pythag sA", command = self.pythag_a)
        self.pythag_a_button.grid(row = 5, column = 2, sticky = W)
        self.pythag_b_button = Button(self, text = "Pythag sB", command = self.pythag_b)
        self.pythag_b_button.grid(row = 2, column = 4, sticky = W)
    
        #self.close_button = Button(self, text = "Close", command = self.quit)
        #self.close_button.grid(row = 2, column = 0, sticky = E)

        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 7, column = 0, columnspan = 2, sticky = W)

    def quit(self):
        self.destroy()
        
    def add(self):
        """ Display message based on password typed in """
        addend1 = float(self.valueA.get())
        addend2 = float(self.valueB.get())
        
        sum = addend1 + addend2

        sum = str(sum)
        addend1 = str(addend1)
        addend2 = str(addend2) 

        message = "" + addend1 + " + " + addend2 + " = " + sum
        self.text.delete(0.0, END) 
        self.text.insert(0.0, message)

    def subtract(self):
        minuend = float(self.valueA.get())
        subtrahend = float(self.valueB.get())
        difference = minuend - subtrahend

        difference = str(difference)
        minuend = str(minuend)
        subtrahend = str(subtrahend) 

        message = "" + minuend + " - " + subtrahend + " = " + difference
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def multiply(self):
        factor1 = float(self.valueA.get())
        factor2 = float(self.valueB.get())
        product = factor1 * factor2

        product = str(product)
        factor1 = str(factor1)
        factor2 = str(factor2)

        message = "" + factor1 + " * " + factor2 + " = " + product
        self.text.delete(0.0, END)
        self.text.insert(0.0, message) 

    def divide(self):
        dividend = float(self.valueA.get())
        divisor = float(self.valueB.get())
        quotient = dividend / divisor

        quotient = str(quotient)
        dividend = str(dividend)
        divisor = str(divisor) 

        message = "" + dividend + " ÷ " + divisor + " = " + quotient
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def rectangle_area(self):
        # l * w
        length = float(self.valueA.get())
        width = float(self.valueB.get())
        area = length * width

        length = str(length)
        width = str(width)
        area = str(area)

        message = "" + length + " * " + width + " =  " + area
        self.text.delete(0.0, END)
        self.text.insert(0.0, message) 

    def rectangle_perim(self):
        # 2(l) + 2(w)
        length = float(self.valueA.get())
        width = float(self.valueB.get())
        perim = (2 * length) + (2 * width)

        length = str(length)
        width = str(width)
        perim = str(perim)

        message = "2(" + length + ") + 2(" + width + ") = " + perim
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def circle_circum(self):
        # 2 PI r
        radius = float(self.valueA.get())
        circum = (2 * radius) * 3.1415

        circum = str(circum)
        radius = str(radius)

        message = "2 * PI * " + radius + " = " + circum
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def circle_area(self):
        # PI * r^2
        radius = float(self.valueA.get())
        area = (radius * radius) * 3.1415

        area = str(area)
        radius = str(radius)

        message = "PI * " + radius + "^2 = " + area
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def tri_area(self):
        #1/2B * H
        base = float(self.valueA.get())
        leg1 = float(self.valueB.get())
        #leg2 = float(self.valueC.get())
        area = (base / 2) * leg1

        area = str(area)
        base = str(base)
        height = str(leg1)

        message = "" + base + "/ 2 * " + height + " = " + area
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def tri_perim(self):
        base = float(self.valueB.get())
        leg1 = float(self.valueA.get())
        leg2 = float(self.valueC.get())
        perim = base + leg1 + leg2

        perim = str(perim)
        base = str(base)
        leg1 = str(leg1)
        leg2 = str(leg2)
        
        message = "" + base + " + " + leg1 + " + " + leg2 + " = " + perim

        if leg2 is None:
            message = "Please enter value for 2nd leg." 
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def pythag_c(self):
        #a^2 + b^2 = c^2
        #solve for c^2
        a = float(self.valueA.get())
        b = float(self.valueB.get())

        a_sq = a * a
        b_sq = b * b

        c_sq = a_sq + b_sq
        c = math.sqrt(c_sq)

        a = str(a)
        a_sq = str(a_sq)
        b = str(b)
        b_sq = str(b_sq)
        c = str(c)
        c_sq = str(c_sq) 

        message = "" + a_sq + " + " + b_sq + " = " + c_sq + ", c = " + c
        self.text.delete(0.0, END)
        self.text.insert(0.0, message) 

    def pythag_a(self):
        #a^2 + b^2 = c^2
        #solve for a
        c = float(self.valueA.get())
        b = float(self.valueB.get())

        c_sq = c * c
        b_sq = b * b

        a_sq = c_sq - b_sq
        a = math.sqrt(a_sq)

        a = str(a)
        a_sq = str(a_sq)
        b = str(b)
        b_sq = str(b_sq)
        c = str(c)
        c_sq = str(c_sq) 

        message = "" + c_sq + " - " + b_sq + " = " + a_sq + ", c = " + a
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)

    def pythag_b(self):
        #a^2 + b^2 = c^
        #solve for b
        c = float(self.valueA.get())
        a = float(self.valueB.get())

        a_sq = a * a
        c_sq = c * c

        b_sq = c_sq - a_sq
        b = math.sqrt(b_sq)

        a = str(a)
        a_sq = str(a_sq)
        b = str(b)
        b_sq = str(b_sq)
        c = str(c)
        c_sq = str(c_sq) 

        message = "" + c_sq + " - " + a_sq + " = " + b_sq + ", c = " + b
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        
root = Tk()
root.title("Calculator entry")
root.geometry("500x250")
app = Application(root)

root.mainloop()
        
