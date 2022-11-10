parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()
# 真的也，就是上面正着数时的index减去string的长度14。
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

#                   1
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[:6] + parrot[6:])

print(parrot[:])

letters = "abcdefghijklmnopqrstuvwxyz"

print(parrot[-4:2])  # print nothing
print(parrot[-4:-2])  # Bl
print(parrot[-4:12])  # Bl

print(parrot[0:6])
print(parrot[-14:-8])

# Using a step in a slice
#                   1
#         012345678901234
parrot = "Norwegian Blue"
print(parrot[0:6:2])  # Nre
print(parrot[0:6:3])  # Nw

number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "9,223;372:036 854,775;807"
print(number[1::4])  # step可以将separator提取，然后用于data file提取数据

separators = number[1::4]
print(separators)
print("*" * 80)

number = input("Please enter a series of numbers using any separators: ")
separators = ""
for char in number:
    if not char.isnumeric():
        separators += char
#print(separators)
# 后面来看这个!!!
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
#  [9, 223, 372, 36, 854, 775, 807]





