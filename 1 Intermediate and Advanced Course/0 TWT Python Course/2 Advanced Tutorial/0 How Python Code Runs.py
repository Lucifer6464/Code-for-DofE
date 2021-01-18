# python is a interpreted coding language
# python is also complied into byte code before it is interpreted

# the python compiler takes high level code (furthest away from the hardware) and
# translates it into byte code which is easier for the computer to read

# codes like C only need a compiler as the code is directly translated into machine
# code so that it can be run directly on the os and no interpreter is needed

# in  python, when you run the code, it is translated into bytecode, which can be checked
# for errors, and if there are no errors, then the interpreter converts it into machine code
# line by line in real-time and then this is run for you too see

# this code wont cause an error because the compiler only checks for code that is to be run and
# produce something and if it causes an error but only checks the syntax for errors
# this can be an error if you don't test your code and then when it comes to running it there are
# a lot of errors

# Since the code is executed live, each piece of code is stored at an address and memory to be accessed
# an interacted with in real-time

# this works since the compiler does not pick up that bark is not a method and cause an error
# because the compiler only checks python syntax for errors and then code is checked for errors at runtime,
# and this code isn't used so it won't get an error
class Dog:
    def __init__(self):
        self.bark()


# dog = Dog() # <----- this would cause an attribute error because it would now have to check the code and when it
# goes to check what bark() is referencing inside of Dog it would come back with nothing and cause an error


# this is a feature in python because the compiler doesn't care how your code is written
# as long as the syntax is correct, you can have whatever code you want

# this is a cool feature of python - you can make anything you want, classes inside functions inside classes e.t.c
# as long as your syntax is correct. This can't be done in most other languages
def make_class(x):
    class Cat:
        def __init__(self, name):
            self.name = name

        def print_value(self):
            print(x)

    # this refers to the class, not the object
    return Cat


cls = make_class(10)
print(cls)
# creates an instance of the class because cls is technically just a class when accessing it
c = cls('Oscar')
c.print_value()

# another instance of a block of code inside of something else
# not quite sure when it would be useful but it is thing you can do in python
for i in range(10):
    def show():
        print(i)


    show()


# another way of putting code blocks inside of code blocks
# again, not sure when it would be useful but it is a thing in python
def func(x):
    if x == 1:
        def rv():
            print('x is 1')
    else:
        def rv():
            print(' x is not 1')

    return rv


new_func = func(1)
new_func()

# memory address/location of our function. We can find this on any variable, function, class, statement e.t.c.
# this is how we are able to loop around our python code with returning variables and having accessible code
# inside of code
print(id(new_func))

import inspect

# you can see all of the members and things inside of new_func and their memory and address
print(inspect.getmembers(new_func))
print('----------')
# you can see the source code of any object, this is quite useful for looking at what code is what
print(inspect.getsource(new_func))

# you can see all of the source code of a code in a module as well
# queue is a built in data structure in python
from queue import Queue

# print(inspect.getsource(Queue))# <----- this is a large class and you can see all of the code just
# by printing it externally
