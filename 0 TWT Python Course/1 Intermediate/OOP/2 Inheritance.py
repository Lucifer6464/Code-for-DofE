class Dog():
    def __init__(self, name, age):
        # init will run things when a Dog class is created, it doesn't have to be called
        # these self. are attributes of the class they are in
        self.name = name
        self.age = age

    def speak(self):
        print('Hi I am a', self.name, 'and I am', self.age, 'years old')

    def talk(self):
        print('Woof!')


# adding something in the bracket means it is a parent class
class Cat(Dog):
    def __init__(self, name, age, color):
        # super will take the attributes from its 'super' class, which is Dog in this case
        super().__init__(name, age)
        self.color = color
        # you can overwrite attributes even if you have taken them from a parent class
        self.name = 'Overwrite Name Cat'

    # this overwrites the talk function in Dog
    def talk(self):
        print('Meow!')


dog = Dog('Dog', 4)
dog.speak()
dog.talk()

cat = Cat('Cat', 13, 'orange')
cat.speak()
cat.talk()


# another example of inheritance
class Vehicle():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillTank(self):
        self.gas = 121

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('BEEP')


class Van(Car):
    def __init__(self, price, gas, color, speed, tires):
        super().__init__(price, gas, color, speed)
        self.tires = tires

    def beep(self):
        print('HONK')
