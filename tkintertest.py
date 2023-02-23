
# Using youtube video: https://www.youtube.com/watch?v=ibf5cx221hk
# Left the video at 7:37

import tkinter as tk

root  = tk.Tk() # This creates my initial window
root.geometry("500x500") # This changes the size of the window
root.title("My first GUI") # This sets the name of the actual window, does not set a header

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(pady=20) # The pack feature basically puts the above code into the GUI

textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack(padx=10, pady = 10)

buttonframe = tk.Frame(root) # Sets up the button fram within my window
buttonframe.columnconfigure(0, weight = 1)
buttonframe.columnconfigure(1, weight = 1)
buttonframe.columnconfigure(2, weight = 1) # This created 3 columns, I could also do it by rows but the variable you configure should be fixed

btn1 = tk.Button(buttonframe, text = "1", font = ('Arial', 18))
btn1.grid(row=0, column=0, sticky = tk.W+tk.E)

btn2 = tk.Button(buttonframe, text = "2", font = ('Arial', 18))
btn2.grid(row=0, column=1, sticky = tk.W+tk.E)

btn3 = tk.Button(buttonframe, text = "3", font = ('Arial', 18))
btn3.grid(row=0, column=2, sticky = tk.W+tk.E)

btn4 = tk.Button(buttonframe, text = "4", font = ('Arial', 18))
btn4.grid(row=1, column=0, sticky = tk.W+tk.E)

btn5 = tk.Button(buttonframe, text = "5", font = ('Arial', 18))
btn5.grid(row=1, column=1, sticky = tk.W+tk.E)

btn6 = tk.Button(buttonframe, text = "6", font = ('Arial', 18))
btn6.grid(row=1, column=2, sticky = tk.W+tk.E)

buttonframe.pack(fill = 'x')

anotherbtn = tk.Button(root, text = "TEST")
anotherbtn.place(x=200, y=200, height=100, width=100) # This is kinda shitty so...

# button = tk.Button(root, text = "Click Me!", font = ('Arial', 18))
# button.pack(padx = 10, pady = 10)

# myentry = tk.Entry(root) # This makes an entry box which is a single line and probably what I will use in my GUI
# myentry.pack()

root.mainloop()