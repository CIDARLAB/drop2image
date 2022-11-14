import serial
from serial.tools import list_ports
import time


def send():
    dev = [info.device for info in list_ports.comports()]
    filename = 'emoji_test/pix_art_gui.txt' # set your path here
    if filename == '':
        filename = input('Enter the path to the file: ')
    cnt = 0
    print('Choose the Serial port')
    for d in dev:
        print('\t[', cnt, ']: ', d, sep='')
        cnt += 1
    port = dev[int(input())]
    num = ''
    ser = serial.Serial(port, 115200, timeout=.1)
    with open(filename, 'r', encoding='utf_8') as f:
        l = f.readline()
        while l:
            num += l.strip()
            l = f.readline()
    time.sleep(2)
    ser.write(bytes(num[0:25], 'utf-8'))
    print('sent')
    # time.sleep(5)
    # ser.write(bytes(num[61:121], 'utf-8'))
    time.sleep(0.05)

    while True:
        time.sleep(0.05)
        data = ser.readline()
        print(data)


if __name__ == '__main__':
    send()
