# Global means it can be used anywhere
# Local means it was created in a function

# It is a good idea to have few global variables that functions depend on because otherwise when importing it to
# another file it will try to reference that global variable and wont be able to, you could import all global
# variables from a settings file if there are a lot of necessary global variables

number = 9
newNumber = 12
loop = True


def func(x):
    # newNumber is a local variable to func
    newNumber = 10
    print(f'newNumber ({newNumber}) is being printed in its local function')
    print(f'Global variables are still accessible ({number})')
    print(f'Global variables are still accessible ({loop})')
    if x == 5:
        return newNumber


# print(newNumber) # <---- raises an error that it is not defined
func(3)
print('----------')


# print(newNumber)  # <---- still wont work

def otherFunc():
    newNumber = 5
    # this creates a new variable called loop, if you wanted to change it then you would have to do 'global loop'
    # global loop # <------ uncommenting this would cause loop below to be changing the global variable loop
    loop = 100
    print(newNumber)


# it will print 5 because it is taking newNumber from the local function that is invoked and won't use the global
# number if there is a local one (newNumber is also a global variable)
otherFunc()
# loop will be true even if you
print(loop)
