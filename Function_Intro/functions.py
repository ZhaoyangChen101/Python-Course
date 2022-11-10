def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence. If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    The testing standard is case-insensitive.

    :param string: A string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespaces, capitalization, and
    punctuation in the sentence.

    :param sentence: A sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    # print(string)
    # return string[::-1].casefold() == string.casefold()
    return is_palindrome(string)


def fibonacci(n: int) -> int:
    """Return the  `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return 0

    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n - 1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result
    return result


for i in range(36):
    print(i, fibonacci(i))

print(multiply.__doc__)
print("*" * 80)
print(is_palindrome.__doc__)
print("*" * 80)
print(palindrome_sentence.__doc__)
print("*" * 80)

answer = multiply(18, 3)
print(answer)

p = palindrome_sentence()
# word = input("please enter a word to check: ")
# if palindrome_sentence(word):
#     print("{} is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))

# there should be two blank lines after the definition of the function
# answer = multiply(5, 4)
# print(answer)
#
# forty_two = multiply(6, 7)
# print(forty_two)
#
# print()
#
# for val in range(1, 5):
#     two_times = multiply(2, val)
#     print(two_times)

