from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 500  # начальный баланс в банке
        self.oplimit = 100  # лимит операций
        self.lock = Lock()
        
        self.lock.acquire()  # устанавливает начальное состояние объекта класса при инициализации в ЗАБЛОКИРОВАНО
    
    def deposit(self):
        depo_op = 0  # счётчик операций
        while depo_op < self.oplimit:  # проверка на лимит операций
            if self.lock.locked():
                self.lock.release()
            depo_sum = randint(50, 500)
            self.balance += depo_sum
            depo_op += 1
            print(f'Пополнение: {depo_sum}. Баланс: {self.balance}.\n depo_op is {depo_op}')
            sleep(0.001)
    
    def take(self):
        take_op = 0  # счётчик операций
        take_spam = 0  # счётчик "спама" иногда возникает вероятность псевдо-зацикливания
        while take_op < self.oplimit and take_spam < 1000:  # проверка на лимит операций
            take_sum = randint(50, 500)
            print(f'Запрос на {take_sum}')
            if take_sum <= self.balance:
                self.balance -= take_sum
                take_op += 1
                print(f'Снятие: {take_sum}. Баланс: {self.balance}.\n take_op is {take_op}')
            else:
                print(f'Запрос отклонён, недостаточно средств.')
                take_spam += 1  # спасение от иногда возникающего псевдо-зацикливания
            sleep(0.001)
        self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

# проработать варианты ещё от зацикливания в операции снятия.... иногда это происходит
# как вариант переменная СПАМ , но возможно тут что-то другое