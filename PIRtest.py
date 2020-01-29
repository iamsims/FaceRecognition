import serial
ser=serial.Serial('COM3',9600)
while 1:
    a=ser.readline()
    if (int(a[0])==1)
    break;
