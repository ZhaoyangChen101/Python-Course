# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as city_file:
#     for city in cities:
#         # print(city, file=city_file, flush=True) # flush=True能够使得文件立刻被写
#         print(city, file=city_file)
#
#
#

# cities = []
# #
# # with open("cities.txt", 'r') as city_file:
# #     for city in city_file:
# #         cities.append(city.strip('\n'))   # string.strip()默认去掉前后空格，有的话就去掉前后输入的字符。
# #
# # print(cities)
# # for city in cities:
# #     # print(city, end='')
# #     print(city) # 有strip之后，\n被去掉了，就不需要这里的end了。

# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "pulling the rug"), (2, "psycho"), (3, "mayhem"), (4, "kentish"))
#
# with open("imelda3.txt", "w") as imelda_file:
#     print(imelda, file=imelda_file)
    # imelda是一个tuple，但是写进file之后，是string类型的了
    # 在read it back的时候就比较难读取给一个tuple variable。
    # 但是python又一个eval的function，会evaluate输入的string，然后
    # 在这种情况下，可以得到tuple。

with open("imelda3.txt", "r") as imelda_file:
    contents = imelda_file.readline()
    # 复习：readline()读一行，输出string类型
    # readlines()读所有行，输出list类型
    # read()读所有行，输出string类型。

imelda = eval(contents)
# 此处eval就将string类型，实则tuple输出为tuple
# 还原了其本来面目
# 但是用eval来处理data outside the program不太好，因为可能会导致文件的内容被改变。
# 并且文件里面可能有的damaging instructions，your program would happily execute them.
# 这个好可怕哦！
# 小结：it's really important to design programs with security in mind
# and not to leave vulnerabilities in your code.

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
