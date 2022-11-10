import csv

csv_filename = 'cereal_grains.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    # QUOTE_NONNUMERIC 说明的是所有的非数字都是被quoted了的。
    for row in reader:
        print(row)