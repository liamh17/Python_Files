'''
 This is a simple password-entry GUI that detects whether
 or not a correct password(random number from 1-10) is entered.

 First, a password is entered into the Entry box, then is handled
 by the program, comparing it to the random passwored genereated
 by the random.randint function..

 Second, once the submit button is clicked, a the text entered
 is then comopared to the one generated. It then runs through a
 simple series of if statements:

 CONDITIONS:
     if correct password is entered:
        1) print to text box in GUI that correct pass was entered
        2) send email via gmail to 2159179402@vtext.com,
            mentioning the access was granted
        3) and open chrome gmail window/tab, thus "giving acccess"

     elif incorrect password is entered:
        1) print to text box in GUI that incorrect pass was entered
        2) send email via gmail to 2159179402@vtext.com,
            mentioning the failed password attempt.
        3) DO NOT OPEN CHROME WINDOW

'''

from tkinter import *
import random
import os
import sys
import smtplib


class Application(Frame):
    global password_entry
    password_entry = random.randint(1, 10)
    password_entry = abs(password_entry)

    password_hint = password_entry + 10
    password_hint = str(password_hint)

    global server, fromaddr, toaddr, user, password
    server = smtplib.SMTP('smtp.gmail.com:587')
    fromaddr = '17lheisler@fatherjudgestudent.com'
    toaddr = '2159179402@vtext.com'

    user = '17lheisler@fatherjudgestudent.com'
    password = 'REDACTED'

    #print('Password hint, ' + password_hint + ' - 5(2)')

    def __init__(self, master):
        """ Init the Frame """
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create button, text, and entry """
        self.instruction = Label(self, text="Enter the password ")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=0, column=1, sticky=W)

        self.submit_button = Button(self, text="Submit",
            command=self.reveal, width=10)
        self.submit_button.grid(row=2, column=0, sticky=W)

        self.exit_button = Button(self, text="Exit",
            command=self.quit, width=10)
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
        #content = int(content)

        if content == 'admin':
            #do something more with this
            message = "Access granted."

            # email text
            granted_msg = 'Access granted via login system.'

            server.starttls()
            server.login(user, password)
            server.sendmail(fromaddr, toaddr, granted_msg)

            # will auto log onto gmail acc
            #os.system("start chrome www.gmail.com")
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
root.geometry("350x150")
app = Application(root)

root.mainloop()
