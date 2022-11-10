choice = "-"
while choice != "0":
    # 这种比while True好，因为明确指出了跳出循环的条件。
    # 否则，就需要继续阅读接下来的代码，不够清晰。
    # if choice in "12345":
    # if choice in list('12345'):
    # 此处用set比list高效。
    # if choice in set("12345"): 存在转换，涉及到loop复制。
    # 如何使用set也很重要，下面比上面的用法更高效。
    if choice in {"1", "2", "3", "4", "5"}:
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list")
        print("1:\tLearn python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")

    choice = input()

