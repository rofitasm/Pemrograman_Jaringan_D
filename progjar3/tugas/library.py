import logging
import requests
import os
import time
import datetime
import socket


def get_url_list():
    urls = dict()
    # urls['bitcoin_logo']='https://1000logos.net/wp-content/uploads/2018/04/Bitcoin-Logo.png'
    # urls['biatcoin_logo']='https://1000logos.net/wp-content/uploads/2018/04/Bitcoin-Logo.png'
    # urls['bitacoin_logo']='https://1000logos.net/wp-content/uploads/2018/04/Bitcoin-Logo.png'
    # urls['adidas_logo']='https://www.nretnil.com/logo/adidas-flower-logo-200.jpg'
    # urls['youtube_logo']='https://www.seekpng.com/png/small/3-30986_youtube-play-button-png-youtube-logo-round-png.png'
    urls['discord_logo']='https://png.pngitem.com/pimgs/s/362-3629253_downloads-the-tz-beautiful-transparent-background-discord-logo.png'
    urls['google_logo']='https://media.glassdoor.com/sqll/9079/google-squarelogo-1441130773284.png'
    return urls


def download_then_broadcast_pict(url=None, tuliskefile=False, ip_target=None, port_target=None):
    waktu_awal = datetime.datetime.now()
    if (url is None):
        return False
    ff = requests.get(url)
    time.sleep(2) #untuk simulasi, diberi tambahan delay 2 detik

    #download gambar
    namafile = os.path.basename(url)
    if (tuliskefile):
        fp = open(f"{namafile}","wb")
        fp.write(ff.content)
        fp.close()

    if (ip_target is None):
        return False
    #broadcast gambar
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    print(f"broadcast file {namafile}")
    image_file = open(f"{namafile}","rb")
    image_bytes = image_file.read()
    sock.sendto(image_bytes, (ip_target, port_target))

    #waktu yang digunakan
    waktu_process = datetime.datetime.now() - waktu_awal
    waktu_akhir =datetime.datetime.now()
    logging.warning(f"download dan broadcast {namafile} dalam waktu {waktu_process} {waktu_awal} s/d {waktu_akhir}")
    return waktu_process
