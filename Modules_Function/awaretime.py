import datetime
import pytz

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

print("Naive local time {}".format(local_time))
print("Naive UTC {}".format(utc_time))

# from naive -> aware time
# pytz.utc表示的是UTC这个时区对象, pytz.utc.zone是'UTC'string。
aware_local_time = pytz.utc.localize(utc_time).astimezone()  # astimezone方法里的tz默认是当前时区对象。
aware_utc_time = pytz.utc.localize(utc_time)

print("Aware local time{}, time zone{}".format(aware_local_time, aware_local_time.tzinfo))
print("Aware UTC {}, time zone{}".format(aware_utc_time, aware_utc_time.tzinfo))


gap_time = datetime.datetime(2015, 10, 25, 1, 30, 0, 0)
print(gap_time)
print(gap_time.timestamp())
# 1445725800.0, UTC输出是：1445733000
# 相差7200 / 3600 = 2小时
# timestamp return的是POSIX
# The Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number of seconds
# that have elapsed since January 1, 1970 (midnight UTC/GMT), not counting leap seconds
# (in ISO 8601: 1970-01-01T00:00:00Z).

s = 1445733000
t = s + (60 * 60)

gb = pytz.timezone("GB")
# dt1 = pytz.utc.localize(datetime.datetime.fromtimestamp(s)).astimezone(gb)
# dt2 = pytz.utc.localize(datetime.datetime.fromtimestamp(t)).astimezone(gb)
dt1 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(s)).astimezone(gb)
dt2 = pytz.utc.localize(datetime.datetime.utcfromtimestamp(t)).astimezone(gb)

print("{} seconds since the epoch is {}".format(s, dt1))
print("{} seconds since the epoch is {}".format(t, dt2))
# 二者的时间一样是因为，正好跨过了2015年10月的最后一个星期日的凌晨2点，转换为冬令时，时间往后拨动一小时
# 即减去一小时

# In the UK the clocks go forward 1 hour at 1am on the last Sunday in March,
# and back 1 hour at 2am on the last Sunday in October.
