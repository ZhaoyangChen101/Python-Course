import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range is returning {}".format(start))
        yield start
        start += 1


# _ = input("line 12")
big_range = range(5)   # range是iterable
# big_range = my_range(5)   # my_range是iterator
# _ = input("line 16")

# print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big range
big_list = []

# _ = input("line 23")
for val in big_range:
    # _ = input("line 25 - inside loop")
    big_list.append(val)

# big_list = list(big_range)
print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again ... or not")
for i in big_range:
    print("i is {}".format(i))
# big_range = my_range(5)时nothing happens
# big_range = range(5)时，正常运行。
print("=" * 30)

# for i in my_range(5):
#     print("i is {}".format(i))
print(type(range(45)))
print(type(my_range(45)))
