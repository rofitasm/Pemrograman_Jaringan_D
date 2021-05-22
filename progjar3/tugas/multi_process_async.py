from library import download_then_broadcast_pict, get_url_list
import time
import datetime
from multiprocessing import Process, Pool

TARGET_IP = '192.168.122.0'
TARGET_PORT = 5005

def download_then_broadcast_all():
    texec = dict()
    urls = get_url_list()
    status_task = dict()
    task_pool = Pool(processes=2) #2 task yang dapat dikerjakan secara simultan, dapat diset sesuai jumlah core
    catat_awal = datetime.datetime.now()
    for k in urls:
        print(f"download dan broadcast {urls[k]}")
        #bagian ini merupakan bagian yang mengistruksikan eksekusi fungsi download dan broadcast gambar secara multiprocess
        texec[k] = task_pool.apply_async(func=download_then_broadcast_pict, args=(urls[k], True, TARGET_IP, TARGET_PORT))

    #setelah menyelesaikan tugasnya, dikembalikan ke main process dengan mengambil hasilnya dengan get
    for k in urls:
        status_task[k]=texec[k].get(timeout=20)

    catat_akhir = datetime.datetime.now()
    selesai = catat_akhir - catat_awal
    print(f"Waktu TOTAL yang dibutuhkan {selesai} detik {catat_awal} s/d {catat_akhir}")
    print("status TASK")
    print(status_task)


#fungsi download_gambar akan dijalankan secara multi process

if __name__=='__main__':
    download_then_broadcast_all()
