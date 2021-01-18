# public classes are classes that can be seen and modified (if specified to be mutable) anywhere by other classes
# private classes are classes that cannot be seen or modified anywhere by other classes

# this terminology public and private is only convention and not a real feature in python, you can change
# private classes anywhere in python but is it just a sign that it was not created to be modified

# you can also have private functions in python by adding a _ before their name

# having an underscore at the start of a class name signifies that it is not meant to be
class _Private:
    def __init__(self, name):
        self.name = name


class NotPrivate:
    def __init__(self, name):
        self.name = name
        # _Private is still seen here by NotPrivate, as said, _ before a name is just convention and not a feature
        self.priv = _Private(name)

    def _display(self):
        print('This is a private function in a class')

    def display(self):
        print('This is a public function in a class')


priv = _Private('bob')
notPriv = NotPrivate('Oscar')

# private functions and classes can still be used but it is just a convention and notice although
# it does give you a warning you are accessing a private member of the class
print(notPriv._display())
print(notPriv.display())

print(_Private)
