shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

item_to_find = "apple"
found_at = None

# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break
#  代码简单，但是个人看法，不比上面的效率高
if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at is not None:
    print("Item found at position {}".format(found_at))
else:
    print("{} not found".format(item_to_find))
