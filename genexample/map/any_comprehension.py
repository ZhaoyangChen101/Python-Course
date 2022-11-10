from data import people, plants_list, plants_dict

# people = []

if bool(people) and all([person[1] for person in people]):  # all returns True if all emails aren't empty.
    # all returns False as soon as a False value is found
    # any returns True as soon as a True value is found
    print("Sending email")
else:
    print("User must edit the list of recipients")

if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grasses")
else:
    print("No grass in this pack")

print()

# if any([plant.plant_type == "Grass" for plant in plants_dict.values()]):
if any(plant.plant_type == "Grass" for plant in plants_dict.values()):
    print("This pack contains grasses")
else:
    print("No grass in the dict")

# 小结：any all接受的是iterable，所以generator也是可以的，不是非要list。

if any(plants_dict[key].plant_type == "Grass" for key in plants_dict):
    print("This pack contains grasses")
else:
    print("No grass in the dict")