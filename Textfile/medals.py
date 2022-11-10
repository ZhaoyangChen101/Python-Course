import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    headers = csv_file.readline().strip('\n').split(',')  #.readline()返回的是string。
    print(f"Column headers: {headers}")
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)  # <class '_csv.reader'>
    # print(type(reader))
    for row in reader:
        # print(type(row))   # list，说明csv.reader这个iterable遍历的时候返回的是list。
        print(row)