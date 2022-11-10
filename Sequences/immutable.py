# result = True
# another = result
# print(id(result))
# print(id(another))
#
# result = False
# print(id(result))

result = "Correct"
another = result
print(id(result))
print(id(another))

result += "ish"
print(id(result))
print(id(another))

