from ctypes import sizeof
from tkinter import *
from tkinter import filedialog
from tkmacosx import Button
import string
from turtle import back, color
import numpy as np

class GUI:
    def __init__(self):
        self.cur_color = None
        self.root = Tk()
        self.pix_btn = []
        self.color_set = ['gray', 'black', 'blue', 'red', 'green', 'yellow', 'pink', 'cyan', 'white']
        # what should be the default color??
        # skip = red x
        # default = black
        self.x = 15
        self.y = 15
        self.pix_list = []
        self.save_filename = None

        self.root.title("Pixel Art GUI")
        self.root.geometry("1000x1000")

        main_frm = Frame(self.root).grid(row=0, column=0)

        myscrollbar=Scrollbar(main_frm, orient="vertical").grid(row=0, column=16, sticky=NS)

        black_btn = Button(main_frm, command = lambda: self.set_color('black'), bg='black', width=50).grid(row=0, column=0)
        blue_btn = Button(main_frm, command = lambda: self.set_color('blue'), bg='blue', width=50).grid(row=0, column=1)
        red_btn = Button(main_frm, command = lambda: self.set_color('red'), bg='red', width=50).grid(row=0, column=2)
        green_btn = Button(main_frm, command= lambda: self.set_color('green'), bg='green', width=50).grid(row=0, column=3)
        skip_btn = Button(main_frm, command= lambda: self.set_color('purple'), width=50, text='skip').grid(row=0, column=4)
        yellow_btn = Button(main_frm, command= lambda: self.set_color('yellow'), bg='yellow', width=50).grid(row=1, column=0)
        pink_btn = Button(main_frm, command= lambda: self.set_color('pink'), bg='pink', width=50).grid(row=1, column=1)
        cyan_btn = Button(main_frm, command= lambda: self.set_color('cyan'), bg='cyan', width=50).grid(row=1, column=2)
        white_btn = Button(main_frm, command= lambda: self.set_color('white'), bg='white', width=50).grid(row=1, column=3)
        reset_btn = Button(main_frm, command= lambda: self.set_color('gray'), bg='gray', width=50).grid(row=1, column=4)

        for i in range(self.y):
            pix_btn_row = []
            for j in range(self.x):
                pix_btn_row.append(Button(main_frm, command= lambda i=i, j=j: self.change_pix(i,j), width=50, height=50, bg='gray'))
                pix_btn_row[j].grid(row=i+2, column=j)
            self.pix_btn.append(pix_btn_row)

        save_btn = Button(self.root, command= lambda: self.save_pix(), text='Save').grid(row=self.y+3, column=self.x+1)
        save_as_btn = Button(self.root, command= lambda: self.save_as_pix(), text= 'Save as').grid(row=self.y+4, column=self.x+1)

        self.root.mainloop()

    def set_color(self, color):
        self.cur_color = color

    def change_pix(self, i, j):
        red_cross = PhotoImage(file= r"/Users/kaedekawata/Documents/STEM_Pathway/droplets/emoji_test/red_x.png").subsample(8,8)
        if (self.cur_color == 'purple'):
            self.pix_btn[i][j].config(image= red_cross)
        self.pix_btn[i][j].config(bg=self.cur_color)

    def format_pix(self):
        if self.y%2==0:
            for i in range(self.y):
                for j in range(self.x):
                    if i%2==0:
                        if (self.pix_btn[i][j].cget('bg') == 'purple'):
                            continue
                        pix = self.color_set.index(self.pix_btn[i][j].cget('bg'))
                    else:
                        if (self.pix_btn[i][self.x-1-j].cget('bg') == 'purple'):
                            continue
                        pix = self.color_set.index(self.pix_btn[i][self.x-1-j].cget('bg'))
                    self.pix_list.append(pix)
        else:
            for i in range(self.y):
                for j in range(self.x):
                    if i%2==0:
                        if (self.pix_btn[i][self.x-1-j].cget('bg') == 'purple'):
                            continue
                        pix = self.color_set.index(self.pix_btn[i][self.x-1-j].cget('bg'))
                    else:
                        if (self.pix_btn[i][j].cget('bg') == 'purple'):
                            continue
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


if __name__ == '__main__':
    test = GUI()

# 