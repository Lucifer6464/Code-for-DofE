# this includes more advanced uses of optional parameters

def func(word, add=5, freq=1):
    print(word * (freq + add))


call = func('tim', 2)


# useful example
class Car():
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display(self, showAll=True):
        if showAll:
            print('This is a %s %s from %s, it is %s and has %s kms.' % (
                self.make, self.model, self.year, self.condition, self.kms))
        else:
            print('This is a car from %s %s from %s.' % (self.make, self.model, self.year))


whip = Car('Ford', 'Fusion', 2012)
whip.display(False)
