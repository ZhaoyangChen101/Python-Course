letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards)  # zyxwvutsrqponmlkjihgfedcb

backwards = letters[25:-1:-1] # nothing

backwards2 = letters[::-1]
print(backwards2)

# qpo
print(letters[-10:-13:-1])  # letters[16:13:-1]
# edcba
print(letters[4::-1])
# last 8 charatcters in reverse order
print(letters[-1:-9:-1])  # [::-9:-1]

# slice idioms
# 返回倒序
print(letters[::-1])
# 返回最后几个字符
print(letters[-4:])
# 返回最后一个字符
print(letters[-1:])
# 返回第一个字符，两种方式
print(letters[:1])
print(letters[0])
# 如果字符是空的，第二种方式就会有错误：string index out of range，第一种会返回空
# 故，选择第一种表达





