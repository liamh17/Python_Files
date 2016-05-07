from tkinter import *

# Create window
root = Tk()

# Modify window
root.title("Labeler")
root.geometry("400x200")

app = Frame(root)
app.grid() 

button1 = Button(app)
button1.configure(text = "This is a button") 
button1.grid() 


# Start event loop
root.mainloop() 
