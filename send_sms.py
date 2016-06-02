from tkinter import *
import random
import os
import sys
import smtplib


class Application(Frame):
    global server, fromaddr, toaddr, user, password
    server = smtplib.SMTP('smtp.gmail.com:587')
    fromaddr = '17lheisler@fatherjudgestudent.com'
    toaddr = '2159179402@vtext.com'

    user = '17lheisler@fatherjudgestudent.com'
    password = 'yohihey123'

    def __init__(self, master):
        """ Init the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruct = Label(self, text="Enter phone number/contact: ")
        self.instruct_b = Label(self, text="Enter carrier: ")
        self.instruct_c = Label(self, text="Enter message: ")

        self.instruct.grid(row=0, column=0, sticky=W)
        self.instruct_b.grid(row=1, column=0, sticky=W)
        self.instruct_c.grid(row=2, column=0, sticky=W)

        self.number_entry = Entry(self)
        self.carrier_entry = Entry(self)
        self.message_entry = Entry(self)

        self.number_entry.grid(row=0, column=1, sticky=W)
        self.carrier_entry.grid(row=1, column=1, sticky=W)
        self.message_entry.grid(row=2, column=1, sticky=W)

        self.send_button = Button(self, text="Send", command=self.send,
            width=5)
        self.exit_button = Button(self, text="Exit", command=self.quit,
            width=5)

        self.send_button.grid(row=6, column=0, sticky=W)
        self.exit_button.grid(row=7, column=0, sticky=W)

    def quit(self):
        sys.exit()

    def send(self):
        number = str(self.number_entry.get())
        carrier = self.carrier_entry.get()
        msg = self.message_entry.get()

        user = '17lheisler@fatherjudgestudent.com'
        password = 'yohihey123'

        global from_addr, server
        from_addr = '17lheisler@fatherjudgestudent.com'

        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.login(user, password)

        if number == 'gab':
            carrier = 'verizon'
            number = '2156806156'

        if number == 'me':
            carrier = 'verizon'
            number = '2159179402'

        if number == 'mom':
            carrier = 'verizon'
            number = '2154856323'

        if number == 'dad':
            carrier = 'verizon'
            number = '2154856613'

        if number == 'gavin':
            carrier = 'verizon'
            number = '2159901360'

        if number == 'mark':
            carrier = 'tmobile'
            number = '2156998288'

        if number == 'angelo':
            carrier = 'verizon'
            number = '2155821337'

        if carrier == 'verizon':
            to_addr = '' + number + '@vtext.com'
            to__addr = str(to_addr)

            server.sendmail(from_addr, to__addr, msg)

        elif carrier == 'tmobile':
            to_addr = '' + number + '@tmomail.com'
            to__addr = str(to_addr)
            server.sendmail(from_addr, to__addr, msg)

        elif carrier == 'att':
            to_addr = '' + number + '@txt.att.net'
            to__addr = str(to_addr)
            server.sendmail(from_addr, to__addr, msg)

        elif carrier == 'sprint':
            to_addr = '' + number + '@messaging.sprintpcs.com'
            to__addr = str(to_addr)
            server.sendmail(from_addr, to__addr, msg)

        elif carrier == 'cricket':
            to_addr = '' + number + '@sms.mycricket.com'
            to__addr = str(to_addr)
            server.sendmail(from_addr, to__addr, msg)

root = Tk()
root.title("Password entry")
root.geometry("350x150")
app = Application(root)

root.mainloop()
