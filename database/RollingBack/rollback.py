import sqlite3
import pytz
import datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
db.execute("CREATE TABLE IF NOT EXISTS accounts (name TEXT PRIMARY KEY NOT NULL, balance INTEGER NOT NULL)")
db.execute("CREATE TABLE IF NOT EXISTS history (time TIMESTAMP NOT NULL, "
           "account TEXT NOT NULL, amount INTEGER NOT NULL, PRIMARY KEY (time, account))")
db.execute("CREATE VIEW IF NOT EXISTS localhistory AS"
           " SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
           " history.account, history.amount FROM history ORDER BY history.time")


# opt + cmd + L -> reformat


class Account(object):

    @staticmethod
    def _current_time():
        # return 1  # 导致composite key(time, account)不一致，就会出现错误
        return pytz.utc.localize(datetime.datetime.utcnow())

        # local_time = pytz.utc.localize(datetime.datetime.utcnow())
        # return local_time.astimezone()

    def __init__(self, name: str, opening_balance: int = 0):
        cursor = db.execute("SELECT name, balance FROM accounts WHERE (name = ?)", (name,))
        row = cursor.fetchone()

        if row:
            self.name, self._balance = row
            print("Retrieved record for {}. ".format(self.name), end='')
        else:
            self.name = name
            self._balance = opening_balance
            cursor.execute("INSERT INTO accounts VALUES(?, ?)", (name, opening_balance))
            cursor.connection.commit()
            print("Account created for {}. ".format(self, name), end='')
        self.show_balance()

    def _save_update(self, amount):
        new_balance = self._balance + amount
        deposit_time = Account._current_time()
        # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
        # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        # db.commit()
        # self._balance = new_balance
        try:
            db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
        except sqlite3.Error:
            db.rollback()
            # 因为insert出现错误时，update语句是执行了的，
            # rollback的作用就是这个尚未被保存却被执行了的update语句也被取消执行。
            # 普遍地来说，就是在错误语句之前执行的语句都撤销，即整个try block的语句。
            #
            # pass
            # 疑问？反正此处update语句（崩溃语句前一条）并未被commit（保存），为何还要rollback呢？
            # 懂了，当此处删除rollback，那么update就一直pending。老师的例子是，删除了表中的terryG再次运行，发现john的存款是1980而非2010
            # 就是因为三个deposit和最后一个withdraw对于表的操作会覆盖，当withdraw完了之后，就进行了terryG对象的建立，插入数据
            # 这个插入之后，进行了cursor.connection.commit()即db.commit()，就导致了withdraw的update操作成功，减少了30。
            # 所以必须要进行哪怕try中有语句出现错误没有commit之前的操作，也要rollback这些语句，
            # 以避免其他的操作带来的commit导致最后一次pending的update操作进行成功。
        else:
            # commit放在更新balance前面是因为如果commit出现了问题，balance不用进行存储
            db.commit()
            self._balance = new_balance  # 虽然放在try里面也可行，但是不是好的习惯，因为最好try里面就只放想要保护会出问题的代码
        # finally:
        #     db.commit()

    def deposit(self, amount: int) -> float:
        if amount > 0.0:
            # # self._balance += amount
            # new_balance = self._balance + amount
            # deposit_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (deposit_time, self.name, amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(amount)
            print("{:.2f} deposited".format(amount / 100))
        return self._balance / 100

    def withdraw(self, amount: int) -> float:
        if 0 < amount <= self._balance:
            # # self._balance -= amount
            # new_balance = self._balance - amount
            # withdraw_time = Account._current_time()
            # db.execute("UPDATE accounts SET balance = ? WHERE (name = ?)", (new_balance, self.name))
            # db.execute("INSERT INTO history VALUES(?, ?, ?)", (withdraw_time, self.name, -amount))
            # db.commit()
            # self._balance = new_balance
            self._save_update(-amount)
            print("{:.2f} withdrawn".format(amount / 100))
            return amount / 100
        else:
            print("The amount must be greater than zero and no more than your account balance.")
            return 0.0

    def show_balance(self):
        print("Balance on account {} is {:.2f}".format(self.name, self._balance / 100))


if __name__ == "__main__":
    john = Account("John")
    john.deposit(1010)
    john.deposit(10)
    john.deposit(10)
    john.withdraw(30)
    john.withdraw(0)
    john.show_balance()

    terry = Account("TerryJ")
    graham = Account("Graham", 9000)
    eric = Account("Eric", 7000)
    michael = Account("Michael")
    terryG = Account("TerryG")

    db.close()
