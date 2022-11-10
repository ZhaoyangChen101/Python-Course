# import time
#
# print(time.gmtime(0))
#
# # print(time.localtime())
# print(time.localtime(time.time()))
#
# print(time.time())  # the number of seconds since epoch
#
# time_here = time.localtime()
# print(time_here)
# print("Year:", time_here[0], time_here.tm_year)
# print("Month:", time_here[1], time_here.tm_mon)
# print("Year:", time_here[2], time_here.tm_mday)
#

import time
# three funcs to measure elapsed time
# from time import time as my_timer  # for real time
# from time import perf_counter as my_timer  # best choice for elapsed time
# from time import monotonic as my_timer

from time import process_time as my_timer  # time spent on CPU
import random

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")

end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))

print("Your reaction time was {} seconds.".format(end_time - start_time))
