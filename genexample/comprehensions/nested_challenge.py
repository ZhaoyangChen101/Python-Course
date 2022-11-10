for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)

print("=" * 20)

products = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(products)

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)

products2 = [[(j, j * i) for i in range(1, 11)] for j in range(1, 11)]
print(products2)

# 因为list comprehension会生成list memory，当数据量太大的时候，会占用很多的内存
# 如果list会被重复使用，是okay的
# 如果只是有iterate的需求，没有说要再使用这个list，就只需要使用其generator就好。
for x, y in ((i, i * j) for i in range(1, 11) for j in range(1, 11)):
    print(x, y)
