menu = [
    ["egg", "spam", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
    ["spam", "egg", "sausage", "spam"],
    ["chicken", "chips"]
]

# meals = []
# for meal in menu:
#     if "spam" not in meal:
#         meals.append(meal)
#     else:
#         meals.append("a meal was skipped")
# print(meals)
#
# # meals = [meal for meal in menu if "spam" not in meal]
# meals = [meal if "spam" not in meal else "a meal was skipped" for meal in menu]
# print(meals)
#
# x = 15
# expression = "Twelve" if x == 12 else "unknown"
# print(expression)

for meal in menu:
    print(meal, "contains chicken" if "chicken" in meal else "contains bacon" if "bacon" in meal else "contains egg")

print()

items = set()
for meal in menu:
    for item in meal:
        items.add(item)
print(items)
print()

for meal in menu:
    for item in items:
        if item in meal:
            print("{} contains {}".format(meal, item))
            break  # 表示只要找到第一个item就停止。

print()

# meals = ["{} contains {}".format(meal, item) if item in meal else None for meal in menu for item in items]
# for meal in meals:
#     if meal is not None:
#         print(meal)

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)