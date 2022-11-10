print("today is a good day to learn Python")
print('Python is fun')
print("python' s string are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " world")
greeting = "hello"
name = "Tim"
print(greeting + name)
# if we want a space, we can add that too
print(greeting + ' ' + name)

age = 24
print(type(age))
print(type(greeting))

# f-strings
age_in_words = '2 years'
print(name + f" is {age} years old")
print(type(age))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

meal1 = "1" \
       "2" \
       "3"
print(meal1)

meal2 = """1
2
3
"""
print(meal2)

meal3 = "1\n2\n3"
print(meal3)