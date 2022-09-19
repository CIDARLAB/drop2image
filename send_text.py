import serial
from serial.tools import list_ports
import time


def send():
    dev = [info.device for info in list_ports.comports()]
    filename = '/Users/kaedekawata/Documents/STEM_Pathway/droplets/emoji_test/pix.txt' # set your path here
    if filename == '':
        filename = input('Enter absolute path to the file: ')
    cnt = 0
    print('Choose the Serial port')
    for d in dev:
        print('\t[', cnt, ']: ', d, sep='')
        cnt += 1
    port = dev[int(input())]
    ser = serial.Serial(port, 115200, timeout=.1)
    with open(filename, 'r', encoding='utf_8') as f:
        lines = [x.strip() for x in f.readlines()]

    for line in lines:
        ser.write(bytes(line, 'utf-8'))
        print(line)
        time.sleep(1)
    ser.close()
    print("Done")


if __name__ == '__main__':
    send()
