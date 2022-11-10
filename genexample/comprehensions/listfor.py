print(__file__)   # print out the full name of the python file we're executing

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Please enter a number, and I'll tell you its square: "))

squares = []
for number in numbers:
    squares.append(number ** 2)

print("The current value of `number` is {}".format(number))
index_pos = numbers.index(number)
print(squares[index_pos])
print(squares)