from collections import deque

# deque is pronounced dek

# deque is faster at adding elements to the start and end of a list
# it can take any string or container and will split up every character in a string
d = deque('hello')
print(d)

# you can append or remove to a deque and you can append or remove from the start
# it will append something as one element
d.append('4')
d.appendleft('hi')
print(d)

d.pop()
d.popleft()
print(d)

# removes all elements from the deque
d.clear()
print(d)

# puts something at the end or beginning of the deque
# extending will append each character at a time
d.extend('123')
d.extend('hello')
print(d)
# if you add to the front then it will add in reverse order
d.extendleft('hey')
print(d)

# moves all elements one to the left, a positive number will rotate to the right
d.rotate(-1)
print(d)
d.rotate(2)
print(d)
print('-----------')
# this deque has a maximum length of five and if it goes over five then it will remove elements from the deque
# starting at the start
# you cannot change the maxlen after it is initialised
d = deque('hello', maxlen=5)
print(d.maxlen)
print(d)
d.append(1)
print(d)

# there are more attributes on deque that can be found in the documentation
