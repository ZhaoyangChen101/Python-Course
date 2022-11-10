import sqlite3
# import pytz

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     # print(row)
#     # local_time = row[0]
#     # print("{}\t{}".format(local_time, type(local_time)))
#
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print("UTC time: {}\t\tLOCAL time: {}".format(utc_time, local_time))
print("VIEW of localhistory with local time:")
for row in db.execute("SELECT * FROM localhistory"):
    print(row, type(row[0]))
print()

print("strftime func:")
for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', history.time, 'localtime') AS localtime,"
                      " history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

print()

print("datetime func:")
# truncates the second fractional parts so it is not as accurate as strftime with format specified
for row in db.execute("SELECT datetime(history.time, 'localtime') AS localtime,"
                      " history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

print()
print("Whether integer values are output in String?")  # int
# 发现如果只是单独一个值，输出也是tuple也
# for row in db.execute("SELECT balance FROM accounts"):
#     print(row, type(row[0]))
# 为了解决上面的问题，可以通过下面添加一个,来解决！！！而不是`,_`——这个会报错。
for row, in db.execute("SELECT balance FROM accounts"):
    print(row, type(row))

db.close()