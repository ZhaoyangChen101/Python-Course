import sqlite3

db = sqlite3.connect("contacts.sqlite")
# print(type(db))  # sqlite3.Connection
# print(type(db.execute("SELECT * FROM contacts")))  # sqlite3.Cursor

# cursor = db.cursor()
# cursor.execute("SELECT * FROM contacts")
# 也就是说可以db.cursor().execute(...)，也可以直接db.execute(...)
# 不比担心非要创建一个cursor对象。

# cursor有一个属性，就是rowcount，来记录修改的数据数量。
new_email = "emailupdate@update.com"
phone = input("Please enter the phone number: ")
# update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE contacts.phone = 1234"
# update_sql = "UPDATE contacts SET email = '{}' WHERE contacts.phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE contacts.phone = ?"
print(update_sql)

update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, phone))  # execute只执行一条语句，和update_sql里面有问号的时候搭配使用。
# update_cursor.execute(update_sql)  # execute只执行一条语句
# update_cursor.executescript(update_sql)  # executescript是执行多条语句，注意：此时的rowcount会返回不正确的值。
print("{} rows updated".format(update_cursor.rowcount))
# cursor对象没有commit方法，但是有connect的reference。

print()
print("are connections the same: {}".format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()
# 在contacts的数据commit之后，就可以了。
for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

# db.commit()  # 最好就是在修改完数据满意后，就及时使用connect的commit
db.close()
