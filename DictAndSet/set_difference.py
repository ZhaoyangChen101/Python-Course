from primes_and_squares import squares_generator, primes_generator

evens = set(range(0, 50, 2))
odds = set(range(1, 50,2))

print(evens)
print(odds)

primes = set(primes_generator(100))
print(primes)
squares = set(squares_generator(100))
print(squares)

print(odds.difference(primes))
# primes numbers are integers greater than 1. 所以1不算质数。
# 2是最小的质数，也是唯一的一个既是偶数又是质数的数． 也就是说，除了2以外，质数都是奇数。

print(odds - primes)
print(primes - odds)
