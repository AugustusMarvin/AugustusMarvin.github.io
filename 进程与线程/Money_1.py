from time import sleep
from threading import Thread, Lock

class Account(object):
    def __init__(self):
        self._balabce = 0
        self._lock = Lock()
    def deposit(self, money):
        #先获取锁之后才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balabce + money
            sleep(0.01)
            self._balabce = new_balance
        finally:
            #在finally中执行释放锁的操作以保证正常异常锁都可以释放
            self._lock.release()
    @property
    def balance(self):
        return self._balabce
    #balance = property(set_balance)

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money
    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    for i in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print("账户余额为：" + str(account.balance))

if __name__ == '__main__':
    main()
