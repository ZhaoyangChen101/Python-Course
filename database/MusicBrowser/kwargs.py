# def print_backwards(*args, **kwargs):
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#     # print(kwargs)  # 字典

def print_backwards(*args, **kwargs):
    # 字典的pop中的第二个元素表示的是，如果没有该key，则返回的值。
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]:
        print(word[::-1], end=sep_character, **kwargs)
    # print(end=end_character)
    print(args[0][::-1], end=end_character, **kwargs)  # print the first word separately


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", "w") as backwards:
    print_backwards("hello", "planet", "earth", end='\n', sep='|')
