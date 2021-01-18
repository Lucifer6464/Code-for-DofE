from collections import namedtuple

# Named Tuples allow the ability to access fields (element) by name rather than position index

# named tuple takes the name and then the elements with all the elements separated by a space
Point = namedtuple('Point', 'x gy z')

# newtuples are treated as classes, you have to create an instance of it to use it
# 3, 4, 5 splits up the string and assigns each element in the string to each character is split up and
# assigned to each integer
newP = Point(3, 4, 5)
print(newP)

# you can also split up a list in this same way

Point = namedtuple('Point', ['x', 'gy', 'z'])
newP = Point(3, 4, 5)
print(newP)

# you can also split it up in the form of a dictionary. It will take the key names and ignore the values
# you cannot create a value in namedtuple() and then not give a value for it when creating an
# instance otherwise it will crash

Point = namedtuple('Point', {'x': 0, 'gy': 0, 'z': 0})
newP = Point(3, 4, 5)
print(newP)
# you can print an individual aspects of it (this can be done using any string on container passed to namedtuple)
print(newP.x)
print(newP[1])
# you can print an ordered dictionary from it (this can be done using any string on container passed to namedtuple)
print(newP._asdict())
# print the fields
print(newP._fields)

# you can change a value
newP = newP._replace(z=6)
print(newP)

# you can create a new point this way and it will make the keys the values given to the namedtuple()
# and the values will be the elements passed to it
p2 = Point._make(['a', 'b', 'c'])
print(p2)