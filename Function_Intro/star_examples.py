numbers = (0, 1, 2, 3, 4, 5)


# print(numbers)
# print(numbers, sep=";")
# print(*numbers, sep=";")   #* unpacks the tuple
# print(0, 1, 2, 3, 4, 5, sep=";")


def test_star(*args):
    print(args)
    print(*args)  # unpacking
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5)

print()
test_star()


