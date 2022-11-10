shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'rice']

# for item in shopping_list:
#     if item != "spam":
#         print("buy " + item)

for item in shopping_list:
    if item == 'spam':
        #continue
        break
    print("buy " + item)

