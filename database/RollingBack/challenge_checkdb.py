import sqlite3
import pytz
import pickle

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     # print(row)
#     # local_time = row[0]
#     # print("{}\t{}".format(local_time, type(local_time)))
#
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print("UTC time: {}\t\tLOCAL time: {}".format(utc_time, local_time))

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]
    # picked_zone = row[3]
    # zone = pickle.loads(picked_zone)

    # zone = pytz.timezone("CET")  # 可行
    # zone = pytz.timezone("ACDT")  # 不可行
    zone = pytz.timezone("Australia/Adelaide")
    local_time = pytz.utc.localize(utc_time).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))

print()

db.close()