import random


def get_integer(prompt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param prompt: The Strings that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)  # cmd + click查看function的source code
        if temp.isnumeric():
            return int(temp)
        # else:
        print("{0} is not a valid number".format(temp))


# We are not calling functions here but referring to their attributes.
# That means we do not use parentheses after the function name.

# print(input.__doc__)
# print("*" * 80)
# print(get_integer.__doc__)
# print("*" * 80)

help(get_integer)

highest = 1000
answer = random.randint(1, highest)  # random number from 1 to 10 inclusive
print(answer)  # TODO: remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
guess = 0

# if guess == answer:
#     print("you got it first time")
# else:
#     if guess < answer:
#         print("please guess higher")
#     else:  # guess must be greater than answer
#         print("please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("well done, you guessed it")
#     else:
#         print("sorry")
guess_times = 1
while guess != answer:
    guess = get_integer(": ")
    # print(guess)    # TODO: delete after test
    if guess == 0:
        break
    elif guess < answer:
        print("please guess higher: ")
    else:  # guess must be greater than answer
        print("please guess lower: ")
    # guess = int(input())
    guess_times += 1
if guess == 0:
    print("You have quit the game!")
elif guess_times == 1:
    print("So lucky, you got it first time!")
else:
    print("Well done, you have the correct answer in {} times".format(guess_times))
# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry")
# else:
#     print("you got it first time")



