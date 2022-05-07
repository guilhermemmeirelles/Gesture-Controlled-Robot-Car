# RECEIVER
import socket
import serial
from subprocess import call

dev = serial.Serial("/dev/ttyUSB0", baudrate=19200)


ip = "192.168.1.255"
port = 5005
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind((ip, port))

print(f'Start listening to {ip}:{port}')

while True:
    data, addr = sock.recvfrom(1024) # buffer
    if(data != b'9'):
        print(f"received message: {data}")
        dev.write(data)
    else:
        print(f"received message: {data}")
        dev.write(data)
        call("sudo shutdown now", shell=True)
    


