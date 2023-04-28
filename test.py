import tkinter as tk
root = tk.Tk()
root.title("tk")
root.geometry("600x200+30+30")
import socket

ip = socket.gethostbyname(socket.gethostname())

def test():
    txtbox1.insert(tk.END, "http://" + ip + ":8888/pix.txt")

def copy_text():
    txt = txtbox1.get()
    print(txt)
    root.clipboard_clear()
    root.clipboard_append(txt)

button1 = tk.Button(root, text="display IP address", command=test)
button1.pack(expand=1)

txtbox1 = tk.Entry(font=("Meiryo UI",18), width=30)
txtbox1.pack(expand=1)



button3 = tk.Button(root, text="COPY", font=("Meiryo UI",18), command=copy_text)
button3.pack(expand=1)

root.mainloop()