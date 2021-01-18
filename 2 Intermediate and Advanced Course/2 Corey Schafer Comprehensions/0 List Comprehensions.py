# recap of list comprehensions

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# non comprehension
my_list = []
for n in nums:
    my_list.append(n)
print(my_list)

# comprehension
my_list = [n for n in nums]
print(my_list)

# more complicated

# non comprehension
my_list = []
for n in nums:
    my_list.append(n * n)
print(my_list)

# comprehension
my_list = [n * n for n in nums]
print(my_list)

# making this using lambda and map
# comprehensions reduce lots of the cases where map and lambda are useful because comprehensions
# are easier to read. Simple is better than complex
my_list = list(map(lambda n: n * n, nums))
print(my_list)

# more complicated

# non comprehension
my_list = []
for n in nums:
    if n % 2 == 0:
        my_list.append(n)
print(my_list)

# comprehension
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# using filter and lambda
my_list = list(filter(lambda n: n % 2 == 0, nums))
print(my_list)

# more complicated
# this is a nested for loop. Flat is better than nested.
# non comprehension
my_list = []
for letter in 'abcd':
    for num in range(4):
        my_list.append((letter, num))
print(my_list)

# outer list comes first, it reads left to right and then assigns the properties of the
# first values and appends them to the list it is equal to
# comprehension
my_list = [(letter, num) for letter in 'abcd' for num in range(4)]
