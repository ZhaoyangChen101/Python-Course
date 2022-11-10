age = int(input("How old are you? "))

#  if age >= 16 and age <=65:
# if 16 <= age <= 65: 这个比下面range的方法更加有效
if age in range(16, 66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")

print("-" * 80)

if age < 16 or age > 65:
    print("enjoy your free time")
else:
    print("have a good day at work")
