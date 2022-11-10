import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for line in range(3):
        sample += countries_data.readline()  # 这就是高效的做法，就看个几行，因为格式反正都是差不多的。
    # sample = countries_data.read()  # 你去读所有的文件就不太高效。
    country_dialect = csv.Sniffer().sniff(sample)
    country_dialect.skipinitialspace = True
    # country_reader = csv.reader(countries_data, delimiter='|')
    countries_data.seek(0)  # position the file pointer to another place in the file，这里就是最初的位置。
    country_reader = csv.reader(countries_data, dialect=country_dialect)
    for row in country_reader:
        print(row)

print('*' * 80)
attibutes = ['delimiter',
             'doublequote',
             'escapechar',
             'lineterminator',
             'quotechar',
             'quoting',
             'skipinitialspace',]

for attribute in attibutes:
    print(f"{attribute}: {repr(getattr(country_dialect, attribute))}")
    # getattr(对象，属性名称) -> 获得属性值。
    # repr是表达式，此处就能看到它的作用，没有使用repr时，lineterminator后面什么都没有，使用之后就出现'\r\n'
    # 可见，就是将本身的表达式显示出来。