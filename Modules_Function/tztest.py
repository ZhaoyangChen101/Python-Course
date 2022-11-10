import pytz
import datetime

country = "Europe/Moscow"

tz_to_display = pytz.timezone(country)
local_time = datetime.datetime.now(tz=tz_to_display)
print("The time in {} is {}".format(country, local_time))
print("UTC is {}".format(datetime.datetime.utcnow()))

# for x in pytz.all_timezones:
#     print(x)
#
# for x in sorted(pytz.country_names):
#     print(x + ": " + pytz.country_names[x])

# for x in sorted(pytz.country_names):
#     # print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones[x]))
#     # timezones不全，比如没有BV对应的timezone，所以改为get，找不到就返回None。
#
#     print("{}: {}: {}".format(x, pytz.country_names[x], pytz.country_timezones.get(x)))
#     # BV: Bouvet Island: None

for x in sorted(pytz.country_names):
    print("{}: {}".format(x, pytz.country_names[x], end=": "))
    if x in pytz.country_timezones:
        for zone in sorted(pytz.country_timezones[x]):
            tz_to_display = pytz.timezone(zone)
            local_time = datetime.datetime.now(tz=tz_to_display)
            print("\t\t{}:{}".format(zone, local_time))
    else:
        print("\t\tNo time zone defined")

# 留个笔记
# for x in sorted(pytz.country_names):
#     if x in pytz.country_timezones:
#         print(
#             "{}:{}\n\tTime Zone:{}"
#             .format(x, pytz.country_names[x], type(pytz.timezone(pytz.country_timezones[x][0]))))
# type是pytz.tzfile.xxx
# ZW:Zimbabwe
# 	Time Zone:<class 'pytz.tzfile.Africa/Harare'>
