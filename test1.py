import serial
import time
arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
# def write_read(x):
#     arduino.write(bytes(x, 'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data
# while True:
#     # num = input("Enter a number: ") # Taking input from user
#     num = '1111110000011111100000111111000001111110000011111100000111111000001111110000011111100000111111000001111110000011111100000'
#     value = write_read(num)
#     print(value) # printing the value
time.sleep(2)
num = '1111110000011111100000111111000001111110000011111100000111111000001111110000011111100000111111000001111110000011111100000'
arduino.write(bytes(num[0:60], 'utf-8'))
arduino.write(bytes('\n', 'utf-8'))
time.sleep(5)
arduino.write(bytes(num[60:120], 'utf-8'))
print('sent part2')
time.sleep(0.05)

while True:
    time.sleep(0.05)
    data = arduino.readline()
    print(data)

