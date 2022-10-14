import serial
import time
arduino = serial.Serial(port='COM4', baudrate=115200, timeout=.1)
arduino.stopbits=2

time.sleep(2)
num = ''
with open("emoji_test/pix_art_gui.txt") as f:
    l = f.readline()
    while l:
        num += l.strip()
        l = f.readline()
# open file and read data into string
arduino.write(bytes(num[0:61], 'utf-8'))
arduino.write(bytes('\n', 'utf-8'))
time.sleep(5)
arduino.write(bytes(num[61:121], 'utf-8'))
time.sleep(0.05)

while True:
    time.sleep(0.05)
    data = arduino.readline()
    print(data)

# what type of data you want to display
# how much delays in one loop -> 2 ms
# sorting 150 ms
# voltage in float