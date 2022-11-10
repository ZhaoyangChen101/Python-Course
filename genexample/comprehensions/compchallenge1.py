# for x in range(1, 31):
#     fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
#     print(fizzbuzz)
#
# print()

# list are designed to be homogenous
fizzbuzz = ["fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
            for x in range(1, 31)]
print(fizzbuzz)

for buzz in fizzbuzz:
    print(buzz.center(12, '*'))
    # string.center(length, 补缺符号)，
    # 如果list之前中间有int类型，就会出现问题，故str(x)
    