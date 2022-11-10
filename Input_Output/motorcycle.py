import shelve

with shelve.open("bike2") as bike:
    # bike["make"] = "Honda"
    # bike["model"] = "250 dream"
    # bike["colour"] = "red"
    # bike["engin_size"] = 250  # 这里写错了，还是会写进去。
    # bike["engine_size"] = 250

    del bike['engin_size']   # 可以像字典那样来删除。
    for key in bike:
        print(key)
    print('=' * 40)

    print(bike['engine_size'])
    # print(bike['engin_size'])
    print(bike["colour"])

