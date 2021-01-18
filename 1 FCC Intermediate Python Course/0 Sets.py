# this is a basic container in python that wasn't included in my beginners course but also
# are very rarely used

# sets are unordered, mutable and don't allow duplicates

# created
# 3 is a duplicate so it will be ignored
myset = {1, 2, 3, 3}

print(myset)
myset = set('Hello')
# it is unordered so the letters will be scrambled
print(myset)

# this is not an empty set because it is recognised as a dictionary
myset = {}

# this is an empty set below
myset = set()
print(myset)
# you can add to sets and mutate them
myset.add(1)
myset.add(2)
print(myset)

# you can remove certain elements and if you try to remove one that doesn't exist then nothing will happen
myset.discard(2)
myset.discard(3)
print(myset)
myset.add(2)

# you can pop out a random value
print(myset.pop())
# the one
print(myset)

# clears the set
myset.clear()

myset.add(1)
myset.add(2)
myset.add(3)

for i in myset:
    print(i)

if 1 in myset:
    print('one is in myset')

# union and intersection

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(primes)
print(i)

# .difference and .symmetric_difference will return a new set so they will not modify the old set
# print numbers in the first set that are not in the second set
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

# A u B'
diff = setA.difference(setB)
print(diff)

# A' u B
diff = setB.difference(setA)
print(diff)

# symmetric difference is everything in both sets but not the intersection (same either way around)

# A' n B'
diff = setB.symmetric_difference(setA)
print(diff)

# adding new numbers to a set that are not already there

setA.update(setB)
print(setA)

# put the set back to normal
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# this puts all elements into setA that are also it setB and remove all other elements from setA
setA.intersection_update(setB)
print(setA)

# put the set back to normal
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# removes all elements found in another set
setA.difference_update(setB)
print(setA)

# put the set back to normal
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}

# removes elements that are in both sets
setA.symmetric_difference_update(setB)
print(setA)

# check if a set is a subset or superset of something
print(setA.issubset(setB))
print(setA.issuperset(setB))

# check if two sets have do not have an intersection
print(setA.isdisjoint(setB))

# modifying a copy will also modify the original set
setC = {1, 2, 3}
setD = setC
print(setD)
setD.add(4)
print(setC)
print(setD)

# to fix this you have to use the .copy() method when copying or make the copied set an argument
setD = setC.copy()
# or you can do
setD = set(setC)
setD.add(5)
print(setC)
print(setD)

# a frozen set is an immutable version of a normal set
a = frozenset([1,2,3,4])
print(a)
# a.remove(1) # <--- this will give an AttributeError because remove is not an attribute of a frozenset
