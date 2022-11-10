vehicles = {
    'dream': 'Honda 250T',
    'er5': 'Kawasaki ER5',
    'can-am': 'Bombardier Can-Am 250',
    'virago': 'Yamaha XV250',
    'tenere': 'Yamaha XT650',
    'jimny': 'Suzuki Jimny 1.5',
    'fiesta': 'Ford Fiesta Ghia 1.4',
    'roadster': 'Triumph Street Triple'
}

# my_car = vehicles['Fiesta']
# print(my_car)  # Error
#
# commuter = vehicles['virago']
# print(commuter)
#
# learner = vehicles.get("ER5")
# print(learner)  # None

# 反思：两种获得value的方式，1）index，2）get方法。区别在于，当key不存在时
# index方法会出现错误，而get方法会返回None,get还有找不到可以返回设定的值。
# 故，当不确定key存不存在时，用get方法。
# 但是由于index会更高效，故，在确定key存在时，用index。
# 补充：有时，你希望能出现错误，因为你不想要不合适的data，此时需要配合exception。

# for key in vehicles:
#     print(key, vehicles[key], sep=", ")

vehicles['starfighter'] = "Lockheed F-104"
vehicles["learjet"] = "bombardier Learjet 75"
vehicles["toy"] = "glider"

# upgrade the Virago
vehicles["virago"] = "Yamaha XV535"

# 删除
del vehicles['starfighter']
# del vehicles['f1']  # error
result = vehicles.pop("f1", None) # 第二个argument表示如果没有f1，就返回None。这样找不到也不会crash
print(result)
plane = vehicles.pop("learjet")
print(plane)

bike = vehicles.pop("tenere", "not present")
print(bike)
print()
# "删除"小结：del比pop效率略高，但是pop有一个default的值在没有key的时候不会报错。

for key, value in vehicles.items():
    print(key, value, sep=": ")

# 小结：enumerate —> sequence, .items() -> dictionaries

