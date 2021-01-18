class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        # Multiplication is actually returning the scalar product so you don't need to return
        # a new object, just a number
        return self.x * p.x + self.y * p.y

    # try to get the magnitude of the point from the origin and can return if a number is something
    # in relation to another number
    def length(self):
        import math
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # greater than
    def __gt__(self, p):
        return self.length() > p.length()

    # greater than or equal to
    def __ge__(self, p):
        return self.length() >= p.length()

    # less than
    def __lt__(self, p):
        return self.length() < p.length()

    # less than or equal to
    def __le__(self, p):
        return self.length() <= p.length()

    # equal to
    def __eq__(self, p):
        # we change it here to prevent decimals messing up and effecting it
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


p1 = Point(3, 4)
p2 = Point(3, 2)
p3 = Point(1, 3)
p4 = Point(0, 1)
# we have now added in the functionality for +, - and *. Using + when you have a function of __add__ will call
# that function to deal with the problem
p5 = p1 + p2
p6 = p4 - p1
p7 = p2 * p3
# printing this without the str function will just return what the point's address and memory is
print(p5, p6, p7)

print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)

# there are many more overloading methods that can been seen in python documentation
