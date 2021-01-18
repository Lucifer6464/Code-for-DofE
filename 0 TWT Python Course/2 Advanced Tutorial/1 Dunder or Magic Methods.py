# Dunder stands for double underscore

x = [1, 2, 3]
y = [4, 5]

# at an intermediate understanding we just take this for granted that we can do all these things
# in python for granted (adding lists, finding the length of lists and on)
print(x + y)
print(len(x))
print(x[1])


# in fact all of these abilities are implemented on a list in such a way that it tells the list what to do
# facing something like this


class Person:
    # __init__ is a dunder method
    def __init__(self, name):
        self.name = name

    # causes the name to be returned as something meaningful
    def __repr__(self):
        return f'Person({self.name})'

    # multiplies the amount of times the name is printed if called
    def __mul__(self, x):
        if type(x) is not int:
            raise Exception('Invalid Argument, must be type int')
        self.name = self.name * x

    # we can cause it to print something if an instance of the class is called
    # with a parameter (y) to be printed
    def __call__(self, y):
        print(y)

    # find the length of something
    def __len__(self):
        return len(self.name)


p = Person('Oscar')
# by default, when this is called it will print the address and memory of Person
# because we have not told it to do otherwise
# repr
print(p)

# mul
p * 4
print(p)

# call
p(4)

# len
# without coding this dunder method into our class it would return an error
print(len(p))

# there is a large list of dunder methods in the python documentation

from queue import Queue as q
import inspect


# queue does not have the dunder method __repr__ but you can write it into queue yourself
class Queue(q):
    def __repr__(self):
        # qsize is the length of self.queue (0 until you add to it)
        return f'Queue({self._qsize()})'

    # creating functionality to add to the queue
    def __add__(self, item):
        self.put(item)

    # creating functionality to remove from the queue
    def __sub__(self, item):
        self.get()

qu = Queue()
# adding something to the queue just adds one object no matter what you add
qu + 'hello'
qu + 4
# this will remove a value from the queue no matter what you put after the minus sign
qu - 'g'
print(qu)
