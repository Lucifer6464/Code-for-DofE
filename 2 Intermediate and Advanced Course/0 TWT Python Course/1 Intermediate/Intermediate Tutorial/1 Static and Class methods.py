# another use of staticmethod and classmethod

class Person():
    population = 27

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


newPerson = Person('Oscar', 13)
print(newPerson.display())

print(Person.isAdult(64))
print(Person.getPopulation())
