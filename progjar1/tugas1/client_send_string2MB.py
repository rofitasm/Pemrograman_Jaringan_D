import sys
import socket
import string
import random

ip_arr = ['192.168.122.33', '192.168.122.156']
for i in ip_arr:
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect the socket to the port where the server is listening
  server_address = (i, 3000)
  print(f"connecting to {server_address}")
  sock.connect(server_address)

  try:
    # Send data
    message = ''.join(random.choices(string.ascii_letters, k = 2000000))
    print(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    message2 = ''
    while amount_received < amount_expected:
        data = sock.recv(32)
        amount_received += len(data)
        print(f"{data}")
        message2 += data.decode("utf-8")
  finally:
      print(f"{message2}")
      print("closing")
      sock.close()
