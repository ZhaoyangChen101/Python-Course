import json

languages = [
    ('ABC', 1987),
    ('Algol 68', 1968),
    ('APL', 1962),
    ('C', 1973),
    ('Haskell', 1990),
    ('Lisp', 1958),
    ('Modula-2', 1977),
    ('Perl', 1987),
]  # tuple存储在json里面会成为list，因为没有什么改变

with open('text.json', 'w', encoding='utf-8') as testfile:
    json.dump(languages, testfile)

with open('text.json', 'r', encoding='utf-8') as testfile:
    data = json.load(testfile)
print(data)
print(data[2])  # confirm that we are dealing with a list here, and not a string.
# 此处就说明json保存好了原本的存储的数据结构。
