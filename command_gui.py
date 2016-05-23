from tkinter import *
import random
import os
import warnings
import winsound
import time
import sys
from subprocess import *


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text="Choose an option.")
        self.instruction.grid(row=0, column=2,
        columnspan=2, sticky=W)

        self.exit_button = Button(self, text="exit",
            command=self.exit_command, height=2, width=10)
        self.exit_button.grid(row=1, column=0, sticky=W)

        self.ipconfig_button = Button(self, text="ipconfig",
            command=self.ipconfig, height=2, width=10)
        self.ipconfig_button.grid(row=2, column=0, sticky=W)

        self.powershell_button = Button(self, text="powershell",
            command=self.powershell, height=2, width=10)
        self.powershell_button.grid(row=3, column=0, sticky=W)

        self.logoff_button = Button(self, text="logoff",
            command=self.logoff, height=2, width=10)
        self.logoff_button.grid(row=4, column=0, sticky=W)

        self.shutdown_button = Button(self, text="shutdown",
            command=self.shutdown, height=2, width=10)
        self.shutdown_button.grid(row=5, column=0, sticky=W)

        self.shutdown_abort_button = Button(self, text="abort s.d.",
            command=self.shutdown_abort, height=2, width=10)
        self.shutdown_abort_button.grid(row=1, column=1, sticky=W)

        self.restart_button = Button(self, text="restart",
            command=self.restart, height=2, width=10)
        self.restart_button.grid(row=2, column=1, sticky=W)

        self.chrome_button = Button(self, text="chrome",
            command=self.chrome, height=2, width=10)
        self.chrome_button.grid(row=3, column=1, sticky=W)

        self.netflix_button = Button(self, text="Netflix",
            command=self.netflix, height=2, width=10)
        self.netflix_button.grid(row=4, column=1, sticky=W)

        self.cbs_button = Button(self, text="CBS",
            command=self.CBS, height=2, width=10)
        self.cbs_button.grid(row=5, column=1, sticky=W)

        self.firewall_enable_button = Button(self, text="firewall ON",
            command=self.firewall_enable, height=2, width=10)
        self.firewall_enable_button.grid(row=1, column=2, sticky=W)

        self.firewall_disable_button = Button(self, text="firewall OFF",
            command=self.firewall_disable, height=2, width=10)
        self.firewall_disable_button.grid(row=2, column=2, sticky=W)

        self.flushdns_button = Button(self, text="flush DNS",
            command=self.flushdns, height=2, width=10)
        self.flushdns_button.grid(row=3, column=2, sticky=W)

        self.test_connection_button = Button(self, text="ping test",
            command=self.test_connection, height=2, width=10)
        self.test_connection_button.grid(row=4, column=2, sticky=W)

        self.regedit_button = Button(self, text="regedit",
            command=self.firewall_disable, height=2, width=10)
        self.regedit_button.grid(row=5, column=2, sticky=W)

    def exit_command(self):
        #exits application
        exit()

    def ipconfig(self):
        #gets configuration of ip and everything else
        os.system("ipconfig /all")

    def powershell(self):
        #opens powershell
        os.system("start powershell")

    def logoff(self):
        #logs user off after 3 seconds
        os.system("shutdown -l -f")

    def shutdown(self):
        #shuts computer down after 3 seconds
        os.system("shutdown -s -f -t 3")

    def shutdown_abort(self):
        #aborts shutdown
        os.system("shutdown -a")

    def restart(self):
        #restarts comptuer after 3 seconds
        os.system("shutdown -r -f -t 3")

    def chrome(self):
        #starts chrome browser, WEBSITES COULD BE ADDED
        os.system("start chrome")

    def netflix(self):
        #starts chrome browser, WEBSITES COULD BE ADDED
        os.system("start chrome www.netflix.com")

    def CBS(self):
        #starts chrome browser, WEBSITES COULD BE ADDED
        os.system("start chrome www.cbs.com")

    def firewall_enable(self):
        #enables fireawll
        os.system("netsh advfirewall set allprofiles state on")

    def firewall_disable(self):
        #disables firewall
        os.system("netsh advfirewall set allprofiles state off")

    def flushdns(self):
        #flushes DNS
        os.system("ipconfig /flushdns")

    def test_connection(self):
        #pings comptuer, IP CAN BE CHANGED
        os.system("ping 10.0.0.180")

    def regedit(self):
        #opens registry editor
        os.system("regedit")

root = Tk()
root.title("Command GUI")
root.geometry("450x240")

app = Application(root)
root.mainloop()
