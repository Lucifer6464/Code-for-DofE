class Dog():
    # class variables that are static (left unchanged) are typically created at the top of the class
    # this is so they can be accessed from anywhere in the class are are not changed
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    # methods with a @ on top of a function at the start are called decorators

    # classmethods are a special type of methods that can be called on a class
    # cls is the name of the class, it implicitly refers to Dog
    # using classmethod means you can call a function on the name of a class (cls refers to Dog)
    # it is called cls on convention but can be anything
    # they are useful for accessing class variables without having to create an instance of a class

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    # with staticmethods we don't have to refer to the class or create any instances of the class
    # we don't use any attributes in a staticmethod so we don't pass self either
    # staticmethods can be useful when you don't want to make any attributes but want to import a class
    # from a module to another and just call it directly from the main module

    @staticmethod
    def talk(n):
        for _ in range(n):
            print('Woof!')


Oscar = Dog('Oscar')
Bob = Dog('Bob')

# this will print the memory and address of the amount of dogs (in this case 2, Bob and Oscar)
print(Dog.dogs)

# this will print the same thing as Dog.dogs because dogs[] is being added to each time a Dog is created and we have
# created two dogs (Oscar and Bob)
print(Oscar.dogs)

# prints the amount of dogs created from an instance (Oscar) of Dogs
print(Oscar.num_dogs())

# prints the amount of dogs directly from the class, you can do it as it is above but it is a feature that you
# can call it without having to do it through an instance of the class
print(Dog.num_dogs())

print(Dog.talk(3))
