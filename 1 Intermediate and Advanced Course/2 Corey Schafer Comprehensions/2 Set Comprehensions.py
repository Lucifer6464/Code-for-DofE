nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# non comprehension
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

# comprehension
my_set = {n for n in nums}
print(my_set)