# def factorial(number: int) -> int:
#     """Return the factorial of `number` """
#     if number == 0:
#         return 1
#     elif number > 0:
#         result = 1
#         for i in range(1, number + 1):
#             result *= i
#         return result

# recursion
def factorial(number: int) -> int:
    """Return the factorial of `number`"""
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


for num in range(36):
    print("{} {}".format(num, factorial(num)))
