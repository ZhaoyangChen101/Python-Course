d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four"
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)
print("eleven" in v)

keys = list(d.keys())
values = list(v)
if "four" in values:
    index = values.index("four")
    # list.index(value)的一大问题是：只能返回value第一次出现的index，后面的就不会管了。
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items():
    if value == "four":
        print(f"{d[key]} was found with the key {key}")

# retrieving key is faster than getting a value.
# Code for "the dict `update` method" lecture
# ***********************************************
# d2 = {
#     7: "lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }
#
# d.update(d2)
# for key, value in d.items():
#     print(key, value)
#
# print()
#
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)

# Code for "the remaining `dict  methods" lecture
# dict.fromkeys(iterable, default)
# new_dict = dict.fromkeys(pantry_items, 0)
# # list中的元素作为keys来形成新的字典，默认键对应的值为none，设置为0，就是0。
# print(new_dict)

# .keys(), 这个不太高效，因为它是将字典中的键值进行复制。
# 如果字典很大的话，效果就很不好了。
# keys = d.keys()
# print(keys)
#
# # print(keys)
# for item in d:
#     print(item)
# # print(keys)只是这个代码的功能就很清晰了。但是这个用得很少。用上面的那个就好。
# for item in d.keys():
#     print(item)






