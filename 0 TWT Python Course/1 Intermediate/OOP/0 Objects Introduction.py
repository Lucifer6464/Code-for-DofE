import turtle
# All things like strings, booleans e.t.c. are objects

x = 10
y = 'something'

print(type(x))  # prints <class 'int'>
print(type(y))  # prints <class 'str'>

# it prints the type of them in this way because when it creates them it is actually
# creating an instance of an object, x = 10 means x is equal to an instance of the
# int object and its value is 10

# this creates a new instance of a turtle object
# Turtle() is called a constructor
turtle = turtle.Turtle()

# upper is a method for strings only to transform them too all upper case
print(y.upper())
# print(x.upper()) # <------ this will cause an error because upper is not a method for integers

# you can also have methods where they return values such as
print(y.replace('s', 'this is s'))

def func(x):
    return x+1

print(func(5))


