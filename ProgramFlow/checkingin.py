parrot = "Norweigan Blue"
letter = input("enter: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("i don't need that letter")
