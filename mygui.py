# Import my Libraries and whatnot

from tkinter import *
import tkinter as tk  # This library allows for the development of a GUI
from stringart import StringArtGenerator  # This is the string art generator from previous students

# Defining my processes for my GUI
def button_clicked():
    print("Button Clicked!")

# Creating GUI window
window = tk.Tk()
window.title('String Art Generator/Optimizer')
window.geometry('600x600')

# Placing Header
header_label = tk.Label(window, text='String Art Generator', font = ('Ariel', 20))
header_label.place(relx=0.5, rely=0.05, anchor=CENTER)

# Placing a button
button = tk.Button(window, text = "Click me!", command = button_clicked)

mainloop()