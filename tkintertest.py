import tkinter as tk

root  = tk.Tk() # This creates my initial window
root.geometry("500x500") # This changes the size of the window
root.title("My first GUI") # This sets the name of the actual window, does not set a header

label = tk.Label(root, text="Hello World", font=('Arial', 18))
label.pack(pady=20)

textbox = tk.Text(root, height=3, font=('Arial',16))
textbox.pack()

root.mainloop()