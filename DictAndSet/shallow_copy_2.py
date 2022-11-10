lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkle"]
teddy_list = ["cuddly", "stuffed"]
# animals = {
#     "lion": ["scary", "big", "cat"],
#     "elephant": ["big", "grey", "wrinkle"],
#     "teddy": ["cuddly", "stuffed"],
# }

animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}

# things = animals 后面在更改了animal的teddy对应的值后的print(things[])是toy
# things = animals.copy()
# 对比：
things = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}
# 回忆：list也有copy方法，不过，副本和原本做改变都是独立于彼此的。
# 对比字典的copy，二者都是一样的，一方做出了改变，另一方也跟着改变，那有什么意思呢？
# 上一行的说法并不对，这不是copy的问题，dict和list的问题。
# 这个list不是存储在字典里的，而是存储在memory的某个位置，字典里的value是一个reference而已。
# animals["teddy"] = "toy"
# 此处是shallow copy

# print(things["teddy"])
# print(animals["teddy"])

print()

# things["teddy"].append("toy")
teddy_list.append("toy")
animals["teddy"].append("added via `animals`")
things["teddy"].append("added via 'things`")
print(things["teddy"])
print(animals["teddy"])

print()
animals["teddy"].append("eureka")
print(things["teddy"])
print(animals["teddy"])