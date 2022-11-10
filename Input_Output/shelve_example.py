# pickling是存储在memory里面的，而如果文件太大就不太好了
# 于是就有shelve，存储在file而不是memory里面。
# 同pickling一样，也是不要使用untrusted source
# 和字典的结构类似，key+value pair
import shelve

# shelve是read and write by nature，所以不比像之前一样设置读写模式。
# with shelve.open("ShelfTest") as fruit:
#     # 以下不可以直接写成一个字典的形式，虽然也能print出来
#     # 但是会发现，在with板块外仍然能够打印文件内容出来，所以就不行。
#     fruit["orange"] = "a sweet, orange, citrus fruit"
#     fruit["apple"] = "good for making cider"
#     fruit["lemon"] = "a sour, yellow citrus fruit"
#     fruit["grape"] = "a small, sweet fruit growing in bunches"
#     fruit["lime"] = "a sour, green citrus fruit"
#
#     print(fruit["lemon"])
#     print(fruit["grape"])
#
# # print(fruit["lemon"])  # 移出来了就不能打印文件内容了，因为在with板块外面，就说明文件已经关闭。
# # print(fruit["grape"])
#
# print(fruit)   # shelve对象，而非字典。

# 想手动开关文件的话
fruit = shelve.open("ShelfTest")

# fruit["orange"] = "a sweet, orange, citrus fruit"
# fruit["apple"] = "good for making cider"
# fruit["lemon"] = "a sour, yellow citrus fruit"
# fruit["grape"] = "a small, sweet fruit growing in bunches"
# fruit["lime"] = "a sour, green citrus fruit"

# print(fruit["lemon"])
# print(fruit["grape"])
#
# fruit["lime"] = "great with tequila"
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])
# 鼠标选中，shift + tab，反向缩进。
# print(fruit["lemon"])  # 移出来了就不能打印文件内容了，因为在with板块外面，就说明文件已经关闭。
# print(fruit["grape"])

# print(fruit)   # shelve对象，而非字典。

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#
#     if dict_key in fruit:
#         description = fruit[dict_key]  # 下方用get是为了避免查无key出现错误的情况。
#         # description = fruit.get(dict_key, "We don't have a " + dict_key)   # 找不到就默认值返回None，不会出现错误。
#         print(description)
#     else:
#         print("We don't have a " + dict_key)

# 因为shelve和字典一样也是无序的，所以还是需要排序。
# ordered_keys = list(fruit.keys())
# ordered_keys.sort()
#
# for f in ordered_keys:
#     print(f"{f} - {fruit[f]}")

for v in fruit.values():
    print(v)
print(fruit.values())

for f in fruit.items():
    print(f)
print(fruit.items())

# 可见shelve的操作和字典差不多，只是shelve key必须是string类型的，而字典可以是任何hashable类型。
fruit.close()
