import socket
import threading

SERVER_IP = '0.0.0.0'
SERVER_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT, 1)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST, 1)

sock.bind(("", SERVER_PORT))

num = 1

while True:
    data, addr = sock.recvfrom(65536)
    #buffer size 1024 * 64
    print(addr)
    print("diterima ", data)
    print("dikirim oleh " , addr)

    received_image = 'img_from_broadcast' + str(num) + ".png"
    num += 1
    file = open(received_image, 'wb')
    file.write(data)
    file.close()


