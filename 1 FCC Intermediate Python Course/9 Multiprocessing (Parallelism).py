from multiprocessing import Process, Value, Lock
import os
import time

# because they don't have access to the same memory data we have to use special shared memory objects
# to them have shared memory. We can either use value for a single value or an array

# sharing with a single value
'''def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


if __name__ == '__main__':
    lock = Lock()
    # Value('datatype (i=integer)', starting value)
    shared_number = Value('i', 0)
    print('Number at the start is ', shared_number.value)

    # this will cause a race condition if there is no lock
    p1 = Process(target=add_100, args=(shared_number, lock,))
    p2 = Process(target=add_100, args=(shared_number, lock,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('NUmber at the end is', shared_number.value)'''

# sharing with an array
from multiprocessing import Array

''''def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1


if __name__ == __main__':
    lock = Lock()
    # Array('datatype',initial list)
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print('Array at the start is ', shared_array[:])

    # this will cause a race condition if there is no lock
    p1 = Process(target=add_100, args=(shared_array, lock))
    p2 = Process(target=add_100, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Array at the end is', shared_array[:])'''

# using queues with multiprocessing
# the queue here is from the multiprocessing, the difference is that it doesn't have the
# task_done and join method because they will mess up multiprocessing
# instead you have to stop the queue a different way
from multiprocessing import Queue

'''def square(numbers, q):
    for i in numbers:
        q.put(i * i)


def negative(numbers, q):
    for i in numbers:
        q.put(i * -1)


if __name__ == '__main__':

    numbers = range(1, 6)
    q = Queue()
    p1 = Process(target=square, args=(numbers, q))
    p2 = Process(target=negative, args=(numbers, q))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    # stopping the queue by removing all elements when the processes
    # have stopped and also prints all of the elements the processes
    # have altered

    while not q.empty():
        print(q.get())'''

# pool takes care of a lot of things so you don't have to work with them as much

from multiprocessing import Pool


def cube(number):
    return number ** 3


if __name__ == '__main__':
    numbers = range(1, 10)
    pool = Pool()

    # there are four methods. Two are used here and the other tow can be accessed in the documentation
    # map, apply, join, close

    # this will create as many processes as you have cores and then run the method in parallel, returning
    # the result when it is finished
    result = pool.map(cube, numbers)

    # you can print one of the results using apply
    # result = pool.apply(cube, (numbers[1],))

    # wait for the pool to finish all of the calculations
    pool.close()
    pool.join()

    print(result)

# you can also have asynchronous calls to map and apply but they are not covered here but
# can be viewed in the documentation
