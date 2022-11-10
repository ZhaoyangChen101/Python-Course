import random

highest = 10
answer = random.randint(1, highest)  # random number from 1 to 10 inclusive
#  print(answer)  # TODO: remove after testing
print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

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
    if guess < answer:
        print("please guess higher: ")
    else:  # guess must be greater than answer
        print("please guess lower: ")
    guess = int(input())
    guess_times += 1
if guess_times == 1:
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



