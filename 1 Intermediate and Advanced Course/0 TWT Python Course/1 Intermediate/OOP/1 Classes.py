class Dog():
    def __init__(self, name, age):
        # init will run things when a Dog class is created, it doesn't have to be called
        # these self. are attributes of the class they are in
        self.name = name
        self.age = age
        self.list = ['this', 'is', 'a', 'list', 'in', 'a', 'class']
        print('I have been initialised')

    def speak(self):
        print('Hi I am', self.name, 'and I am', self.age, 'years old')

    def change_name(self, name):
        self.name = name
        print('My name is now', self.name)

    def add_weight(self, weight):
        # you can create self. outside of init but it isn't
        # convention unless it makes sense to create it outside of init
        self.weight = weight
        print('I am', self.weight, 'lbs')
        return 'you have to return something else it prints None if you call a function in a class'

# dog is an instance of Dog()
dog_oscar = Dog('Oscar', 35)
dog_oscar.speak()
dog_oscar.add_weight(324)
dog_oscar.change_name('Bob')

# you can print something specific and also changing something that is self will globally effect the variable
# if change_name is not called then this will print Oscar instead of Bob
print(dog_oscar.name)

print(dog_oscar.list)

print(dog_oscar.weight)
print(dog_oscar.add_weight(324))
