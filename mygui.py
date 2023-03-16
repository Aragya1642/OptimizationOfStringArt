# Import my Libraries and whatnot
from tkinter import *
import tkinter as tk  # This library allows for the development of a GUI
from stringart import StringArtGenerator  # This is the string art generator from previous students
import os # Allows for the interaction with the computer os (I think)
from tkinter import filedialog # For Upload function
from PIL import ImageTk, Image # For Upload function


image_list = {}

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
        ########################################## - Upload
        self.sublabel5 = tk.Label(self.root, text="Upload your Image", font=('Arial', 14))
        self.sublabel5.pack(padx=10, pady=10, anchor="nw")

        self.button1 = tk.Button(self.root, text="Upload", font=('Arial', 10), command= self.Upload)
        self.button1.pack(padx=10, pady=0, anchor="nw")
        ########################################## - Shows Image path
        self.path_label = tk.Label(self.root, text = '  ')
        self.path_label.pack()
        img_path_value = self.path_label.cget("text")
        ########################################## - Showing the uploaded image
        self.imageLabel = tk.Label(self.root)
        self.imageLabel.pack(padx=10,pady=10)
        ########################################## - Start generating the stringart
        self.generate_btn = Button(self.root, text = "Optimize my Picture", font= ('Arial', 30))
        self.generate_btn.pack(side=tk.TOP)
        # Make sure to add a command to the optimize button
        ##########################################
        self.root.mainloop()

# If I want to add more buttons, I need to define their functions here.
    def check_buttons(self):
        if self.check1_state.get() == 1:
            self.check2_state.set(0)
        elif self.check2_state.get() == 1:
            self.check1_state.set(0)

    def Upload(self):
        print('upload')
        selectFileName = filedialog.askopenfile(mode='r', title = 'Select a image', filetypes=[
                        ("image", ".jpeg"),
                        ("image", ".png"),
                        ("image", ".jpg"),
                    ])
        filepath = os.path.abspath(selectFileName.name)
        print(filepath)
        self.path_label.configure(text=filepath)

        # Create an object of tkinter ImageTk
        img = Image.open(self.path_label.cget("text"))
            # Resize the image
        orig_width, orig_height = img.size
        scale_factor = max(orig_height, orig_width) / 200
        resized_img = img.resize((int(orig_width/scale_factor), int(orig_height/scale_factor)))
        white_img = Image.new('RGB', (200, 200), (255, 255, 255))
        resized_width, resized_height = resized_img.size
        paste_x = int((200 - resized_width) / 2)
        paste_y = int((200 - resized_height) / 2)
        white_img.paste(resized_img, (paste_x, paste_y))
        upload_img_tk = ImageTk.PhotoImage(white_img)
        image_list['upload_img'] = upload_img_tk

        # Create a Label Widget to display the text or Image
        self.imageLabel.configure(image = image_list.get('upload_img'))
        self.imageLabel.image = image_list.get('upload_img')
        return filepath
    
# This is where code starts and refrences back to my class
OptimizationGUI()