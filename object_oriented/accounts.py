import datetime
import pytz


class AccountNumber:  # class name-camel case
    """Simple account class with balance"""

    # self parameter isn't used in this method
    # so that Pycharm indicates that this method may be static.
    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance
        # 发现了__是为了避免subclass的时候名字的混淆。
        # 在对象.__dict__打印的时候，这个__name和__balance前面会出现类名，而_transaction_list没有前缀类名。
        self._transaction_list = [(AccountNumber._current_time(), balance)]
        print("Account created for " + self.__name)
        self.show_balance()

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.show_balance()
            self._transaction_list.append((AccountNumber._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            self._transaction_list.append((AccountNumber._current_time(), -amount))
        else:
            print("The amount should be more than 0 and no more than your account balance. ")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transactions(self):
        for date, amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposited"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} (local time was {}".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    tim = AccountNumber("tim", 0)
    tim.show_balance()

    tim.deposit(1000)
    # tim.show_balance()
    tim.withdraw(500)
    # tim.show_balance()

    tim.withdraw(2000)

    tim.show_transactions()

    steph = AccountNumber("Steph", 800)
    steph.__balance = 200
    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()
    print(steph.__dict__)
    # steph._Account__balance = 40
    # 也是可以改的，但是最好不要，因为本来name mangling的作用就是private的作用，
    # 不允许在类外进行更改，所以__balance被name mangling为_Account__balance，使得其初始值不能更改
    # 当在类外想要对__balance进行更改时候，由于和类内的被mangle的属性名称不同，所以创建了新的属性，
    # 从而不能达到更改_Account__balance（原__balance）的作用。
    # 最后一点comment是，名称后面如果有两个下划线，则不会被mangle，比如__init__.
    # 小结：name mangling 条件：前面两根下划线，后面不超过一根