choice = "-"
while choice != "0":
    # 这种比while True好，因为明确指出了跳出循环的条件。
    # 否则，就需要继续阅读接下来的代码，不够清晰。
    if choice in "12345":
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
