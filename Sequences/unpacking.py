a = b = c = d = e = f = 12
print(c)

x, y, z = 1, 2, 3
print(x)
print(y)
print(z)

print("Unpacking a tuple")

data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)

print("Unpacking a list")

data_list = [12, 13, 14]
# data_list.append(15)
p, q, r = data_list
print(p)
print(q)
print(r)
# 小结：可以unpacking任意一种sequence。但是因为list是mutable的，
# 如果在unpacking之前对list进行了更改，那么再进行unpacking的时候程序就会crash
# 所以，在unpack list的时候，一定要保证list的长度不会变。

