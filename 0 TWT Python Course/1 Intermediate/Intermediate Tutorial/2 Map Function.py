numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(x):
    return x ** 2


# the way to return a list with every value squared without map, it takes far more code
# and you have to create a copy of a list instead of changing the original one
squaredList = []
for x in numbers:
    squaredList.append(square(x))
print(squaredList)

print(list(map(square, numbers)))

# you could also use list comprehension for a just as good result

print([square(x) for x in numbers])

# here's a way to do it with list comprehensions only for even numbers

print([square(x) for x in numbers if x % 2 == 0])


