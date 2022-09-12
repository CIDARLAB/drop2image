import string
from tkinter import *
from tkinter import colorchooser, filedialog, ttk
from PIL import Image, ImageTk, ImageColor
import numpy as np
import cv2

class GUI:
    def __init__(self):
        self.filename = None
        self.root = Tk()
        self.root.title("Drop2Image")
        self.root.geometry("750x1000")
        self.root.resizable(width = True, height = True)
        
        menu_bar = Menu(self.root)
        self.root.config(menu=menu_bar)
        menu_file = Menu(self.root)
        menu_bar.add_cascade(label='File', menu=menu_file)
        menu_file.add_command(label='Open', command=lambda: self.open_img())
        menu_setting = Menu(self.root)
        menu_bar.add_cascade(label='Preference', menu=menu_setting)
        menu_run = Menu(self.root)
        menu_bar.add_cascade(label='Run', menu=menu_run)



        self.root.mainloop()


    def open_img(self):
        self.filename = filedialog.askopenfilename(title = "original")
        img = Image.open(self.filename)
        img = img.resize((200, 200), Image.Resampling.LANCZOS)
        img = ImageTk.PhotoImage(img)
        panel = Label(self.root, image=img)
        panel.image = img
        panel.grid(row=1)


test = GUI()
