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

print("nested for loops")
print("----------------")
# timeit的时候，两种选择：1）string，将代码使用"""包括起来，先保证程序是良好运行的，因为string不会有任何的错误提示，
# \表示的是继续，这样的话就不会有tab在里面。
# 2.将代码块形成一个function。
nested_loop = """\
for loc in sorted(locations):
    exits_to_destination_1 = []
    for xit in exits:
        if loc in exits[xit].values():
            exits_to_destination_1.append((xit, locations[xit]))
    print("Locations leading to {}:".format(loc), end="\t")
    print(exits_to_destination_1)
"""
print()

print("List comprehension inside a for loop")
print("------------------------------------")
loop_comp = """\
for loc in sorted(locations):
    exits_to_destination_2 = [(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
    print("Locations leading to {}:".format(loc), end="\t")
    print(exits_to_destination_2)
"""
print()

print("Nested comprehension")
print("--------------------")
nested_comp = """\
exits_to_destination_3 = [[(xit, locations[xit]) for xit in exits if loc in exits[xit].values()]
                          for loc in sorted(locations)]
# enumerate(sequence)，提供index和值。感觉还是蛮有用的。
for index, loc in enumerate(exits_to_destination_3):
    print("Locations leading to {}:".format(index), end="\t")
    print(loc)
"""

# global=global()只适用于3.5及以上。
# result_1 = timeit.timeit(nested_loop, globals=globals(), number=1000)   # 使得locations和exits的变量能被代码板块使用
result_1 = timeit.timeit(nested_loop, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
result_2 = timeit.timeit(loop_comp, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
result_3 = timeit.timeit(nested_comp, setup, number=10000)   # 将变量设置为setup string类型，相当于该代码板块可以使用setup变量
print("Nested loop:\t{}".format(result_1))
print("Loop and comp:\t{}".format(result_2))
print("Nested comp:\t{}".format(result_3))
