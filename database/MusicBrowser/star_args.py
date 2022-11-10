# from __future__ import print_function  # python2 print
def average(*args):
    print(type(args))
    print("args is {}:".format(args))
    print("*args is:", *args)
    mean = 0
    for arg in args:
        mean += arg
    return mean / len(args)


def build_tuple(*args):
    return args


def average_length(*args):
    try:
        total_length = 0
        for word in args:
            total_length += len(word)
        return total_length / len(args)
    except ZeroDivisionError:
        print("Please include at least one word")


def smallest_number(*numbers):
    try:
        return min(numbers)
    except ValueError:
        print("Please include at least one number")


def reverse_words(*words):
    # for word in words[::-1]:
    for word in reversed(words):
        print(word, end=" ")


def unpacking(args):
    """lists and tuples can both be unpacked."""
    print(args)
    print(*args)


print(average(1, 2, 3, 4))
print(build_tuple("hello", "world", "Zhaoyang"))
print(average_length("hello", "lucky"))
print(smallest_number(1, 3, 5, 6, 10))
print(reverse_words("!", "beautiful", "so", "are", "You"))
print(unpacking((8, 8, 8, 8)))
print(unpacking([9, 9, 9, 9]))


