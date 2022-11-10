# deep copy

import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkle"],
    "teddy": ["cuddly", "stuffed"],
}

# Perform a shallow copy
# things = animals.copy()

# perform a deep copy
things = copy.deepcopy(animals)

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(id(things["teddy"]))
print(animals["teddy"])
print(id(animals["teddy"]))

print()
animals["teddy"].append("eureka")
print(things["teddy"])
print(animals["teddy"])

# 小结：shallow copy -> dictionary.copy() 复制reference，
#      deep copy -> import copy, copy.deepcopy(dictionary), 复制objects
# list.copy()两个list是不一样的id，如果dict里面有list，其.copy()之后，list的id是
# 相同的。