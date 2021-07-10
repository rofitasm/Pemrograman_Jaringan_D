import socket
import json
import base64
import logging
import time
import datetime
from multiprocessing import Process, Pool

server_address = ('0.0.0.0', 6666)


def send_command(command_str=""):
    global server_address
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)
    logging.warning(f"connecting to {server_address}")
    try:
        logging.warning(f"sending message ")
        sock.sendall(command_str.encode())
        # Look for the response, waiting until socket is done (no more data)
        data_received = ""  # empty string
        while True:
            # socket does not receive all data at once, data comes in part, need to be concatenated at the end of process
            data = sock.recv(16)
            if data:
                # data is not empty, concat with previous content
                data_received += data.decode()
                if "\r\n\r\n" in data_received:
                    break
            else:
                # no more data, stop the process by break
                break
        # at this point, data_received (string) will contain all data coming from the socket
        # to be able to use the data_received as a dict, need to load it using json.loads()
        hasil = json.loads(data_received)
        logging.warning("data received from server:")
        return hasil
    except:
        logging.warning("error during data receiving")
        return False


def remote_list():
    command_str = f"LIST"
    hasil = send_command(command_str)
    if (hasil['status'] == 'OK'):
        print("daftar file : ")
        for nmfile in hasil['data']:
            print(f"- {nmfile}")
        return True
    else:
        print("Gagal")
        return False


def remote_get(filename="", i=""):
    command_str = f"GET {filename}"
    hasil = send_command(command_str)
    if (hasil['status'] == 'OK'):
        # proses file dalam bentuk base64 ke bentuk bytes
        namafile = hasil['data_namafile']

        s = namafile.split(".")
        img_name = s[0].strip()
        img_ext = s[1].strip()

        img_filename = img_name + '_' + str(i) + '.' + img_ext
        isifile = base64.b64decode(hasil['data_file'])
        fp = open(img_filename, 'wb+')
        fp.write(isifile)
        fp.close()
        return True
    else:
        print("Gagal")
        return False

def get_100image(image):
    texec = dict()
    status_task = dict()
    s = image.split(".")
    img_filename = s[0].strip()
    task_pool = Pool(processes=100)

    start_time = datetime.datetime.now()
    for i in range(1, 101):
        print(f"get {img_filename} {i}")
        texec[i] = task_pool.apply_async(func=remote_get, args=(image, i,))

    end_time = datetime.datetime.now()
    runtime = end_time - start_time
    print(f"total program berjalan {runtime} detik, program berjalan dari {start_time} hingga {end_time}")

if __name__ == '__main__':
    server_address = ('192.168.122.107', 6666)
    # remote_list()
    # remote_get('donalbebek.jpg')
    get_100image('pokijan.jpg')