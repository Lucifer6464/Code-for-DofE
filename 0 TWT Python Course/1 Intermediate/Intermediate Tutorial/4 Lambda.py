# this can be written in a far quicker way using lambda
def func(x):
    return x + 5


print(func(2))

func2 = lambda x: x + 5

print(func2(2))


# using lambda in functions

def func3(x):
    func4 = lambda x: x + 5
    return func4(x) + 64


print(func3(2))

# it can take multiple parameters like an normal function

func3 = lambda x, y: x + y
print(func3(2, 2))

# easier way to do what was done in '3 Map Function.py' using lambda. If you use a function for one case then this is a
# better way to write the function

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(map(lambda x: x + 5, a))
print(b)

c = list(filter(lambda x: x % 2 == 0, a))
print(c)
