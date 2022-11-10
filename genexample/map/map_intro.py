import timeit

text = "what have the romans even done for us"


def comp_caps():
    capitals = [char.upper() for char in text]
    return capitals


# use map
def map_caps():
    map_capitals = list(map(str.upper, text))
    return map_capitals


def comp_words():
    words = [word.upper() for word in text.split(' ')]
    return words


# use map
def map_words():
    map_w = list(map(str.upper, text.split(' ')))
    return map_w

# print("the type of map is: {}".format(map(str.upper, text)))  # type is map -> map也是iterable。
# print(map(str.upper, text))  # map对象。
# for x in map(str.upper, text.split(' ')):
#     print(x)


# # timeit 自己的方式
# result_1 = timeit.timeit(comp_caps, globals=globals(), number=10000)
# result_2 = timeit.timeit(map_caps, globals=globals(), number=10000)
# result_3 = timeit.timeit(comp_words, globals=globals(), number=10000)
# result_4 = timeit.timeit(map_words, globals=globals(), number=10000)
# print(result_1)
# print(result_2)
# print(result_3)
# print(result_4)

if __name__ == "__main__":
    # 先测试函数是否能成功运行
    print(comp_caps())
    print(map_caps())
    print(comp_words())
    print(map_words())

    # print(timeit.timeit("comp_caps()", setup="from __main__ import comp_caps", number=100000))
    # print(timeit.timeit("map_caps()", setup="from __main__ import map_caps", number=100000))
    # print(timeit.timeit("comp_words()", setup="from __main__ import comp_words", number=100000))
    # print(timeit.timeit("map_words()", setup="from __main__ import map_words", number=100000))
    print(timeit.timeit(comp_caps, number=100000))
    print(timeit.timeit(map_caps, number=100000))
    print(timeit.timeit(comp_words, number=100000))
    print(timeit.timeit(map_words, number=100000))
    # 小结：调用函数的时候（"func()"），需要用""，就必须要setup；如果是函数的reference，setup不用import或者变量设置。
