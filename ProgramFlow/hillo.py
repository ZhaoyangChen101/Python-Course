low = 1
high = 1000

print("please think between {} and {}.".format(low, high))
input("Press ENTER to start")

guess = 1
guesses = 1
while low != high:
    #  print("\tGuessing in the range of {} to {}".format(low, high))
    guess = (low + high) // 2
    # use reformat code
    high_low = input("My guess is {}. Should i guess higher or lower? "
                     "Enter h, l or c if my guess was correct "
                     .format(guess)).casefold()

    if high_low == "h":
        #  Guess higher The low end of the range becomes 1 greater than the guess
        low = guess + 1
    elif high_low == "l":
        # Guess lower. The high end of the range becomes one less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("i got it in {} guesses!".format(guesses))
        break
    else:
        print("please enter h, l, or c")
    guesses += 1
else:  # else in companion with while/for loops means completed/no break
    print("You though of the number {}.".format(low))
    print("I got in {} guesses.".format(guesses))