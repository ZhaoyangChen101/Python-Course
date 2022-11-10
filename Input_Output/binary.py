# # b for binary and w for write, 如果只写w的话，就是textfile
# with open("binary", "bw") as bin_file:
#     # for i in range(17):
#     #     # bytes(i)这样的话就会得到a byte sequence里有i个0，
#     #     # 故[i]，这样会转换成single byte
#     #     bin_file.write(bytes([i]))
#     bin_file.write(bytes(range(17)))  #得到的结果和上方一样
#
#
# with open("binary", "br") as binFile:
#     for b in binFile:
#         print(b)

a = 65534    # FF FE
b = 65535    # FF FF
c = 65536    # 00 01 00 00
x = 2998302  # 00 2D C0 1E

with open("binary2", "bw") as bin_file:
    bin_file.write(a.to_bytes(2, "big"))    # to_bytes里面的参数：length，order
    bin_file.write(b.to_bytes(2, "big"))
    bin_file.write(c.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "big"))
    bin_file.write(x.to_bytes(4, "little"))

with open("binary2", "br") as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile.read(4), 'little')
    print(i)

