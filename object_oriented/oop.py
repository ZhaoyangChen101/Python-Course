# a = 16
# b = 12
# print(a + b)
# print(a.__add__(b))

class Kettle(object):

    power_source = "electricity"   # class attribute

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

"""
Class: template for creating objects. All objects created using the same class will have the same characteristics.
Object: an instance of a class
Instantiate: create an instance of a class
Method: a function defined in a class
Attribute: a variable bound to an instance of a class.
"""

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)   # class.method(对象)也可以哦！！！
print(kenwood.on)
kenwood.switch_on()

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)  # 我又震惊了，可以在这个实例下，新增属性，只不过只属于这一个对象，不会改变类的结构，不会影响其他对象的属性。
# print(hamilton.power)  # 所以这个就是不行的。

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(kenwood.power_source)
print(hamilton.power_source)

print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)   # class.__dict__ 或者对象.__dict__存储了"属性:值"键值对