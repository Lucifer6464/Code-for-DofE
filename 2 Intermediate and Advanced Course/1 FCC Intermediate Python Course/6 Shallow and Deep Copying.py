import copy

# shallow copying is one level deep and only is only a reference of a nested child object
# deep copying is a fully independent copy

org = 5
cpy = org
# you can change it by reassigning it and it doesn't effect the other
cpy = 6
print(org)
print(cpy)
print('---------')

# this shallow copying can be problematic with lists and other mutable data types because
# changing one variable will affect the other(s)
org = [0, 1, 2, 3, 4]
cpy = org
cpy[0] = -10
print(cpy)
print(org)
print('--------')

# this is a shallow copy and won't work if we have a nested list
org = [0, 1, 2, 3, 4]
# this way
cpy = copy.copy(org)
# or this way
cpy = org.copy()
# or this way
cpy = list(org)
# or this way
cpy = org[:]
cpy[0] = -10
print(cpy)
print(org)
print('---------')

# it fails when a nested list appears
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)
print('--------')

# this is how to make a deep copy and will work with nested lists
org = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)
print('---------')


# copying custom objects with shallow copying
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person('Oscar', 64)
# shallow copy
p2 = copy.copy(p1)

p2.age = 28
print(p1.age)
print(p2.age)
print('---------')

# this wont work with a deeper structure
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Oscar', 64)
p2 = Person('Bob', 32)

company = Company(p1, p2)
company_clone = copy.copy(company)
company_clone.boss.age = 32
print(company_clone.boss.age)
print(company.boss.age)
print('---------')


# copying custom objects with deep copying
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person('Oscar', 64)
p2 = Person('Bob', 32)

company = Company(p1, p2)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 32
print(company_clone.boss.age)
print(company.boss.age)

