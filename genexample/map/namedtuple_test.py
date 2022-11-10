from data import basic_plants_list, plants_list

print(plants_list[0])

# for plant in basic_plants_list:
#     print(plant[0])   # namedtuple可以直接像tuple一样使用，此处就是直接index就能得到对应的值

for plant in plants_list:
    # print(plant.name)   # namedtuple显示属性值的这种写法可读性更高，且不用去记住位置，体现了namedtuple的意义。
    print(plant.name, plant[1])   # 但是index也是可行的，不能说没有任何价值。
    # tuple的任何操作，namedtuple都是可以的。
    # 额外有三个function。
    # namedtuples are immutable，but _replace方法是创建一个部分值被更改的新namedtuple。

print()

example = plants_list[0]
print(example)
example = example._replace(lifecycle='Annual')  # 实际上是新建了新namedtuple.
print(example)

