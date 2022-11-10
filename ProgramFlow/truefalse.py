day = "Saturday"
temp = 30
raining = False

#  and has a higher precedence than or
if day == "Saturday" and temp > 27 and not raining:
    print("go swimming")
else:
    print("learn python")

if 0:
    print("True")
else:
    print("False")

name = input("Name:")
#if name:
if name !="":
    print("hello, {}".format(name))
else:
    print("No name?")
