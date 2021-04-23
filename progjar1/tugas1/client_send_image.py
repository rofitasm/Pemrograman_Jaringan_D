import sys
import socket

alpine = 1
ip_arr = ['192.168.122.13', '192.168.122.34']
for i in ip_arr:
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Connect the socket to the port where the server is listening
  server_address = (i, 3000)
  print(f"connecting to {server_address}")
  sock.connect(server_address)


  try:
    # Send image
    image = 'ikigai.png'
    image_file = open(image, 'rb')
    image_bytes = image_file.read()
    print(f"sending {image}")
    sock.sendall(image_bytes)
    # Look for the response
    amount_received = 0
    amount_expected = len(image_bytes)
    received_image = 'received-by-alpine-' + str(alpine) + '.png'
    alpine+=1
    with open(received_image, 'wb') as file:
        while amount_received < amount_expected:
            data = sock.recv(32)
            amount_received += len(data)
            if not data:
                break
            file.write(data)
  finally:
    print("closing")
    sock.close()
