# reformat: cmd + opt + L
# alt + shift + up 将对应行往上挪一行。在挪动的时候，这个多余的逗号也不会影响整体的结构。
# 结尾加了一个多余逗号，便于更改，又不影响使用
menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]
for meal in menu:
    if "spam" not in meal:
        print(meal)

        for item in meal:
            print(item)
    else:
        # list/sequence.count(element) - total occurrence of element in the sequence
        print("{0} has a spam score of {1}".format(meal, meal.count("spam")))




