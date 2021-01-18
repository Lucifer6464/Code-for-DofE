names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heroes = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

# zip lines up two lists so that the first one becomes the key and the second becomes the value

# non comprehension
superheroes = {}
for name, hero in zip(names, heroes):
    superheroes[name] = hero
print(superheroes)

# comprehension
superheroes = {name: hero for name, hero in zip(names, heroes)}
print(superheroes)

# you can add other things as well to the conditions
superheroes = {name:hero for name, hero in zip(names, heroes) if name != 'Peter'}
print(superheroes)