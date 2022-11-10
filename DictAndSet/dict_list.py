available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "mouse mat",
                   "6": "hdmi cable",
                   "7": "dvd drive",
                   }

computer_parts = []
current_choice = None
while current_choice != "0":
    if current_choice in available_parts:   # `in` in dictionaries only checks keys
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
        if chosen_part not in computer_parts:
            computer_parts.append(chosen_part)
        else: # remove the part if it exists
            print(f"Removing {chosen_part}")
            computer_parts.remove(chosen_part)

    else:
        print("Please add options from the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")


