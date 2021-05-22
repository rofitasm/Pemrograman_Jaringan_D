from library import download_then_broadcast_pict, get_url_list
import time
import datetime
from multiprocessing import Process

TARGET_IP = '192.168.122.0'
TARGET_PORT = 5005


def download_broadcast_semua():
    texec = dict()
    urls = get_url_list()
    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"download dan broadcast {urls[k]}")
        waktu = time.time()
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download dan broadcast gambar secara multiprocess
        texec[k] = Process(target=download_then_broadcast_pict, args=(urls[k], True, TARGET_IP, TARGET_PORT))
        texec[k].start()
    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan join
    for k in urls:
        texec[k].join()
    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
#fungsi download_gambar akan dijalankan secara multi process

if __name__=='__main__':
    download_broadcast_semua()
