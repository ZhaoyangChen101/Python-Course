def center_text(*args):
    text = ""
    # for arg in args:
    #     text += str(arg) + "-"

    # text = '-'.join(args)

    text = '-'.join([str(arg) for arg in args])  # 对于int也行了。
    # text = '-'.join(str(arg) for arg in args)  # 这个也能行，不过此时括号里是generator。
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)


# call the function
center_text("spam and eggs")
center_text("spam, spam and eggs")
center_text(12)   # text = '-'.join(args)这里会出问题：you cannot join int to strings
center_text("spam, spam, spam and spam")

center_text("first", "second", 3, 4, "spam")
