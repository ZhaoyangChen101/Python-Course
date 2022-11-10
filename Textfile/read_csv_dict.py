import csv

cereal_filename = 'cereal_grains.csv'

with open(cereal_filename, encoding='utf-8', newline='') as cereal_file:
    reader = csv.DictReader(cereal_file)  # 回忆起和文本文件的区别就是多了一句
    for row in reader:
        print(row)
