# you can put this class inside of a function and it doesn't cause an error is because of how
# python runs. It actually works because classes are objects

# properties of objects are that we can
# interact with it at runtime
# pass it around through parameters and variables
# we can store, save, modify and interact with it

def hello():
    class Hi:
        pass

    return Hi


# classes are known for creating objects for us but classes are actually an object themselves
# this means there was some higher level class that created the object for us

# classes define all the attributes, methods, things that are allowed, operations that can be performed
# a metaclass define the rules for a class. It happens automatically when you create a class

class Test:
    pass


# it doesn't explicitly say object when you print it here
print(Test)
# it does say that it is an object in the address and memory
print(Test())

# all objects have a type
print(type(2))

# when you print the type of an instance of a class it will print __main__.Test
# because Test is an attribute of the class __main__
# instances of a class are objects, not classes anymore so they will print here that
# # they are an attribute of __main__ because that is what they refer to when they refer to
# the class they are an instance of
print(type(Test()))

# however, when you ask for the type of a class it will print that it is of type 'type'
print(type(Test))

# type is also of the type 'type'. It created itself essentially
print(type(type))
print('---------')


# this is because type is the metaclass of Test and all other classes

# logically you should also be able to use the metaclass type to create all objects and you can
# although it is slightly strange syntax due to backwards compatibility

class Foo:
    def show(self):
        print('hi')


def add_attrbute(self):
    self.z = 9


# when having a function as a attribute it is not called when referenced
# each superclass must have a comma after it even if there is only one superclass
# all the attributes are in a dictionary
# ClassName = nameofmetaclass('nameofclass', (superclass,), {attributes})
Hello = type('HelloCLass', (Foo,), {'x': 5, 'add_attribute': add_attrbute})

print(type(Hello))
# when you reference a class you must use the first name.
# when a class' name is printed it will be the string name
print(type(Hello()))

h = Hello()
print(h.x)

# inheritance also works exactly the same as normal classes
h.show()

# just like all other classes, you can define attributes outside of the class
h.y = 12
print(h.y)

# the two ways of creating a class below are exactly the same
Bar = type('Bar', (), {})


class Bar:
    pass


# you can also make your own metaclass. It has to inherit from type (there are other ways) and
# it can change object properties
class Meta(type):
    # __new__ is the first thing that is called when an object is created
    # you can change its values and how a class is created.
    # __init__ simply defines values and takes parameters and initialises it
    # the class __new__ creates the essence of the class

    # we have defined the parameters so that on creation all classes need
    # a class_name, base(s) and attribute(s)
    def __new__(self, class_name, bases, attrs):
        print(attrs)
        # blank dictionary that will represent our attributes
        a = {}
        # this is very powerful and is referred to as magic because you can stop
        # classes from using an attribute and influence an of their properties
        for name, val in attrs.items():
            # if the name startswith a __ then replace it with its proper value
            # and leave the dunder method alone because making it uppercase will
            # stop it being a dunder method
            if name.startswith('__'):
                a[name] = val
            # if it doesn't start with a __ then change its name to uppercase
            # with the corresponding value
            else:
                a[name.upper()] = val
        print(a)
        return type(class_name, bases, a)


# here the metaclass has been changed
class Dog(metaclass=Meta):
    x = 5
    y = 8

    def hello(self):
        print('hi')


# even without creating an instance of the class, all the properties of the class will be
# printed because it is told to print the attributes in def __new__ if the metaclass is Meta
d = Dog()
# print(d.x) # <--- this will create an attribute error because x was turned to X when we turned all values
# (unless they started with __) to uppercase
# all attributes in Meta
# it says it has an error because it cannot directly find X in Dog but when it actually searches it will find that
# Meta modified x to X
print(d.X)
print(d.HELLO())
