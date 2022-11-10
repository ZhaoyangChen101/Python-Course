def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


# def centre_text(*args, sep=' ', end='\n', file=None, flush=False):
#     text = ''
#     for arg in args:
#         text += str(arg) + sep
#     left_margin = (80 - len(text)) // 2
#     # print(" " * left_margin, text, end=end, file=file, flush=flush)
#     return " " * left_margin, text

# with open("centred", mode='w') as centre_file:
#     centre_text("Spam and eggs", file=centre_file)
#     centre_text("Spam, spam and eggs", file=centre_file)
#     centre_text("Spam, spam, spam and eggs", file=centre_file)
#     centre_text(12, file=centre_file)
#     centre_text("first", 2, 3, "spam", sep=":", file=centre_file)


def centre_text(*args, sep=' '):
    text = ''
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text


# s1 = centre_text("Spam and eggs")
# print(s1)
# s2 = centre_text("Spam, spam and eggs")
# print(s2)
# s3=centre_text("Spam, spam, spam and eggs")
# print(s3)
# s4=centre_text(12)
# print(s4)
# s5 = centre_text("first", 2, 3, "spam", sep=":")
# print(s5)

with open("menu", mode='w') as menu:
    s1 = centre_text("Spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("Spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text("Spam, spam, spam and eggs"), file=menu)
    print(centre_text(12), file=menu)
    s5 = centre_text("first", 2, 3, "spam", sep=":")
    print(s5, file=menu)


# python_food()
# skvmsvslvm  -> fn + delete反向删除
# print(python_food())
# 不仅执行了程序本身，还返回了None，这个是从来没有留意过的。
# 所有的方程都会返回结果，如果是action，未定义返回，则返回None。


