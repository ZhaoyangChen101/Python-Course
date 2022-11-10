data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac- Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]


# plants_filename = "flowers_print.txt"
#
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         print(plant, file=plants)   # default is to print to the screen.
#
# new_list = []
#
# with open(plants_filename) as plants:
#     for plant in plants:
#         new_list.append(plant.rstrip())
#         # new_list.append(plant)   # 没有strip就会有/n在末尾。
#
# print(new_list)

# plants_filename = "flowers_write.txt"
#
# with open(plants_filename, 'w') as plants:
#     for plant in data:
#         plants.write(plant)  # 对比print写文件，因为默认是/n结尾，所以自动换行，可是write没有，就直接写成了一行。
#
# print(data)
# string_representation = data.__str__()
# print(type(string_representation))

file_name = "test_numbers.txt"
with open(file_name, 'w') as test:
    for i in range(10):
        print(i, file=test)

with open(file_name, 'w') as test:
    for i in range(10):
        # test.write(i)  # 报错
        test.write(str(i) + '\n')



