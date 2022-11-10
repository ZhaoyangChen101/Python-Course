def fizz_buzz(number: int) -> str:
    """
    Return `fizz` or `buzz` given required numbers.
    :param number: Any integer number to start
        counting
    :return: If the number is divisible by 3, return
        `fizz`; if divisible by 5, return `buzz`; if
        divisible by both, return `fizz buzz`.
    """

    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)


# my solution works
# print("Game start!")
# computer_num = 1
#
# while True:
#     print("Computer: {}".format(fizz_buzz(computer_num)))
#     your_answer = input("Your answer: ")
#     expected_num = computer_num + 1
#     if your_answer == fizz_buzz(expected_num):
#         computer_num = expected_num + 1
#     elif your_answer != fizz_buzz(expected_num) or expected_num == 100:
#         print("Game is over!")
#         break


input("Play Fizz Buzz.    Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    player_answer = input("Your go: ")
    # player_answer = correct_answer  # TODO: Have a look at the correct list of answers
    if player_answer != correct_answer:
        print("You lose, the correct answer was {}".format(format(correct_answer)))
        break
else:
    print("Well done, you reached {}".format(next_number))