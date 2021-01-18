# the * sign can be used for:

# multiplication and indices
# creation of lists or tuples with repeated elements
# *args and **kwargs
# keyword only parameters
# unpacking lists, tuples and dictionaries into function arguments
# unpacking and merging containers into a list

# lists with repeated elements

# this creates a list with 10 0s and 1s each
zeros = [0, 1] * 10
print(zeros)
zeros = (0, 1) * 10
print(zeros)
zeros = '01' * 10
print(zeros)

print('-------')


# *args and **kwargs

# you can name args and kwargs whatever you want but they are
# normally called args and kwargs
# a parameter with * at the start means it is a list and you
# are now able to pass any number of positional arguments (extra parameters) to a function
# and a parameter with ** at the start means it is a dictionary and you
# can now pass any number of keyword arguments (parameter=) to the function

def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])


foo(1, 2, 3, 4, 5, six=6, seven=7)
print('----------')


# if you have a * and then more parameters, all parameters afterwards are keyword arguments
def foo(a, b, *, c):
    print(a, b, c)


foo(1, 2, c=3)
print('--------')


# unpacking lists, tuples and dictionaries into functions arguments
# this is where you can give lists or tuples to functions as arguments by unpacking them into separate
# elements to be given to the function. The list must have the same amount of elements as parameters
# there are to fill

def foo(a, b, c):
    print(a, b, c)


# one star before the name of the list when passed to the function will unpack it
mylist = [0, 1, 2]
foo(*mylist)
# same with tuples
mylist = (0, 1, 2)
foo(*mylist)

# two stars before the name of the dictionary will unpack it
# the name of the keys must match the name of the parameters amd the value
# will be the value passed to each parameter
mydict = {'a': 1, 'b': 2, 'c': 3}
foo(**mydict)

# unpacking containers

numbers = [1, 2, 3, 4, 5, 6]

# if the * is at the start this will unpack all elements bar the last into a list with the first given element and
# last element in the list will be unpacked as its own type into the second given element
*beginning, last = numbers
print(beginning)
print(last)
print('-------')

# if the * is at the start then the first element will be unpacked as its own type into the first given element
# and the rest will be unpacked as a list into the second given elememt#
beginning, *last = numbers
print(beginning)
print(last)
print('-------')

# you could have three or up to six variables where the one with the * at the given element which should take the list
beginning, *middle, last = numbers
print(beginning)
print(middle)
print(last)
print('-------')

# merging containers

# you can unpack a tuple, set and list and merge them into another list
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}

new_list = [*my_tuple, *my_list, *my_set]
print(new_list)
print('-------')

# you can unpack two or more dictionaries into another dictionary to merge them
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
