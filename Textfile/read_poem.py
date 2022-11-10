# # jabber = open('Jabberwocky.txt', 'r')
# #
# # for line in jabber:
# #     # print(line)
# #     # 结果的行与行之间有一行空，是因为txt文件，每一行最后都有一个换行符
# #     # 而print默认也是以换行结尾，所以为了避免结尾重复换行可改为：
# #     # print(line, end='')
# #     # print(len(line))
# #     # print(line.strip())   # str.strip()默认是去除前后端的whitespace
# #     print(line.rstrip())   # str.rstrip()默认是去除末端的whitespace， lstrip开端
# #
# #
# # jabber.close()
#
# with open('Jabberwocky.txt', 'r') as jabber:
#     # for line in jabber:
#     #     print(line.rstrip())
#     lines = jabber.readlines()  # returns a list containing strings of each line
#
# print(lines)
# print(lines[-1:])
# print(lines[::-1])
# for line in reversed(lines):
#     print(line, end='')

# with open('Jabberwocky.txt', 'r') as jabber:
#     text = jabber.read()  # return a string
#
# # print(text)
# for character in reversed(text):
#     print(character, end='')

# readline 没有read和readlines有用，因为就和普通的for line in jabber一样的功能。
with open("Jabberwocky.txt", 'r') as jabber:
    while True:
        line = jabber.readline().rstrip()
        print(line)
        if 'jubjub' in line.casefold():
            break

print('*' * 80)

with open('Jabberwocky.txt') as jabber:   # 不声明r，因为默认就是读。
    for line in jabber:
        print(line.rstrip())   # 再次强调string是immutable的，strip是制造了一个copy。
        if 'jubjub' in line.casefold():
            break