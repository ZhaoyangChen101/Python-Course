import timeit

setup = """\
gc.enable()
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}
"""
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}


# timeit的时候，两种选择：1）string，将代码使用"""包括起来，先保证程序是良好运行的，因为string不会有任何的错误提示，
# \表示的是继续，这样的话就不会有tab在里面。
# 2.将代码块形成一个function。
def nested_loop():
    result = []
    for loc in sorted(locations):
        exits_to_destination_1 = []
        for xit in exits:
            if loc in exits[xit].values():
                exits_to_destination_1.append((xit, locations[xit]))
        result.append(exits_to_destination_1)
    # print the result before returning
    for x in result:
        pass

    return result


def loop_comp():
    result = []
    for loc in sorted(locations):
        exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
        result.append(exits_to_destination_2)
        # print the result before returning
        for x in result:
            pass

    return result


def nested_comp():
    exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations)]
    # print the result before returning
    for x in exits_to_destination_3:
        pass

    return exits_to_destination_3


def nested_gen():
    exits_to_destination_3 = ([(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                              for loc in sorted(locations))
    # print the result before returning
    for x in exits_to_destination_3:
        pass

    return exits_to_destination_3


print(nested_loop())
print(loop_comp())
print(nested_comp())

# global=global()只适用于3.5及以上。
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)   # 使得locations和exits的变量能被代码板块使用
result_1 = timeit.timeit(nested_loop, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
result_2 = timeit.timeit(loop_comp, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
result_3 = timeit.timeit(nested_comp, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
result_4 = timeit.timeit(nested_gen, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
print("Nested loop:\t{}".format(result_1))
print("Loop and comp:\t{}".format(result_2))
print("Nested comp:\t{}".format(result_3))
print("Nested gen:\t{}".format(result_4))

