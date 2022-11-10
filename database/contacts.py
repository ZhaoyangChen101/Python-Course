import sqlite3

# sqlite不在意数据库名称，只要是个file name就行
# 不过这里后缀名名为.sqlite
# 原来它connect了就是创建了。
db = sqlite3.connect("contacts.sqlite")
db.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT, phone INTEGER, email TEXT)")
db.execute("INSERT INTO contacts (name, phone, email) VALUES('Tim', 6545678, 'tim@email.com')")
db.execute("INSERT INTO contacts VALUES ('Brian', 1234, 'brian@myemail.com')")

cursor = db.cursor()
cursor.execute("SELECT * FROM contacts")
# 此处的cursor是generator, which works by generating the next value
# each time it's used in python.
# 如果是list，就得先存储好所有的records，那memory runs out quickly.
# cursor here does not keep track of previous records.

# print(cursor.fetchall())  # 输出所有值为一个list。

print(cursor.fetchone())  # first record
print(cursor.fetchone())  # second
print(cursor.fetchone())  # 返回None，而不是什么都不返回。

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()
db.commit()  # 保证修改是永久的，如果没有这套语句，则数据库关闭时，修改的数据就会失效。
db.close()
