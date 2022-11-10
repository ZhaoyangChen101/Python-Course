def factorial(n):
    # n! can also be defined as n * factorial(n-1)
    """calculate n! recursively!"""
    if n <= 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n - 1)


# try:
#     print(factorial(1000))
# except RecursionError:
#     print("This program cannot calculate factorials that large.")
# except ZeroDivisionError:
#     print("Dividing zero is not acceptable.")

try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program cannot calculate factorials that large.")

print("Program terminating")

