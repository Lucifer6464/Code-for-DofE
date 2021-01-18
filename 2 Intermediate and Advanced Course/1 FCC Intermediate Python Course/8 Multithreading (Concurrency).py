from threading import Thread, Lock
import time

database_value = 0


# since threads share the same memory space, they have access to the same data, this makes sharing data very easy

def increase(lock):
    global database_value
    # lock by using it as a context manager
    with lock:
        local_copy = database_value

        # processing
        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy

    # lock by calling its methods
    # lock.acquire()
    # local_copy = database_value
    #
    # # processing
    # local_copy += 1
    # time.sleep(0.1)
    #
    # database_value = local_copy
    # lock.release()


if __name__ == '__main__':
    lock = Lock()
    print('start value: ', database_value)
    # this will cause a race condition because they are both trying to access the same variable and it should
    # theoretically be 2 but when we time.sleep(0.1), thread 2 will start to run the increase() and because thread 1
    # has not put the database_value to the local_copy, the database_value has not been incremented so when thread 2
    # copies the database_value, it just copies the value of 1 because thread 1 has not changed it yet when thread 2
    # start running
    # to fix this we put a lock on it so that thread 2 cannot access database_value until thread 1 has finished with it
    # we say lock.acquire() at the start and then lock.release() at the end. These are the only attributes of lock
    # or you could use lock as a context manager and this is generally a better way to do it for how it looks
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print('end value: ', database_value)
    print('end of main about multithreading with locks')
    print('----------')

# queues are good for thread, process safe data exchange and data processing in multithreading or
# multiprocessing environments

# queue is a linear data structure that follows FIFO (first in, first out)
# a good example of a queue is a queue of customers waiting in line with the customer there first
# gets served first

from queue import Queue

database_value = 0


def increase(lock):
    global database_value

    with lock:
        local_copy = database_value

        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy


if __name__ == '__main__':
    q = Queue()

    q.put(1)
    q.put(2)
    q.put(3)

    # .get() will store the first value and remove it
    print(q.get())
    # if you do q.get() again, it will get and remove the next value
    print(q.get())

    # check if it is empty (True of False)
    print(q.empty())

    # when you are finished you always call q.task_done() to let the computer know it can continue
    # with anything next
    q.task_done()

    # this blocks the main thread and waits until all of the elements in are queue have been processed
    # it is similar to joining threads or processes
    # q.join()

    print('end of main about queues')
    print('----------')

from threading import current_thread


# the printed sentence may not be in chronological order or several
# threads and what they got might be on the same line because
# they tried to run the loop at the same time
# to fix this we can just use a lock
def worker(q, lock):
    while True:
        value = q.get()
        with lock:
            print(f'in {current_thread().name} got {value}')
            q.task_done()


if __name__ == '__main__':
    q = Queue()
    lock = Lock()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(q, lock))
        # daemon threads are a background threads that die when the main thread dies
        # this essentially causes the thread to exit the while true loop when it is finished processing
        thread.daemon = True
        thread.start()

    # this will loop from 1 to 20
    for i in range(1, 21):
        q.put(i)
    q.join()

    print('end of main about multithreading with queues')
    print('----------')
