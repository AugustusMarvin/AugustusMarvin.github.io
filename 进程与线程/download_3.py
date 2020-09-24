from random import randint
from time import time, sleep
from threading import Thread

class Download_task(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename
    def run(self):
        print("启动下载进程\n")
        print("开始下载" + self._filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print("下载" + self._filename + "耗费了" + str(time_to_download) + "s")

def main():
    start = time()
    p1 = Download_task('Python3.7')
    p1.start()
    p2 = Download_task('C++')
    p2.start()
    p1.join()
    p2.join()
    #download_task('Python3.7')
    #download_task('C++')
    end = time()
    print("总共耗费了" + str(end - start) + "s")

if __name__ == "__main__":
    main()