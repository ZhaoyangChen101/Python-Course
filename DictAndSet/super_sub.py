animals = {'Turtle',
           'Horse',
           'Robin',
           'Python',
           'Swallow',
           'Wren',
           'Aardvark',
           'Cat',
           }
birds = {'Robin', 'Swallow', 'Wren'}

print(f'birds is a subset of animals: {birds.issubset(animals)}')
print(f'animals is a superset of birds: {animals.issuperset(birds)}')

print(birds <= animals)
print(birds < animals)

print('*' * 80)

garden_birds = {'Swallow', 'Wren', 'Robin'}
print(garden_birds == birds)
print(garden_birds <= birds)
print(garden_birds < birds)

print('*' * 80)

more_birds = {'Wren', 'Burgie', 'Swallow'}
print(garden_birds >= more_birds)
print(garden_birds.isdisjoint(more_birds))