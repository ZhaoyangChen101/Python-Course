from contents import pantry, recipes


def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a tuple containing `item` and `amount` to the `data` list."""
    # if item in data:
    #     data[item] += amount  # augmented assignment
    # else:
    #     data[item] = amount
    # setdefault: 如果key在字典中，则返回对应的值；如果不在，则设置为逗号后的规定的值。
    data[item] = data.setdefault(item, 0) + amount  # setdefault终于被我找到了！
        
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}

# enumerate can be used for any iterable.
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}

while True:
    # display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
    print("0 - to finish")

    choice = input(": ")

    if choice == "0":
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0)
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
for things in shopping_list.items():
    print(things)
