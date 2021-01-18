from collections import Counter

# Default Python Containers
# list
# set
# dict
# tuple

# Collections adds 5 new containers to python
# counter (used in this module)
# deque
# namedTuple()
# orderedDict
# defaultDict

# the argument given to counter is any container or string
# counter will return a dictionary labeling each element in order from 1 upwards

# it will count four characters in the string
c = Counter('four')
print(c)
# it will count four elements in the list
c = Counter([1, 2, 3, 4])
print(c)
# it will count four keys in the dictionary
c = Counter({'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(c)
print('-----------')
# you can also create a limited kind of a key and value object in a Counter that can be better
# than a Dictionary in some cases in that it will return 0 if the element does not exist
c = Counter(cats=4, dogs=7)
print(c['cats'])
# when the element does not exist it will return 0 instead of, like a dictionary, it would give an error
print(c['cows'])

# print all of the elements and show them how many times their value is
print(list(c.elements()))
# print the most common key. This can be used for any place e.g. 2nd most common elements e.t.c.
print(c.most_common(1))
print(c.most_common(2))
print('--------------')

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']
# this will subtract c and each value from the frequency of each corresponding key in d
c.subtract(d)
print(c)
# this will add c and d
c.update(d)
print(c)
# removes all elements in the Counter
c.clear()
print(c)
print('------------')

# you can perform mathematical operations between two counters such as +, -, intersection and union
# if their value is less than 0 they wont be displayed
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(['a', 'b', 'b', 'c'])

print(c + d)
print(c - d)
# prints common elements in each list (intersection)
print(c & d)
# prints all elements in each list (if they have a value e.g. >0) (union)
print(c | d)
