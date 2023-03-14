# Import my Libraries and whatnot
from tkinter import *
import tkinter as tk  # This library allows for the development of a GUI
from stringart import StringArtGenerator  # This is the string art generator from previous students

# Trying to do this with OOP
class OptimizationGUI:
    def __init__(self):
        ########################################## - Initial Set up
        self.root = tk.Tk()
        self.root.title("String Art Optimization")
        self.root.geometry('600x600')
        ########################################## - Title
        self.label = tk.Label(self.root, text="String Art Optimization", font=('Arial', 18))
        self.label.pack(padx=10, pady=0)
        ########################################## - Shape
        self.sublabel1 = tk.Label(self.root, text="Canvas Shape", font=('Arial', 14))
        self.sublabel1.pack(padx=10, pady=10, anchor="nw")

        self.check1_state = tk.IntVar()
        self.check2_state = tk.IntVar()

        self.check1 = tk.Checkbutton(self.root, text = "Circle", font=('Arial', 10), variable=self.check1_state, command=self.check_buttons)
        self.check1.pack(padx=10, anchor="nw")

        self.check2 = tk.Checkbutton(self.root, text = "Rectangle", font=('Arial', 10), variable=self.check2_state, command=self.check_buttons)
        self.check2.pack(padx=10, anchor="nw")
        ########################################## - Number of Nails
        self.sublabel2 = tk.Label(self.root, text="Number of Nails", font=('Arial', 14))
        self.sublabel2.pack(padx=10, pady=10, anchor="nw")

        self.nail_frame = tk.Frame(self.root)
        self.nail_frame.pack(padx=10, pady=10, anchor="nw")

        self.subsublabel1 = tk.Label(self.nail_frame, text="Minimum:", font=('Arial', 10))
        self.subsublabel1.pack(side=tk.LEFT)

        self.entry1 = tk.Entry(self.nail_frame)
        self.entry1.pack(padx=15, side=tk.LEFT)

        self.subsublabel2 = tk.Label(self.nail_frame, text="Maximum:", font=('Arial', 10))
        self.subsublabel2.pack(side=tk.LEFT)

        self.entry2 = tk.Entry(self.nail_frame)
        self.entry2.pack(padx=15, side=tk.LEFT)
        ########################################## - Line Weight
        self.sublabel3 = tk.Label(self.root, text="Line Weight", font=('Arial', 14))
        self.sublabel3.pack(padx=10, pady=10, anchor="nw")

        self.entry3 = tk.Entry(self.root)
        self.entry3.pack(padx=10, anchor="nw")
        ########################################## - Number of Lines
        self.sublabel4 = tk.Label(self.root, text="Number of Lines", font=('Arial', 14))
        self.sublabel4.pack(padx=10, pady=10, anchor="nw")

        self.line_frame = tk.Frame(self.root)
        self.line_frame.pack(padx=10, pady=10, anchor="nw")

        self.subsublabel3 = tk.Label(self.line_frame, text="Minimum:", font=('Arial', 10))
        self.subsublabel3.pack(side=tk.LEFT)

        self.entry4 = tk.Entry(self.line_frame)
        self.entry4.pack(padx=15, side=tk.LEFT)

        self.subsublabel4 = tk.Label(self.line_frame, text="Maximum:", font=('Arial', 10))
        self.subsublabel4.pack(side=tk.LEFT)

        self.entry5 = tk.Entry(self.line_frame)
        self.entry5.pack(padx=15, side=tk.LEFT)
        ##########################################
        self.root.mainloop()

# If I want to add more buttons, I need to define their functions here.
    def check_buttons(self):
        if self.check1_state.get() == 1:
            self.check2_state.set(0)
        elif self.check2_state.get() == 1:
            self.check1_state.set(0)

# This is where code starts and refrences back to my class
OptimizationGUI()