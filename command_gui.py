'''
     Creator: Liam Heisler

     This is a simple GUI that uses the "os.system"
     command from python, allowing you to execute
     terminal commands through the script.

     There are specific buttons that call specific
     commands, and they are neatly laid out in a simple
     tkinter pythin GUI.

'''

from tkinter import *
import os
import smtplib
import time


class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.instruction = Label(self, text="Choose an option.")
        self.instruction.grid(row=0, column=2,
        columnspan=2, sticky=W)

###############################################################################

        self.exit_button = Button(self, text="exit",
            command=self.exit_command, height=2, width=12)
        self.exit_button.grid(row=1, column=0, sticky=W)

        self.ipconfig_button = Button(self, text="ipconfig",
            command=self.ipconfig, height=2, width=12)
        self.ipconfig_button.grid(row=2, column=0, sticky=W)

        self.powershell_button = Button(self, text="powershell",
            command=self.powershell, height=2, width=12)
        self.powershell_button.grid(row=3, column=0, sticky=W)

        self.logoff_button = Button(self, text="logoff",
            command=self.logoff, height=2, width=12)
        self.logoff_button.grid(row=4, column=0, sticky=W)

        self.shutdown_button = Button(self, text="shutdown",
            command=self.shutdown, height=2, width=12)
        self.shutdown_button.grid(row=5, column=0, sticky=W)

        self.shutdown_abort_button = Button(self, text="abort s.d.",
            command=self.shutdown_abort, height=2, width=12)
        self.shutdown_abort_button.grid(row=1, column=1, sticky=W)

        self.restart_button = Button(self, text="restart",
            command=self.restart, height=2, width=12)
        self.restart_button.grid(row=2, column=1, sticky=W)

        self.chrome_button = Button(self, text="chrome",
            command=self.chrome, height=2, width=12)
        self.chrome_button.grid(row=3, column=1, sticky=W)

        self.netflix_button = Button(self, text="Netflix",
            command=self.netflix, height=2, width=12)
        self.netflix_button.grid(row=4, column=1, sticky=W)

        self.cbs_button = Button(self, text="CBS",
            command=self.CBS, height=2, width=12)
        self.cbs_button.grid(row=5, column=1, sticky=W)

        self.firewall_enable_button = Button(self, text="firewall ON",
            command=self.firewall_enable, height=2, width=12)
        self.firewall_enable_button.grid(row=1, column=2, sticky=W)

        self.firewall_disable_button = Button(self, text="firewall OFF",
            command=self.firewall_disable, height=2, width=12)
        self.firewall_disable_button.grid(row=2, column=2, sticky=W)

        self.flushdns_button = Button(self, text="flush DNS",
            command=self.flushdns, height=2, width=12)
        self.flushdns_button.grid(row=3, column=2, sticky=W)

        self.test_connection_button = Button(self, text="ping test",
            command=self.test_connection, height=2, width=12)
        self.test_connection_button.grid(row=4, column=2, sticky=W)

        self.regedit_button = Button(self, text="regedit",
            command=self.firewall_disable, height=2, width=12)
        self.regedit_button.grid(row=5, column=2, sticky=W)

        self.incognito_chrome_button = Button(self, text="incog. chrome",
            command=self.incognito_chrome, height=2, width=12)
        self.incognito_chrome_button.grid(row=1, column=3, sticky=W)

        self.wifi_password_button = Button(self, text="wifi password",
            command=self.wifi_password, height=2, width=12)
        self.wifi_password_button.grid(row=2, column=3, sticky=W)

        self.kill_chrome_button = Button(self, text="kill chr + cmd",
            command=self.kill_chrome_cmd, height=2, width=12)
        self.kill_chrome_button.grid(row=3, column=3, sticky=W)

        self.gmail_button = Button(self, text="gmail",
            command=self.gmail, height=2, width=12)
        self.gmail_button.grid(row=4, column=3, sticky=W)

        self.sms_button = Button(self, text="send sms",
            command=self.send_sms, height=2, width=12)
        self.sms_button.grid(row=5, column=3, sticky=W)


###############################################################################

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

    def incognito_chrome(self):
        #starts incognito window
        os.system("start chrome -incognito")

    def wifi_password(self):
        #checks for wifi password for prev. connected network
        #you may use different wireless network
        os.system("netsh wlan show profiles Heisler6-5 key=clear")
        print("Look at KEY CONTENT/SECURITY KEY")

    def kill_chrome_cmd(self):
        #kill any running chrome and command prompt tabs
        #TODO: UPDATE TO POSSIBLY ALL TASKS
        os.system("taskkill /IM chrome.exe /IM cmd.exe /F")

    def gmail(self):
        #open gmail
        os.system("start chrome www.gmail.com")

    def send_sms(self):
        os.system("cd C:\\Users\\liamh\\Desktop\\Scripts")
        os.system("start contacts.txt")
        os.system("python send_sms.py")

###############################################################################

root = Tk()
root.title("Administrative Center")
root.geometry("469x240")

app = Application(root)
root.mainloop()
