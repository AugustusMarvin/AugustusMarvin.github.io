from random import randint
from time import time, sleep
from threading import Thread

def download_task(filename):
    print("启动下载进程\n")
    print("开始下载" + filename)
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print("下载" + filename + "耗费了" + str(time_to_download) + "s")

def main():
    start = time()
    p1 = Thread(target=download_task, args=('Python3.7', ))
    p1.start()
    p2 = Thread(target=download_task, args=('C++', ))
    p2.start()
    p1.join()
    p2.join()
    #download_task('Python3.7')
    #download_task('C++')
    end = time()
    print("总共耗费了" + str(end - start) + "s")

if __name__ == "__main__":
    main()