# decorators allow us to modify the behaviour of a function without changing any of its code

def func(string):
    def wrapper():
        print('Started')
        print(string)
        print('Ended')

    # returning wrapper() gives a function ready to be used so creating a variable of the function will run it
    # if you return wrapper then you return the address and memory of the function so that it can be used later
    # when called and is not immediately run when it is mentioned
    return wrapper


x = func('hello')
print(x)
x()
print('-------')


# using return wrapper() would run wrapper() even if you only wrote x = func('hello')

# this is an another example where a func3 is passed as a parameter to func2 and then run when wrapper
# is called by calling func2 and passing func3

def func(f):
    def wrapper():
        print('Started')
        f()
        print('Ended')

    return wrapper


# this is a decorator where you do @nameoffunction. There are other decorators as well and you can have multiple
# decorators on a function. It makes the function below be passed to the decorator's function so that when func3()
# is called it will be called as func2(func3)
@func
def func2():
    print('I am func2')


@func
def func3():
    print('I am func3')


# Instead of having to call func2 with different parameters and then pass func3 or func4 we can make
# it so that we call func3 or func4 and it gives us that result of func2(func3 or func4)

# func3 = func2(func3) # <---- without the decorator you would have to write this to assign the result of func3
# to be func2(func3), with the decorator it knows that this is what you want to do
# func4 = func2(func2)

func2()
print('--------')
func3()
print('--------')


# then when you introduce parameters into func3 it becomes more complicated
# the parameters in wrapper must be the same as the parameters of the received function
# to func which is either func2 or func3 in this case.
# if we passed x to wrapper and then passed x to f() then it would work and we could
# run something such as func2('hello') but then this would defeat the purpose of decorators
# because then if we wanted to use a function that didn't have any parameters then it would
# cause an error because func3 would have no parameters but wrapper would expect one

# this is the code where wrapper takes a function and decorators would become useless
def func4(f):
    def wrapper(x):
        print('Started')
        f(x)
        print('Ended')

    return wrapper


@func4
def func5(x):
    print(x)


@func4
def func6():
    print('I am func6')


func5('hello')
print('--------')


# func6() # <--- causes an error because of a expected parameter being unfufilled


# the solution is to use *args and **kwargs where you don't know how many parameters you will take

def func7(f):
    def wrapper(*args, **kwargs):
        print('Started')
        rv = f(*args, **kwargs)
        print('Ended')
        return rv

    return wrapper


@func7
def func8(x):
    print(x)


@func7
def func9(x, y):
    print(x)
    # to be able to return something you have to store the f(parameters) and then return the result
    # we also have to store it as a variable and then print it because otherwise it wont return anything
    # the x wil be told to print when rv = parameters and y will be told to wait if it is returned at the end
    # we can use this to not return anything or to return y depending on how it is called
    return y


func8(1)
print('------')
func9(2, 3)  # <----- this 3 won't be used because it is the return parameter and this won't return anything
print('------')
x = func9(3, 4)
print(x)
print('------')

# this is how we can use decorators to work out how long a function takes to run
import time


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        rv = f()
        total = time.time() - start
        print('Time: ', total, ' seconds')
        return rv

    return wrapper


# @timer passes test to timer and test will then be run as f(test) and we can see how long it takes
@timer
def test():
    for _ in range(1000):
        pass


test()
