# Using threading and multiprocessing you can run code in parallel to speed up your code
# threads are limited by the gil

# a process is an instance of a program (e.g. a python interpreter or chrome browser)

# advantages:
# processed use multiple threads and cores in parallel
# they have a separate memory space (it is not shared between processes)
# great for cpu bound processing (large amounts of data can be process on different cpus to speed it up
# a new process is started independently from others
# they are iterruptable
# there is one GIL (global interpreter lock) for each process so it avoids GIL limitation by not using too many

# disadvantages
# they take up a lot of RAM
# it is slower to start up than a thread
# since their memory is separate it is more difficult to share it
# IPC (inter-process communication) is more difficult because on separate memory


# a thread is an entity inside a process that can be scheduled. A process can have multiple threads inside
# also known as a lightweight process

# advantages:
# All threads share the same memory
# easy to run and start
# good for I/O tasks (if the program has to talk to slow such as a hard drive or wifi then it can
# designate some threads to wait on the communication and others to do the processing in the meantime

# disadvantages
# the GIL only allows one thread at a time so there can be no proper multithreading without getting around this
# no effect for cpu bound tasks
# not interruptable so be careful with memory leaks
# share the same memory so you need ot be careful if multiple threads are trying to modify (race conditions)
# the same thing at the same time and this can cause bugs and crashes


# the GIL (global interpreter lock) is a lock that prevents more than one thread at a time from
# executing

# it is needed because in Cpython there is a memory management that is not thread-safe
# the gil is needed because is cpython there is am memory management tht is not thread-safe
# the cpython there is a technique called reference counting that is used for memory management
# this means that objects created in python have a reference count value to see how
# many times it is being referenced. If it is 0 then the memory occupied by the object is released
# the problem is that this reference count variable needs protection from race conditions
# because if two threads are trying to modify the same object and the same time then it will
# either cause leaked memory that is never released or it can incorrectly release the memory
# whilst references to the object still exist

# You can avoid it by using
# a different free-threaded python implementation (Jython or IronPython)
# python as a wrapper for third-party libraries such as numpy which executes its code in C

# multiprocessing
# in task manager you will see all the different processes running this corresponding to each core
# rather than the default two processes
from multiprocessing import Process
import os
import time


def square_numbers():
    for i in range(100):
        i * i
        time.sleep(0.1)


if __name__ == '__main__':
    processes = []
    # you should use the amount of cpus on your machine
    num_processes = os.cpu_count()

    # create processes
    # if your function had an argument then you would have to write the function name, args=
    for i in range(num_processes):
        p = Process(target=square_numbers)
        processes.append(p)

    # start processes
    for p in processes:
        p.start()

    # join processes
    # this means I want to wait for all processes to finish and I am blocking the main thread
    # until they are finished
    for p in processes:
        p.join()
    print('multiprocessing finished')

# multithreading
# if you checked the main process then you would see that it would contain 10 threads but I can't figure out
# how to check the threads in windows 10
from threading import Thread

if __name__ == '__main__':
    def square_numbers():
        for i in range(100):
            i * i
            time.sleep(0.1)


    threads = []
    # you should use the amount of cpus on your machine
    num_threads = 10

    # create processes
    # if your function had an argument then you would have to write the function name, args=
    for i in range(num_threads):
        t = Thread(target=square_numbers)
        threads.append(t)

    # start processes
    for t in threads:
        t.start()

    # join processes
    # this means I want to wait for all processes to finish and I am blocking the main thread
    # until they are finished
    for t in threads:
        t.join()
    print('multithreading finished')
