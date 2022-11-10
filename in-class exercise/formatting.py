for i in range(1, 13):
    # 下结果是右对齐，如果是>，也是右对齐
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    # 下结果<表示是左对齐
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))

for i in range(1, 13):
    # 下结果^表示是中心对齐
    print("No. {0:2} squared is {1:^3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()
# python max precision is between 51 and 53 digits
# python3.8 max precision is 51 according to my experiment
# 精度优先于长度。
print("Pi is approximately {0:12}".format(22 / 7))
print("Pi is approximately {0:12f}".format(22 / 7))
print("Pi is approximately {0:12.50f}".format(22 / 7))
print("Pi is approximately {0:52.50f}".format(22 / 7))
print("Pi is approximately {0:62.50f}".format(22 / 7))
print("Pi is approximately {0:72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.50f}".format(22 / 7))
print("Pi is approximately {0:<72.54f}".format(22 / 7))

# 在{}不声明填充位置时，按顺序依次填充，这样的话每个位置的值只能用一次。
for i in range(1, 13):
    # 下结果^表示是中心对齐
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

