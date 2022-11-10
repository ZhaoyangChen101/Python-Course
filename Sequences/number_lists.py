even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

print()
print(len(even))
print(len(odd))  # function len(), min(), max()直接用

print()
print("mississippi".count("issi"))  # method，.count()必须要和对象绑定在一起使用。

healthy = [1, 1, 1, 1, 3, 2]
print(healthy.count(1))

even.extend(odd)  # extend一个list：将另一个list添加到list后面
print(even)

even.sort()  # .sort()是sort the list in place
print(even)

even.sort(reverse=True)
print(even)

print()
empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]
numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)


digits = list("432985617")  # 返回一个list
print(digits)

# more_numbers = list(numbers)  # 相当于是copy了一个list
# more_numbers = numbers[:]  # 也可以通过slice来copy一个list
more_numbers = numbers.copy()  # copy method直接来copy
print(more_numbers)
print(numbers is more_numbers)  # False, 表明not the same list，只有referring to the same list的时候，才会是True
print(numbers == more_numbers)  # True，只要两个list元素且顺序相同就返回true

# list inside list
print()
another_numbers = [even, odd]
print(another_numbers)

for number_list in another_numbers:
    print(number_list)

    for value in number_list:
        print(value)
