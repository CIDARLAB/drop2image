from ctypes import sizeof
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
# from tkmacosx import Button
import string
from turtle import back, color
import numpy as np
import serial
from serial.tools import list_ports
import time

class GUI:
    def __init__(self):
        self.cur_color = None
        self.root = Tk()
        self.pix_btn = []
        self.color_set = ['gray', 'black', 'blue', 'red', 'green', 'yellow', 'pink', 'cyan', 'white']
        # skip = red x
        # default = black
        self.x = 50
        self.y = 25
        self.pix_list = []
        self.pix_mat = None
        self.save_filename = None
        self.port = None

        self.root.title("Pixel Art GUI")
        self.root.geometry("1000x1000")

        main_frm = Frame(self.root).grid(row=0, column=0)

        myscrollbar=Scrollbar(main_frm, orient="vertical").grid(row=0, column=16, sticky=NS)
        w = 3

        black_btn = Button(main_frm, command = lambda: self.set_color('black'), bg='black', width=w).grid(row=0, column=0)
        blue_btn = Button(main_frm, command = lambda: self.set_color('blue'), bg='blue', width=w).grid(row=0, column=1)
        red_btn = Button(main_frm, command = lambda: self.set_color('red'), bg='red', width=w).grid(row=0, column=2)
        green_btn = Button(main_frm, command= lambda: self.set_color('green'), bg='green', width=w).grid(row=0, column=3)
        skip_btn = Button(main_frm, command= lambda: self.set_color('purple'), width=w, text='skip').grid(row=0, column=4)
        yellow_btn = Button(main_frm, command= lambda: self.set_color('yellow'), bg='yellow', width=w).grid(row=1, column=0)
        pink_btn = Button(main_frm, command= lambda: self.set_color('pink'), bg='pink', width=w).grid(row=1, column=1)
        cyan_btn = Button(main_frm, command= lambda: self.set_color('cyan'), bg='cyan', width=w).grid(row=1, column=2)
        white_btn = Button(main_frm, command= lambda: self.set_color('white'), bg='white', width=w).grid(row=1, column=3)
        reset_btn = Button(main_frm, command= lambda: self.set_color('gray'), bg='gray', width=w).grid(row=1, column=4)

        # override red cross

        for i in range(self.y):
            pix_btn_row = []
            for j in range(self.x):
                pix_btn_row.append(Button(main_frm, command= lambda i=i, j=j: self.change_pix(i,j), width=w, height=int(w/2), bg='gray'))
                pix_btn_row[j].grid(row=i+2, column=j)
            self.pix_btn.append(pix_btn_row)

        save_btn = Button(self.root, command= lambda: self.save_pix(), text='Save').grid(row=self.y+3, column=self.x+1)
        save_as_btn = Button(self.root, command= lambda: self.save_as_pix(), text= 'Save as').grid(row=self.y+4, column=self.x+1)
        partition_button = Button(self.root, command= lambda: self.partition(), text= 'Partition Mosaic').grid(row=self.y+5, column=self.x+1)

        dev = [info.device for info in list_ports.comports()]
        self.port = StringVar()
        select_port_box = Combobox(self.root, textvariable=self.port, values=dev, style='office.TCombobox').grid(row=self.y+6, column=self.x+1)
        send_btn = Button(self.root, command= lambda: self.send(), text='Send').grid(row=self.y+7, column=self.x+1)
        load_btn = Button(self.root, command=lambda: self.load_image(), text='Load').grid(row=self.y + 8, column=self.x + 1)

        self.root.mainloop()

    def set_color(self, color):
        self.cur_color = color

    def change_pix(self, i, j):
        red_cross = PhotoImage(file= r"emoji_test/red_x.png").subsample(8,8)
        if (self.cur_color == 'purple'):
            self.pix_btn[i][j].config(image= red_cross)
        self.pix_btn[i][j].config(bg=self.cur_color)

    def format_pix(self):
        self.pix_list = []
        if self.y%2==0:
            for i in range(self.y):
                for j in range(self.x):
                    if i%2==0:
                        clr = self.pix_btn[i][j].cget('bg')
                        if (clr == 'purple'):
                            continue
                        if (clr == 'gray'):
                            pix = 0
                        else:
                            pix = self.color_set.index(clr) - 1
                    else:
                        clr = self.pix_btn[i][self.x-1-j].cget('bg')
                        if (clr == 'purple'):
                            continue
                        if (clr == 'gray'):
                            pix = 0
                        else:
                            pix = self.color_set.index(clr) - 1
                    self.pix_list.append(pix)
        else:
            for i in range(self.y):
                for j in range(self.x):
                    if i%2==0:
                        clr = self.pix_btn[i][self.x-1-j].cget('bg')
                        if (clr == 'purple'):
                            continue
                        if (clr == 'gray'):
                            pix = 0
                        else:
                            pix = self.color_set.index(clr) - 1
                    else:
                        clr = self.pix_btn[i][j].cget('bg')
                        if (clr == 'purple'):
                            continue
                        if (clr == 'gray'):
                            pix = 0
                        else:
                            pix = self.color_set.index(clr) - 1
                    self.pix_list.append(pix)

    def save_pix(self):
        self.pix_list = []
        self.format_pix()
        if (self.save_filename is None):
            self.save_filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title="Choose filename")
        with open(self.save_filename, 'w'):
            np.savetxt(self.save_filename, self.pix_list, fmt='%d', delimiter=' ')
        print(self.port.get())

    def save_as_pix(self):
        self.pix_list = []
        self.format_pix()
        self.save_filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title="Choose filename")
        with open(self.save_filename, 'w'):
            np.savetxt(self.save_filename, self.pix_list, fmt='%d', delimiter=' ')

    def write_read(self, arduino, text):
        arduino.write(bytes(text, 'utf-8'))
        time.sleep(0.05)

    def send(self):
        arduino = serial.Serial(port=self.port.get(), baudrate=115200, timeout=.1)
        with open(self.save_filename) as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                self.write_read(arduino, line)
                time.sleep(0.1)
        num = ''
        with open(self.save_filename) as f:
            l = f.readline()
            while l:
                num += l.strip()
                l = f.readline()
        arduino.write(bytes(num[0,61], 'utf-8'))
        arduino.write(bytes('\n', 'utf-8'))
        time.sleep(5)
        arduino.write(bytes(num[61:121], 'utf-8'))
        time.sleep(0.05)   

        while True:
            time.sleep(0.05)
            data = arduino.readline()
            print(data) 

    def partition(self):
        # take self.pix_list and resize into a matrix of x by y
        self.format_pix()
        self.pix_mat = np.reshape(np.array(self.pix_list), (self.x, self.y))

        # split matrix by 5x5 groups (assume now perfectly divisible)
        x_num = int(self.x/5)
        y_num = int(self.y/5)
        total_windows = x_num*y_num

        self.save_filename = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text files', '*.txt')], title="Choose filename")
        for m in range(y_num):
            for n in range(x_num):
                partition = self.pix_mat[m*5:(m+1)*5, n*5:(n+1)*5]
                partition_list = np.ravel(partition)
                f_split = str.split(self.save_filename, sep=".")
                partition_filename = f_split[0] + "_" + str(m) + str(n) + "." + f_split[1]
                with open(partition_filename, 'w'):
                    np.savetxt(partition_filename, partition_list, fmt='%d', delimiter=' ')

    def load_image(self):
        self.load_filename = filedialog.askopenfilename(defaultextension=".txt")
        i = 0
        self.pix_mat = np.zeros((self.y, self.x), dtype=int)
        with open(self.load_filename, 'r', encoding='utf_8') as f:
            l = f.readline()
            while l:
                self.pix_mat[int(i/self.x), int(i%self.x)] = int(l.strip())
                l = f.readline()
                i += 1
        self.pix_list = list(np.ravel(self.pix_mat))

        # Now - want to set color and change pix
        for i, px in enumerate(self.pix_list):
            self.set_color(self.color_set[px+1])
            self.color_set[px+1]
            self.change_pix(int(i/self.x), int(i%self.x))

if __name__ == '__main__':
    test = GUI()

# 