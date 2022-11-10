entries = []

if entries:  # list不为空的时候
    print("Yeah")
    print("all: {}".format(all(entries)))   # all values are True or it is empty
else:
    print(False)
print("any: {}".format(any(entries)))   # at least one value is True

# result = entries and all(entries)
result = bool(entries and all(entries))
print(result)
