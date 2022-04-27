import string
from tkinter import *
from PIL import Image
from PIL import ImageTk
from PIL import ImageColor
from tkinter import filedialog
from tkinter import ttk
import numpy as np
import cv2
import os
import time
import http.server
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

class MyServer(threading.Thread):
    def run(self):
        self.server = ThreadingHTTPServer(('10.192.13.179', 8888), SimpleHTTPRequestHandler)
        self.server.serve_forever()
    def stop(self):
        self.server.shutdown()

class GUI:
    def __init__(self):
        self.filename = None
        self.directory = None
        self.filename_closest = None
        self.filename_txt = None
        self.src = None
        self.src_cv2 = None
        self.port = None
        self.root = Tk()
        self.image_size = (10,10) #default 10x10
        self.pix_list = []
        self.color_set = ['#FFFFFF', '#000000'] #default Black and White

        self.root.title("Image Loader")
        self.root.geometry("500x1000")
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

        run_btn = Button(self.root, text = 'run', command = lambda: self.transformation(self.image_size, color)).grid(row = 9)

        # dev = [info.device for info in list_ports.comports()]
        # self.port = StringVar()
        # select_box = ttk.Combobox(self.root, textvariable=self.port, values=dev, style='office.TCombobox').grid(row = 10)

        #send_btn = Button(self.root, text = 'send to Arduino', command = lambda: self.TCP()).grid(row = 11)
        #send_btn = Button(self.root, text = 'send to Arduino', command = lambda: self.Serial_Com()).grid(row = 11)
        #send_btn = Button(self.root, text = 'send to Arduino', command = lambda: self.Bridge_Com()).grid(row = 11)
        send_btn = Button(self.root, text = 'send to Arduino', command = lambda: self.send_to_Arduino()).grid(row = 10)
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

    def transformation(self, size, color_set):
        resized_img = self.resize_image(size)
        resized_img = resized_img.resize((250, 250), Image.Resampling.LANCZOS) # so that user can see (super blurred)
        resized_img = ImageTk.PhotoImage(resized_img)
        panel = Label(self.root, image = resized_img)
        panel.image = resized_img
        panel.grid(row = 7)
        cv2_closest_resized_img = self.get_closest_image(self.src_cv2, self.color_set)
        closest_resized_img = Image.open(self.filename_closest)
        closest_resized_img = closest_resized_img.resize((250, 250), Image.Resampling.LANCZOS)
        closest_resized_img = ImageTk.PhotoImage(image = closest_resized_img)
        panel2 = Label(self.root, image = closest_resized_img)
        panel2.image = closest_resized_img
        panel2.grid(row = 8)
        self.convert_jpeg_to_pix(self.filename_closest, self.color_set)
        self.output_format(self.pix_list)

    def resize_image(self, size):
        if self.src is None:
            self.filename = self.openfilename()
            self.src = Image.open(self.filename)

        r_im = self.src.resize((size))
        file = self.filename.split('.')
        filename = file[0] + '_resized.png'
        r_im.save(filename)
        self.src_cv2 = cv2.imread(filename)
        return r_im

    def set_size(self, w, h, c):
        self.image_size = (int(w.get()),int(h.get()))
        if (len(c.get()) != 0):
            self.color_set = (c.get()).split(', ')

    def send_to_Arduino(self):
        os.chdir(self.directory)
        server_address = ('', 8080)
        s = MyServer()
        s.start()
        print('thread alive:', s.is_alive())  # True
        time.sleep(30)
        s.stop()
        print('thread alive:', s.is_alive())  # False

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

    def get_closest_image(self, im, color_set):
        #im = cv2.imread(filename)
        color_set_rgb = [ImageColor.getrgb(color) for color in color_set]
        h, w, c = im.shape
        im_out = np.zeros((h,w,c))

        for i in range(h):
            for j in range(w):
                b,g,r = im[i,j]
                c_r, c_g, c_b = self.get_closest_color((r,g,b), color_set_rgb)
                im_out[i,j,:] = (c_b, c_g, c_r)
                # fixing the order of rgb

        file = self.filename.split('.')
        self.filename_closest = file[0] + '_closest.png'
        cv2.imwrite(self.filename_closest, im_out)
        return im_out

    def convert_jpeg_to_pix(self, filename, color_set):
        im = Image.open(filename, 'r')
        w, h = im.size
        im = im.convert('RGB')
        color_set_rgb = [ImageColor.getrgb(color) for color in color_set]
        self.pix_list.clear()
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

    def output_format(self, pix):
        file = self.filename.split('/')
        path = ''
        for dr in file:
            if '.' in dr:
                continue
            else:
                path += dr + '/'
        self.directory = path
        self.filename_txt = self.directory + 'pix.txt'
        txt = open(self.filename_txt, 'w').close()
        txt = open(self.filename_txt, 'a')
        np.savetxt(self.filename_txt, pix, fmt='%d', delimiter=" ")
        txt.close()
        return



test = GUI()

#need to implement menu tab
#need to implement select menu for serial port -> done


# README first -> instructions
# repo name: drop to image

# add title, background, centered
# making small changes to make sure mirror worked
