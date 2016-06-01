from tkinter import *
import random
import os
import winsound
import time
import sys
import smtplib


class Application(Frame):
    """ GUI y with buttons. """
    global password_entry
    password_entry = random.randint(1, 10)
    password_entry = abs(password_entry)

    password_hint = password_entry + 10
    password_hint = str(password_hint)

    global server, fromaddr, toaddr, user, password
    server = smtplib.SMTP('smtp.gmail.com:587')
    fromaddr = '17lheisler@fatherjudgestudent.com'
    toaddr = '17lheisler@fatherjudgestudent.com'
    user = '17lheisler@fatherjudgestudent.com'
    password = 'yohihey123'

    print('Password hint, ' + password_hint + ' - 5(2)')

    def __init__(self, master):
        """ Init the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry """
        self.instruction = Label(self, text="Enter the password")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=1, column=1, sticky=W)

        self.submit_button = Button(self, text="Submit",
            command=self.reveal, width=5)
        self.submit_button.grid(row=2, column=0, sticky=W)

        self.exit_button = Button(self, text="Exit",
            command=self.quit, width=5)
        self.exit_button.grid(row=2, column=1, sticky=W)

        #self.close_button = Button(self, text = "Close", command = self.quit)
        #self.close_button.grid(row = 2, column = 0, sticky = E)

        self.text = Text(self, width=35, height=5, wrap=WORD)
        self.text.grid(row=3, column=0, columnspan=2, sticky=W)

    def quit(self):
        sys.exit()

    def reveal(self):

        """ Display message based on password typed in """
        content = self.password_entry.get()
        content = int(content)

        if content == password_entry:
            #do something more with this
            message = "Access granted."

            # email text
            granted_msg = 'Access granted via login system.'

            server.starttls()
            server.login(user, password)
            server.sendmail(fromaddr, toaddr, granted_msg)

            # will auto log onto gmail acc
            os.system("start chrome www.gmail.com")
        else:
            # email text
            denied_msg = 'Someone failed to login to your secure system!'

            # print you were denied access to actual text handler
            message = "Access denied."

            server.starttls()
            server.login(user, password)
            server.sendmail(fromaddr, toaddr, denied_msg)

        self.text.delete(0.0, END)
        self.text.insert(0.0, message)


root = Tk()
root.title("Password entry")
root.geometry("250x150")
app = Application(root)

root.mainloop()
