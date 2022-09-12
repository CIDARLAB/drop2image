from ctypes import sizeof
from tkinter import *
from tkinter import filedialog
from tkmacosx import Button
import string
from turtle import back
import numpy as np

class GUI:
    def __init__(self):
        self.cur_color = None
        self.root = Tk()
        self.pix_btn = []
        self.color_set = ['gray', 'black', 'blue', 'red', 'green', 'yellow', 'pink', 'cyan', 'white']
        # what should be the default color??
        self.size = 15
        self.pix_list = []
        self.save_filename = None

        self.root.title("Pixel Art GUI")
        self.root.geometry("1000x1000")

        color_cnv = Canvas(self.root)

        black_btn = Button(self.root, command = lambda: self.set_color('black'), bg='black', width=50).grid(row=1, column=1)
        blue_btn = Button(self.root, command = lambda: self.set_color('blue'), bg='blue', width=50).grid(row=1, column=2)
        red_btn = Button(self.root, command = lambda: self.set_color('red'), bg='red', width=50).grid(row=1, column=3)
        green_btn = Button(self.root, command= lambda: self.set_color('green'), bg='green', width=50).grid(row=1, column=4)
        yellow_btn = Button(self.root, command= lambda: self.set_color('yellow'), bg='yellow', width=50).grid(row=2, column=1)
        pink_btn = Button(self.root, command= lambda: self.set_color('pink'), bg='pink', width=50).grid(row=2, column=2)
        cyan_btn = Button(self.root, command= lambda: self.set_color('cyan'), bg='cyan', width=50).grid(row=2, column=3)
        white_btn = Button(self.root, command= lambda: self.set_color('white'), bg='white', width=50).grid(row=2, column=4)

        for i in range(self.size):
            pix_btn_row = []
            for j in range(self.size):
                pix_btn_row.append(Button(self.root, command= lambda i=i, j=j: self.change_pix(i,j), width=50, height=50, bg='gray'))
                pix_btn_row[j].grid(row=i+3, column=j+1)
            self.pix_btn.append(pix_btn_row)

        save_btn = Button(self.root, command= lambda: self.save_pix(), text='Save').grid(row=self.size+3, column=self.size+1)
        save_as_btn = Button(self.root, command= lambda: self.save_as_pix(), text= 'Save as').grid(row=self.size+4, column=self.size+1)

        self.root.mainloop()

    def set_color(self, color):
        self.cur_color = color

    def change_pix(self, i, j):
        self.pix_btn[i][j].config(bg=self.cur_color)

    def format_pix(self):
        if self.size%2==0:
            for i in range(self.size):
                for j in range(self.size):
                    if i%2==0:
                        pix = self.color_set.index(self.pix_btn[i][j].cget('bg'))
                    else:
                        pix = self.color_set.index(self.pix_btn[i][self.size-1-j].cget('bg'))
                    self.pix_list.append(pix)
        else:
            for i in range(self.size):
                for j in range(self.size):
                    if i%2==0:
                        pix = self.color_set.index(self.pix_btn[i][self.size-1-j].cget('bg'))
                    else:
                        pix = self.color_set.index(self.pix_btn[i][j].cget('bg'))
                    self.pix_list.append(pix)

    def save_pix(self):
        self.pix_list = []
        self.format_pix()
        if (self.save_filename is None):
            self.save_filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title="Choose filename")
        with open(self.save_filename, 'w'):
            np.savetxt(self.save_filename, self.pix_list, fmt='%d', delimiter=' ')

    def save_as_pix(self):
        self.pix_list = []
        self.format_pix()
        self.save_filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title="Choose filename")
        with open(self.save_filename, 'w'):
            np.savetxt(self.save_filename, self.pix_list, fmt='%d', delimiter=' ')


test = GUI()
