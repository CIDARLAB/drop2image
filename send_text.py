import serial
from serial.tools import list_ports
import time


def send():
    dev = [info.device for info in list_ports.comports()]
    filename = '' # set your path here
    if filename == '':
        filename = input('Enter absolute path to the file: ')
    cnt = 0
    print('Choose the Serial port')
    for d in dev:
        print('\t[', cnt, ']: ', d, sep='')
        cnt += 1
    port = dev[int(input())]
    ser = serial.Serial(port, 9600)
    with open(filename, 'r', encoding='utf_8') as f:
        lines = f.readlines()

    for line in lines:
        ser.write(line.encode('utf-8'))
        time.sleep(0.5)
    ser.close()


if __name__ == '__main__':
    send()