# numbers = {} # type为dictionary
# numbers = {*''}  # 这样type打印出来就是set，看得懂就行，但是avoid doing this。
# numbers = {*{}}
numbers = set()  # 常用的初始化set的方法。

print(numbers, type(numbers))

# numbers.add(1)
# print(numbers)

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
#
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]
# Create a set from the list to remove duplicates
# unique_data = set(data)
unique_data = sorted(set(data))  # sorted方程返回的是list
print(unique_data)

# 如果说想要保持添加的顺序（涉及到顺序就不考虑set），又想要删除多余的值，dict.fromkeys()
# Create a list of unique colors and keep the order they appear.
unique_data = list(dict.fromkeys(data))
# list(dict) 是将dict的keys转换为list。
print(unique_data)

print()
print(dict.fromkeys(data))

