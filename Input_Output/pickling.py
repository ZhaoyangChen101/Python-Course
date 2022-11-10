import pickle
# you can only unpickling data you trust
# pickling your own program data is fun but shouldn't be used when dealing with
# data of untrusted sources, which may wreak havoc.
#
imelda = ('more mayhem',
          'imelda may',
          '2011',
          ((1, 'pulling the rug'),
           (2, 'psycho'),
           (3, 'mayhem'),
           (4, 'kentish')))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file)

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

imelda = ('more mayhem',
          'imelda may',
          '2011',
          ((1, 'pulling the rug'),
           (2, 'psycho'),
           (3, 'mayhem'),
           (4, 'kentish')))

even = list(range(0, 10, 2))
odd = list(range(1, 10, 2))

with open("imelda.pickle", "wb") as pickle_file:
    pickle.dump(imelda, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even, pickle_file, protocol=0)
    pickle.dump(odd, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302, pickle_file, protocol=pickle.DEFAULT_PROTOCOL)
    # protocol 默认是3，protocol与python版本对应
    # data created in protocol 3 cannot be read by python version 2 and below.
    # protocol会被python自动确定，所以不必要去定义它。

with open("imelda.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)

print(imelda2)

album, artist, year, track_list = imelda2

print(album)
print(artist)
print(year)
for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)

print("=" * 40)

for i in even_list:
    print(i)

print("=" * 40)

for i in odd_list:
    print(i)

print("=" * 40)

print(x)


print("=" * 40)
# remove file
pickle.loads(b"cos\nsystem\n(S'rm imelda.pickle'\ntR.")  # mac/linux
# loading a file could lead to another file being deleted.

