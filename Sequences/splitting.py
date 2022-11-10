panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()  # split默认分离一个或多个空格、回车
print(words)  # split是join的逆操作，输入string，输出list。

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

separators = ""
for char in numbers:
    if not char.isnumeric():
        separators += char
# 理解了join里压缩写法，从内板块向外板块写。括号里输出的generator类型。
# 里面也可以写成[char if char not in separators else " " for char in numbers]
# 上列就是一个list了。也是可行的。
values = "".join(char if char not in separators else " " for char in numbers).split()
print(sum([int(val) for val in values]))

print("分解步骤如下：")
values1 = "".join(char if char not in separators else " " for char in numbers)
print(values1)
values2 = values1.split()
print(values2)

# split在读文件的时候很有用。
print("transform strings into integers:")

# transform string into integer of the elements in the list
# 下面的转换并不成功：
# for val in values:
#     val = int(val)

# 换一种：
int_values = []
for val in values:
    int_values.append(int(val))
print(int_values)
# 简洁版：
print([int(val) for val in values])

# 老师版本
# replace the values in the list
for index in range(len(values)):
    values[index] = int(values[index])
    #values[index] = str(values[index]) 上方的index的黄色就消失了，但是此处这个warning可以忽略。
    #! most of the times, the warning is accurate.

print(values)
# 反思：只有list[index]的方式可以更新list的元素值。


