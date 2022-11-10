flowers = [
    "Daffodil",
    "Evening Primrose",
    "Hydrangea",
    "Iris",
    "Lavender",
    "Sunflower",
    "Tiger Lily",
    # 42
]

# for flower in flowers:
#     print(flower)

# it is called bar
# separator = " | "
separator = " , "
# separator.join(sequence)表示iterable中的元素以separator连接起来，输出为string。
# join method iterates for us
# 不过join要求sequence里面的元素必须都是string类型的
output = separator.join(flowers)
print(output)
print(",".join(flowers))

# Lists are mutable sequences,
# typically used to store collections of homogeneous items
# (where the precise degree of similarity will vary by application).
# 存储同一类型的元素并不强制，但是可能会出一些问题。

# join: joins elements in an iterable, which only contains strings, and output a string
# split: returns a list from a sequence
