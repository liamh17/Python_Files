from tkinter import *
import math

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.a_instruction = Label(self, text="Enter A: ")
        self.b_instruction = Label(self, text="Enter B: ")
        self.c_instruction = Label(self, text="Enter C: ")

        self.a_value = Entry(self)
        self.b_value = Entry(self)
        self.c_value = Entry(self)

        self.quad_button = Button(self, text="Calculate",
            command=self.quad_calc, height=2, width=10)

        self.a_instruction.grid(row=0, column=0, sticky=W)
        self. b_instruction.grid(row=0, column=1, sticky=W)
        self.c_instruction.grid(row=0, column=2, sticky=W)

        self.a_value.grid(row=1, column=0, sticky=W)
        self.b_value.grid(row=1, column=1, )
        self.c_value.grid(row=1, column=2)

        self.quad_button.grid(row=4, column=0, sticky=W)

        self.textbox = Text(self, height=3, width=20, wrap=WORD)
        self.textbox.grid(row=6, column=0, sticky=W)

###############################################################################

    def quad_calc(self):
        #-b +- sqr(b^2 - 4ac)
        #--------------------
        #      2a

        a = float(self.a_value.get())
        b = float(self.b_value.get())
        c = float(self.c_value.get())

        b_sq = b * b
        four_ac = 4 * a * c
        d = b_sq - four_ac
        d = math.fabs(d)

        b_neg = b * -1

        if d < 0:
            MESSAGE = "This equation has no real solution."
        if d == 0:
            x = (b_neg + math.sqrt(d)) / 2 * a
            MESSAGE = "One solution: " + x
        else:
            x_one = (b_neg + math.sqrt(d)) / (2 * a)
            x_two = (b_neg - math.sqrt(d)) / (2 * a)

            x_one = str(x_one)
            x_two = str(x_two)

            MESSAGE = "x1 = " + x_one + ", x2 = " + x_two

        self.textbox.delete(0.0, END)
        self.textbox.insert(0.0, MESSAGE)

    def exit_com(self):
        sys.exit()


root = Tk()
root.title("Quadratic Formula Calculator")
root.geometry("400x250")

app = Application(root)
root.mainloop()
