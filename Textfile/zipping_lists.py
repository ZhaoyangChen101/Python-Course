import csv

albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad Company", "Bad Company", 1974),
          ("Nightflight", "Budgie", 1981),
          ("More Mayhem", "Imelda May", 2011),
          ("Ride the Lightning", "Metallica", 1984),
          ]

keys = ['album', 'artist', 'year']

filename = 'albums.csv'
with open(filename, 'w', encoding='utf-8', newline='') as csv_file:
    writer = csv.DictWriter(csv_file, quoting=csv.QUOTE_NONNUMERIC, fieldnames=keys)
    writer.writeheader()  # 哪怕传输了fieldname也需要单独一个步骤writeheader()来写属性名称。
    for row in albums:
        zip_project = zip(keys, row)
        # print(zip_project)
        # for thing in zip(keys, row):
        #     print("\t", thing)
        albums_dict = dict(zip_project)
        print(albums_dict)
        writer.writerow(albums_dict)
