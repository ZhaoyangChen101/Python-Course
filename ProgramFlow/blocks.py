name = input("Please enter your name: ")
age = int(input("how old are you, {0}? ".format(name)))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18 - age))

if age < 18:
    print("Please come back in {0} years".format(18 - age))
elif age == 900:
    print("sorry")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
# 要习惯使用debugger。只有当你实在卡住了的时候才用debugger。
