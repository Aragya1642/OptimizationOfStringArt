# Import my Libraries and whatnot
from tkinter import *
import tkinter as tk  # This library allows for the development of a GUI
from stringart import StringArtGenerator  # This is the string art generator from previous students
import os # Allows for the interaction with the computer os (I think)
from tkinter import filedialog # For Upload function
from PIL import ImageTk, Image, ImageOps, ImageFilter, ImageEnhance # For Upload function
from tkinter import messagebox
from datetime import datetime
import csv
import matplotlib.pyplot as plt # This allows us to graph
import numpy as np
import math
import copy

image_list = {}

# Trying to do this with OOP
class OptimizationGUI:
    def __init__(self):
        ########################################## - Initial Set up
        self.root = tk.Tk()
        self.root.title("String Art Optimization")
        self.root.geometry('1000x800')
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
        self.imageLabel1 = tk.Label(self.root)
        self.imageLabel1.pack(padx=10,pady=10)
        ########################################## - Start generating the stringart
        self.generate_btn = Button(self.root, text = "Optimize my Picture", font= ('Arial', 30), command=self.Generate)
        self.generate_btn.pack(side=tk.TOP)
        ########################################## - Display my Images

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
        self.imageLabel1.configure(image = image_list.get('upload_img'))
        self.imageLabel1.image = image_list.get('upload_img')
        return filepath
    
    def load_image(self, path):
        img = Image.open(path)
        # Resize the image
        orig_width, orig_height = img.size
        scale_factor = max(orig_height, orig_width) / 200
        resized_img = img.resize((int(orig_width/scale_factor), int(orig_height/scale_factor)))
        white_img = Image.new('RGB', (200, 200), (255, 255, 255))
        resized_width, resized_height = resized_img.size
        paste_x = int((200 - resized_width) / 2)
        paste_y = int((200 - resized_height) / 2)
        white_img.paste(resized_img, (paste_x, paste_y))
        
        # Make the image grayscale
        gray_img = white_img.convert('L')

        # Set my gray image
        self.image = gray_img

        # Invert the colors and enhance the image
        self.image = ImageOps.invert(self.image)
        self.image = self.image.filter(ImageFilter.EDGE_ENHANCE_MORE)
        self.image = ImageEnhance.Contrast(self.image).enhance(1)
        self.data = np.array(self.image)  # *IMPORTANT* I have gotten rid of the transformation that the person before me did. This may affect results in the future

    def set_nails(self, nails):
        self.nails = nails

    def set_nodes_circle(self):
        spacing = (2*math.pi)/self.nails

        steps = range(self.nails)

        radius = self.get_radius()

        x = [radius + radius*math.cos(t*spacing) for t in steps]
        y = [radius + radius*math.sin(t*spacing) for t in steps]

        self.nodes = list(zip(x, y)) # I am getting good readings from this

    def set_nodes_rectangle(self):
        perimeter = self.get_perimeter()
        spacing = perimeter/self.nails
        width, height = np.shape(self.data)

        pnails = [ t*spacing for t in range(self.nails) ]

        xarr = []; yarr = []
        for p in pnails:
            if (p < width): # top edge
              x = p; y = 0;
            elif (p < width + height): # right edge
              x = width; y = p - width;
            elif (p < 2*width + height): # bottom edge
              x = width - (p - width - height); # this can obviously be simplified.
              y = height;
            else: # left edge
              x = 0; y = height - (p - 2*width - height);
            xarr.append(x)
            yarr.append(y)

        self.nodes = list(zip(xarr, yarr)) # I am getting good readings from this :)

    def get_radius(self): # This is used for setting the nodes in a circle
        return 0.5*np.amax(np.shape(self.data))

    def get_perimeter(self): # This is used for setting the nodes in a rectangle
        return 2.0*np.sum(np.shape(self.data))

    def set_lines(self, lines):
        self.lines = lines
    
    def set_weight(self,weight):
        self.weight = weight

    def set_seed(self, seed):
        self.seed = seed

    def set_pattern(self): # This is equivalent to the generate function in the stringart code      
        self.nail = self.seed
        self.calculate_paths()
        
        delta = 0.0 # Not exactly sure what this does but probably has some purpose
        pattern = []
        datacopy = copy.deepcopy(self.data)
        for i in range(self.lines):
            # We have calculated all the paths from each pin to every other pin and this data is stored
            # in self.paths

            # Now we need to be able to put these paths on the image and determine which path is the darkest.
            # This will tell us where to put the line down.

            # choose max darkness path
            darkest_nail, darkest_path = self.choose_darkest_path(self.nail)

            # add chosen node to pattern
            pattern.append(self.nodes[darkest_nail])

            # substract chosen path from image
            self.data = self.data - self.weight*darkest_path
            self.data[self.data < 0.0] = 0.0

            if (np.sum(self.data) <= 0.0):
                print("Stopping iterations. No more data or residual unchanged.")
                break

            # store current residual as delta for next iteration
            delta = np.sum(self.data)

            # continue from destination node as new start
            self.nail = darkest_nail

        self.residual = copy.deepcopy(self.data)
        self.data = datacopy

        return pattern

    def calculate_paths(self): # This makes one big list of all the paths possible from each nail.
        for nail, anode in enumerate(self.nodes): # Old code
            self.paths.append([])
            for node in self.nodes:
                path = self.bresenham_path(anode, node)
                self.paths[nail].append(path)
    
    def bresenham_path(self, start, end): # This uses some Bresenham's Line Algorithm, no clue what this is
        # Setup initial conditions
        x1, y1 = start
        x2, y2 = end

        x1 = max(0, min(round(x1), self.data.shape[0]-1))
        y1 = max(0, min(round(y1), self.data.shape[1]-1))
        x2 = max(0, min(round(x2), self.data.shape[0]-1))
        y2 = max(0, min(round(y2), self.data.shape[1]-1))

        dx = x2 - x1
        dy = y2 - y1

        # Prepare output array
        path = []

        if (start == end):
            return path

        # Determine how steep the line is
        is_steep = abs(dy) > abs(dx)

        # Rotate line
        if is_steep:
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        # Swap start and end points if necessary and store swap state
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        # Recalculate differentials
        dx = x2 - x1
        dy = y2 - y1

        # Calculate error
        error = int(dx / 2.0)
        ystep = 1 if y1 < y2 else -1

        # Iterate over bounding box generating points between start and end
        y = y1
        for x in range(x1, x2 + 1):
            if is_steep:
                path.append([y, x])
            else:
                path.append([x, y])
            error -= abs(dy)
            if error < 0:
                y += ystep
                error += dx

        return path
    
    def choose_darkest_path(self, nail):
        max_darkness = -1.0
        for count, rowcol in enumerate(self.paths[nail]):
            rows = [i[0] for i in rowcol]
            cols = [i[1] for i in rowcol]
            darkness = float(np.sum(self.data[rows, cols]))

            if darkness > max_darkness:
                darkest_path = np.zeros(np.shape(self.data))
                darkest_path[rows,cols] = 1.0
                darkest_nail = count
                max_darkness = darkness
        return darkest_nail, darkest_path

    def Generate(self):

        if self.entry1.get() == '' or self.entry2.get() == '' or self.entry3.get() == '' or self.entry4.get() == '' or self.entry5.get() == '' or self.path_label.cget("text") == '':
            messagebox.showwarning("Warning","Please fill all the blanks above")
            return None
        
        # Set my shape
        if self.check1_state.get() == 1:
            self.shape = 'circle'
        elif self.check2_state.get() == 1:
            self.shape = 'rectangle'

        # Using loops to generate 9 instances of an image
        a=0 # This will increment the number of pins
        b=0 # This will increment the number of lines
        c=1 # This will show which iteration we are on

        # Take total range of pins and divide by 3 to get the values at which the image needs to be generated
        pin_range = int(self.entry2.get()) - int(self.entry1.get())
        pin_increment = pin_range / 2

        # Take total range of pins and divide by 3 to get the values at which the image needs to be generated
        line_range = int(self.entry5.get()) - int(self.entry4.get())
        line_increment = line_range / 2
        
        while a < 3:
            my_iteration_p = int(self.entry1.get()) + ((a)*pin_increment) # This calculates the number of pins for the specific iteration
            
            while b < 3:
                my_iteration_l = int(self.entry4.get()) + ((b)*line_increment) # This calculates the number of lines for the specific iteration

                # Print what iteration
                print("Iteration", c)
                print("Pins are:", my_iteration_p)
                print("Lines are:", my_iteration_l)
                
                # Increment iteration number
                c = c+1

                # Starting to rewrite my code
                self.load_image(self.path_label.cget("text")) # This does my preprocessing too
                self.set_nails(int(my_iteration_p))
                self.set_lines(int(my_iteration_l))
                self.set_weight(int(self.entry3.get()))
                self.set_seed(1) # I need to understand where she got this value of 42 from
                if self.shape == 'circle':
                    self.set_nodes_circle()
                elif self.shape == 'rectangle':
                    self.set_nodes_rectangle()
                self.paths = []
                self.pattern = self.set_pattern() # This returns the order of the nodes that will be graphed
                
                # This is the meat of generation code programmed by previous students
                
                lines_x = []
                lines_y = [] 
                axis_list = []
                for i, j in zip(self.pattern, self.pattern[1:]): 
                    lines_x.append((i[0], j[0]))
                    lines_y.append((i[1], j[1]))
                    axis_list.append((i[0], i[1])) 

                axis_w_index = []
                res = []
                point_ref = []
                [res.append(x) for x in axis_list if x not in res]
                axis_w_index.append((0,0.000,0.000,0.000))
                for i in axis_list:
                    axis_w_index.append((res.index(i)+1,i[0],i[1],0.000))
                point_ref.append((0,0.000,0.000,0.000))
                for i in res:
                    point_ref.append((res.index(i)+1,i[0],i[1],0.000))
                
                order = []
                for i in axis_w_index:
                    order.append((i[0],0.000))

                # print(order[0:10])
                # print(axis_w_index[0:10])

                current_dateTime = datetime.now()
                d1 = current_dateTime.strftime("%Y%m%d%H%M%S")

                axis_index_name = os.path.join(os.getcwd(),'StringArt_doc', "axis_w_index_" + d1 + ".txt")
                # print(axis_index_name)
                os.makedirs(os.path.dirname(axis_index_name), exist_ok=True)
                f4 = open(axis_index_name, "w+")
                with f4:   
                    write = csv.writer(f4)
                    write.writerows(axis_w_index)
                f4.close()

                point_ref_name = os.path.join(os.getcwd(), 'StringArt_doc', "point_reference_" + d1 + ".txt")
                os.makedirs(os.path.dirname(point_ref_name), exist_ok=True)
                f = open(point_ref_name, 'w+')
                for t in point_ref:
                    line = ' '.join(str(x).strip('(').strip(',').strip(')') for x in t)
                    f.write(line + '\n')
                f.close()

                order_name = os.path.join(os.getcwd(), 'StringArt_doc', "order_" + d1 + ".txt")
                os.makedirs(os.path.dirname(order_name), exist_ok=True)
                f5 = open(order_name, 'w+')
                for t in order[1:]:
                    line = ' '.join(str(order).strip('(').strip(')') for order in t)
                    f5.write(line+'\n')
                f5.close()

                xmin = 0.
                ymin = 0.
                xmax = self.data.shape[0]
                ymax = self.data.shape[1]

                plt.ion()
                plt.figure(figsize=(8, 8))
                plt.axis('off')
                axes = plt.gca()
                axes.set_xlim([xmin, xmax])
                axes.set_ylim([ymin, ymax])
                axes.get_xaxis().set_visible(False)
                axes.get_yaxis().set_visible(False)
                axes.set_aspect('equal')
                plt.draw()

                batchsize = 10
                for i in range(0, len(lines_x), batchsize):
                    plt.plot(lines_x[i:i+batchsize], lines_y[i:i+batchsize],
                            linewidth=0.1, color='k')
                    plt.draw()
                    plt.pause(0.000001)

                save_fig_path = os.path.join(os.getcwd(), 'StringArt_doc', "result_" + d1 + ".png")
                os.makedirs(os.path.dirname(save_fig_path), exist_ok=True)
                plt.savefig(save_fig_path, bbox_inches='tight', pad_inches=0)

                result_img = Image.open(save_fig_path)
                resize_result_image = result_img.resize((200, 200))

                b += 1
            
            b = 0
            a += 1
        

# This is where code starts and refrences back to my class
OptimizationGUI()