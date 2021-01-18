from collections import OrderedDict, defaultdict

# ordered dict is almost useless nowadays but in older versions of python dictionaries wouldn't
# remember their order

ordered_dict = OrderedDict()
# in older versions of python  it would be in a random order
# dictionary['key'] = value
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

# python 3.7+ support this correct ordering now so you can just use a normal dictionary
ordered_dict = {}
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['a'] = 1
print(ordered_dict)

# defaultdicts have default values if the key has not been set yet

# you can set a default value for it to take if you look for the value of a key that does not exist
# the default value for an integer is 0 so that would be what it would print
# the default value for a float is 0.0
# the default value for containers is empty
d = defaultdict(float)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['c'])
d = defaultdict(int)
print(d['c'])
d = defaultdict(list)
print(d['c'])
