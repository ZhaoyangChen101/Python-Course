import sqlite3

db = sqlite3.connect("contacts.sqlite")

name_to_look = input("Please enter name you want to look up for: ")
# lookup_sql = "SELECT * FROM contacts WHERE name = ?"

# sqlite_master能打印出SQLite的系统表
# for row in db.execute("SELECT * FROM sqlite_master"):
# for row in db.execute("SELECT * FROM contacts WHERE name = ?", (name_to_look,)):
for row in db.execute("SELECT * FROM contacts WHERE name LIKE ?", (name_to_look,)):
    print(row)

db.close()
