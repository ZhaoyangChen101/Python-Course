entries = [1, 2, 3, 4, 5]

print("all: {}".format(all(entries)))   # all values are True or it is empty
print("any: {}".format(any(entries)))   # at least one value is True

print("Iterable with a 'False' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))   # all values are True
print("any: {}".format(any(entries_with_zero)))   # at least one value is True

print()
print("Values interpreted as False in Python")
print("""False: {0}
None: {1}
0: {2}
0.0: {3}
empty list []: {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))


print("=" * 80)
name = "Tim"
if name:
    print("Hello {}".format(name))
else:
    print("Welcome, person with no name")
