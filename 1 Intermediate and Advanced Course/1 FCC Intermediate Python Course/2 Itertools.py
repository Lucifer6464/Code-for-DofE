from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, \
    cycle, repeat

# itertools are modules for handling iterators. Iterators and data types that can be iterated over in a for loop
# we will be looking at the itertools:
# product, permutations, combinations, accumulate, groupby and infinite iterators

a = [1, 2]
b = [3, 4]
c = [3]
d = [1, 2, 3]
e = [1, 2, 3, 4]
# product will give all of the possibilities with numbers in the first set
# as first and then works out the possibilities with the other set's digits
# at the end. Repeat= will make each possibility have twice as many digits
# in a pattern
prod = product(a, b)
print(list(prod))

prod = product(a, c, repeat=2)
print(list(prod))
print('---------')

# permutations will give all possible ordering of an input
perm = permutations(d)
print(list(perm))

# you can specify a max length of each possibility as well, if it is longer than what was
# expected then it will just remove digits at the end
# it is is shorter than expected when it will return a empty list
perm = permutations(d, 2)
print(list(perm))
perm = permutations(d, 4)
print(list(perm))
print('---------')

# combinations will give all possible combinations with a mandatory specified length

comb = combinations(d, 2)
print(list(comb))

# combinations with replacement will create possibilities with the same number multiple times
comb_wr = combinations_with_replacement(d, 2)
print(list(comb_wr))
print('---------')
# accumulate will return accumulated sums, it is similar to the fibonacci sequence but will return a list with the
# first, then first two then 2nd and 3rd digits added together and so on
acc = accumulate(e)
print(e)
print(list(acc))

# you can use operators to cause the digits to multiply instead of add
import operator

acc = accumulate(e, func=operator.mul)
print(e)
print(list(acc))

# return the current highest digit
f = [1, 2, 5, 3, 4]
acc = accumulate(f, func=max)
print(f)
print(list(acc))

# groupby returns keys and groups (seciton of a list) from an iterable
# e will be passed to smaller_than_three
group_obj = groupby(e, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

# grouping people by age

people = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25}, {'name': 'Lisa', 'age': 27},
          {'name': 'Claire', 'age': 28}]

# grouping based on those of the same age
group_obj = groupby(people, key=lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))  #
print('--------')
# count wil create an infinite loop starting at an given value (10 in this case)
for i in count(10):
    print(i)
    if i == 15:
        break
print('---------')
# cycle will infinitely print a iterable and cycle through it, repeating when it finishes
a = [1, 2, 3]
x = 0
for i in cycle(a):
    print(i)
    x += 1
    if x > 7:
        break
    # if i is bigger than three then it will run infinitely because then it will go past the list
    # so this is not a good way to stop a cycle
    # if i == 3:
    #     break
print('----------')
# repeat will just repeat something forever, you can have a condition for how many times it should
# repeat as the second argument. repeat(what to repeat, how many times)
for i in repeat(1, 5):
    print(i)
