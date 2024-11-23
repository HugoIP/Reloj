import serial,time

ard = serial.Serial('COM7',9600)
time.sleep(5)
ard.write(b'5')
ard.close()