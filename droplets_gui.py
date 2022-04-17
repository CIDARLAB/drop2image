from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageColor
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import cv2
import serial
import time

#
# original_filename = ""
#
# def open_img():
#     # Select the Imagename  from a folder
#     original_filename = openfilename()
#     x = original_filename
#
#     # open the image and display
#     img = Image.open(x)
#     img = img.resize((250, 250), Image.Resampling.LANCZOS)
#
#     # PhotoImage class is used to add image to widgets, icons etc
#     img = ImageTk.PhotoImage(img)
#
#     # create a label
#     panel = Label(root, image = img)
#
#     # set the image as img
#     panel.image = img
#     panel.grid(row = 2)
#
#
# def openfilename():
#     filename = filedialog.askopenfilename(title = "original")
#     return filename
#
# def transformation():
#     x = resize_image(original_filename, 100)
#
# def resize_image(filename, size):
#     # can i assume that the aspect ratio of input image file and user specified size are the same?
#     # ok
#     im = Image.open(filename)
#     r_im = im.resize(size)
#     r_im.save('resized_image')
#     return r_im
#
#
# root = Tk()
# root.title("Image Loader")
# root.geometry("550x300")
# root.resizable(width = True, height = True)
# main_btn = Button(root, text = 'open image', command= open_img).grid(row = 1, columnspan = 4)
# run_btn = Button(root, text = 'run', command = transformation).grid(row = 3, columnspan = 5)
# root.mainloop()

class GUI:
    def __init__(self):
        self.filename = None
        self.src = None
        self.root = Tk()
        self.image_size = (10,10) #default 10x10
        self.pix_list = []
        self.color_set = ['#FFFFFF', '#000000'] #default Black and White

        self.root.title("Image Loader")
        self.root.geometry("550x300")
        self.root.resizable(width = True, height = True)

        main_btn = Button(self.root, text = 'open image', command=lambda: self.open_img()).grid(row = 1)

        frame_size = ttk.Frame(self.root, padding = (32)).grid()
        label_width = ttk.Label(frame_size, text = 'width', padding = (5,2)).grid(row = 3, column = 0, sticky =  E)
        label_height = ttk.Label(frame_size, text = 'height', padding = (5,2)).grid(row = 4, column = 0, sticky = E)
        label_color = ttk.Label(frame_size, text = 'color set', padding = (5,2)).grid(row = 5, column = 0, sticky = E)

        width = StringVar()
        width_entry = ttk.Entry(frame_size, textvariable=width, width=10).grid(row = 3, column = 1)
        height = StringVar()
        height_entry = ttk.Entry(frame_size, textvariable=height, width=10).grid(row = 4, column = 1)
        color = StringVar()
        color_entry = ttk.Entry(frame_size, textvariable=color, width=10).grid(row = 5, column = 1)

        set_size_btn = Button(self.root, text = 'OK', command=lambda: self.set_size(width, height, color)).grid(row = 6)

        run_btn = Button(self.root, text = 'run', command = lambda: self.transformation(self.image_size)).grid(row = 8)

        #send_btn = Button(self.root, text = 'send to Arduino', command = lambda: self.send_to_Arduino()).grid(row = 6, columnspan = 8)
        self.root.mainloop()



    def open_img(self):
        # Select the Imagename  from a folder
        self.filename = self.openfilename()

        # open the image and display
        img = Image.open(self.filename)
        self.src = img
        img = img.resize((250, 250), Image.Resampling.LANCZOS)

        # PhotoImage class is used to add image to widgets, icons etc
        img = ImageTk.PhotoImage(img)

        # create a label
        panel = Label(self.root, image = img)

        # set the image as img
        panel.image = img
        panel.grid(row = 2)

    def openfilename(self):
        filename = filedialog.askopenfilename(title = "original")
        return filename

    def transformation(self, size):
        resized_img = self.resize_image(size)
        resized_img = resized_img.resize((250, 250), Image.Resampling.LANCZOS) # so that user can see (super blurred)
        resized_img = ImageTk.PhotoImage(resized_img)
        panel = Label(self.root, image = resized_img)
        panel.image = resized_img
        panel.grid(row = 7)



    def resize_image(self, size):
        if self.src is None:
            self.filename = self.openfilename()
            self.src = Image.open(self.filename)

        r_im = self.src.resize((size))
        file = self.filename.split('.')
        filename = file[0] + '_resized.png'
        r_im.save(filename)
        return r_im

    def set_size(self, w, h, c):
        self.image_size = (int(w.get()),int(h.get()))
        if (len(c.get()) != 0):
            self.color_set = (c.get()).split(', ')

    def send_to_Arduino(self):
        print('Open Port')
        ser = serial.Serial("PortName", 9600)

    def get_closest_color(self, pix, color):
        closest_color = None
        min_diff = 100000
        pix = np.array(pix)
        for clr in color:
            clr = np.array(clr)
            diff = np.sum((clr-pix)**2)
            if diff < min_diff:
                min_diff = diff
                closest_color = clr
        return closest_color

    def get_closest_image(self, filename, color_set):
        im = cv2.imread(filename)
        color_set_rgb = [ImageColor.getrgb(color) for color in color_set]
        h, w, c = im.shape
        im_out = np.zeros((h,w,c))

        for i in range(h):
            for j in range(w):
                b,g,r = im[i,j]
                c_r, c_g, c_b = self.get_closest_color((r,g,b), color_set_rgb)
                im_out[i,j,:] = (c_b, c_g, c_r)
                # fixing the order of rgb
        return im_out

    def convert_jpeg_to_pix(self, filename, color_set):
        im = Image.open(filename, 'r')
        w, h = im.size
        im = im.convert('RGB')
        color_set_rgb = [ImageColor.getrgb(color) for color in color_set]
        if w%2==0:
            for i in range(h):
                for j in range(w):
                    if i%2==0:
                        pix = color_set_rgb.index(im.getpixel((j,i)))
                    else:
                        pix = color_set_rgb.index(im.getpixel((w-1-j,i)))
                    self.pix_list.append(pix)
        else:
            for i in range(h):
                for j in range(w):
                    if i%2==0:
                        pix = color_set_rgb.index(im.getpixel((w-1-j,i)))
                    else:
                        pix = color_set_rgb.index(im.getpixel((j,i)))
                    self.pix_list.append((pix))




test = GUI()