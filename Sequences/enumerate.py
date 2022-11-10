# for index, character in enumerate("abcdefgh"):
#     print(index, character)

# enumerate 就是一堆tuple，是enumerate对象。
for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)
    # print(t)
# print(enumerate("abcdefgh"))

index, character = (0, 'a')
print(index)
print(character)
