import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)

time.sleep(2)
num = '1111110000011111100000111111000001111110000011111100000111111000001111110000011111100000111111000001111110000011111100000'
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

# 
# what type of data you want to display
# how much delays in one loop -> 2 ms
# sorting 150 ms
# voltage in float