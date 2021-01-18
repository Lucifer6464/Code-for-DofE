# generators are better ways of looping through lists

# x = [i ** 2 for i in range(100000000000)]
#
# for el in x:
#     print(el)

# we are working on our computers ram so although most people will never fill it up we do have to understand
# where our programs are running to understand physical limitations. With a program like this your computer should
# fill up its RAM and crash. However, my computer decided not to crash though because I think there is something in
# my cpu or ram or update in pycharm that has something that stops it from crashing and instead it just doesn't
# run and stays at 10gb of ram usage until i stop the program. I increased the numbers to 10^10000 and it still
# wouldn't crash. I should get a memory error in theory

# to fix this, so it doesn't cause my cpu to stay at 66 degrees Celsius until I stop the program, we can't think about
# the code and find a better alternative that produces the same result
# better code would be

# for i in range(1000000):
#     print(i * 2)


# generators allow you to look at one number at a time instead of a whole sequence so the second bit of code is a good
# way to think about generators in comparison to the first program which looked at all of the numbers and
# then run the code. However, the code above isn't quite a generator, proper generators are more complicated ways of
# looping through lists

# this class gives you a better idea of what a generator is as it goes through each item at a time
# but it still isn't a proper generator


class Gen:
    def __init__(self, n):
        self.n = n
        self.last = 0

    def __next__(self):
        return self.next()

    def next(self):
        if self.last == self.n:
            raise StopIteration()
        rv = self.last ** 2
        self.last += 1
        return rv


# g = Gen(100)
# while True:
#     try:
#         print(next(g))
#     except StopIteration:
#         break


# All generators must:

# contain one or more yield statements
# returns an object when called but does not execute immediately
# __iter__() and __next__() are implemented automatically
# once it yields it is paused and control is given to the caller
# local variables and their states are remembered between successive calls
# when it terminates, StopIteration is raised


# yield is a pause and stores the information in memory. return is a stop
# yielding also causes the data printed to conform to measures it puts up
# if yield i ** 2 is written then all values will be squared
# if you yield a number then every value it says will be printed
# the amount of times the generator is to run
# you can have multiple yield keywords to make the output have multiple ways of being
# printed depending on what the yields are
import sys


def gen(n):
    for i in range(n):
        yield i + + 10
        yield 100


x = [i ** 2 for i in range(1000)]
g = gen(1000)

# looping through the first three values using next()
print(next(g))
print(next(g))
print(next(g))
print('-------')

for i in g:
    print(i)

# you can see the amount of bytes passed in for each loop and you can see the huge difference
# that generators make to the run speed of loops
print('--------')
print(sys.getsizeof(x))
print(sys.getsizeof(g))
# there is much more to generators that can be read in the documentation of generators
