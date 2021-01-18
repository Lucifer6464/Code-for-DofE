# context managers, like most other things in this tutorial are something used at an intermediate and beginner level but
# you weren't aware of them. Context managers are also quite useful and commonly used in high level code

# the issue with the code is that if the second line has an error in it then
# the third line won't be closed and you can get corruption this way
# if multiple people are working on the same file
# you could use a try and finally (try to do this and whether this causes
# an error or runs, do this afterwards) but there is a better way using
# a context manager

# file = open('6 file.txt', 'w')
# try:
#     file.write('hello')
# except:
#     file.close()
#     print('There was an error with writing to the file')
# finally:
#     file.close()

# better code using a context manager that will close no matter what happens
# context managers are a better version of a try:finally: block in this case
# they allow you to run some code an then some other code, regardless
# of whether the first section of code succeeds or not
# this is useful for file opening and locks and threading

# with open('file.txt', 'r') as file:
#     file.write('hello')

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print('enter')
        return self.file

    def __exit__(self, type, value, traceback):
        # print the crash information
        print(f'{type}, {value}, {traceback}')
        print('exit')
        self.file.close()
        # if you return True then it won't crash the program
        # a better idea is to look for certain types of errors
        # and then handle them such as a better idea would be
        # this still isn't a good idea to handle an error like
        # this but it is an example of how to handle crashes
        # and possibly ignore them
        # if type == NameError:
        #     return False
        return True


with File('6 file.txt', 'w') as f:
    print('middle')
    f.write('hello!')
    print('after writing')
    # after writing then it will exit and will exit before it crashes if there is an error
    # it will print exit and then raise the error
    error
print('------')

# quicker and easier way to make a context manager
from contextlib import contextmanager


@contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')


with file('6 file.txt', 'w') as f:
    print('middle')
    f.write('hello!')
    print('after writing')

# other things you can do with context managers are locks and threading
# this is where you prevent a resource from being accessed until a thread
# has given up its lock on something
# say you have a variable to be accessed by two threads, you can't access x at the
# same time by both threads so you can put a lock on a variable until the first
# thread is finished with it and then you can give it to the second thread
