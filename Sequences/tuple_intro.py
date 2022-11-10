# 这样的写法就是tuple，但是最好有括号。
# t = "a", "b", "c"
# print(t)
# t1 = ("a", "b", "c")
# print(t1)

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad company", "Bad company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# metallica2 = list(metallica)
# print(metallica2)
#
# metallica2[0] = "Master of Puppets"
# print(metallica2)
title, artist, year = metallica
print(title)
print(artist)
print(year)

table = ("coffee table", 200, 100, 75, 34.50)
print(table[1] * table[2])

name, length, width, height, price = table
print(length * width)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad company", "Bad company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the lightning", "Metallica", 1984),
]
print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist:{}, Year:{}"
          .format(name, artist, year))

for album in albums:
    name, artist, year = album
    print("Album: {}, Artist:{}, Year:{}"
          .format(name, artist, year))

# 反思： 以上两种都是可以的，第二种没有第一种那样高效，不过因为有album，保证了原tuple
# 通常来讲用第一种loop
# Tuples are immutable and there are some advantages.
# 1. Tuples use less memory than lists because they don't have the overhead of
# the methods needed to change them.
# If your memory is dealing millions of these things,
# you can save memory by using a tuple.

# 2. Tuples can protect the integrity of the data.

# 3. Tuples can help to prevent bugs.

# 4. You can always unpack a tuple because it is immutable.
# Even though you can unpack any kind of sequences,
# this is described as unpacking a tuple.

# 5. lists are homogeneous while TUPLES are heterogeneous.
