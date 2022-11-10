# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191, 350, 360]
# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]
# a list that does not have values we want
# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#         1601, 1701, 1831, 1851, 1871, 1881, 1911]
data = []
# del data[0:2]  # 这个del好神奇，都没有括号啥的。
# print(data)
# del data[14:]
# print(data)

min_valid = 100
max_valid = 200
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index] # 反思：不可对iterable的长度进行更改。
#
# print(data)

# process the low values in the list, 下方代码只适合于ordered list
stop = 0
for index, value in enumerate(data):
    if value >= min_valid:
        stop = index
        break
print(stop)  # for debugging
del data[:stop]  # up to but not including stop
print(data)

# process the high value in the list
start = 0
for index in range((len(data)) - 1, -1, -1):
    # print(index)
    if data[index] <= max_valid:
        # we have the index of the last item to keep.
        # set the 'start' to the position of the first
        # item to delete, which is 1 after index.
        start = index + 1
        break
print(start)  # for debugging
del data[start:]
print(data)


