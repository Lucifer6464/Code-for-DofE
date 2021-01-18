# you can have parameters preset to a value so they don't have to take a value when invoked unless you want to

def func(name, special_number='64'):
    if special_number == '64':
        print('Correct, ' + name)
    else:
        print('Incorrect, ' + name)


func('Oscar')
print('-------------------')


def func2(name, special_number='64'):
    if special_number == '64':
        print('Correct, ' + name)
    else:
        print('Incorrect, ' + name)


func2('Oscar', '64')
print('-------------------')


def func3(name, special_number='64'):
    if special_number == '64':
        print('Correct, ' + name)
    else:
        print('Incorrect, ' + name)


func3('Oscar', 32)

# however, if you have two optional parameters you have to specify both if you want the second one to be included
print('-------------------')


def func4(name='Jeff', special_number='64'):
    if special_number == '64':
        print('Correct, ' + name)
    else:
        print('Incorrect, ' + name)


func4('Oscar', '32')