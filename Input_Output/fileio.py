# jabber = open("sample.txt", 'r')  # read only
#
# for line in jabber:
#     if 'jabberwock' in line.lower():
#         print(line, end='')  # 之所以后面的end=''，是因为文本中本来就有换行符号。
#
# jabber.close()
#

# 有with就不用close语句了，并且它也有捕捉错误的功能
# 会在错误前关闭file。
# with open("sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end='')

# with open("sample.txt") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt") as jabber:
#     lines = jabber.readlines()
# print(lines)  # lines输出的是一个list，你可以清楚地看到文本和换行符。
#
# for line in lines:
#     print(line, end='')

with open("sample.txt") as jabber:
    lines = jabber.readlines()
print(lines)  # readlines输出的是一个list，你可以清楚地看到文本和换行符。

for line in lines[::-1]:
    print(line, end='')

print(end="\n")

with open("sample.txt") as jabber:
    lines = jabber.read()
print(lines)   # read()输出一个string，所以你看到的是字母全部倒着排列的。

for line in lines[::-1]:
    print(line, end='')