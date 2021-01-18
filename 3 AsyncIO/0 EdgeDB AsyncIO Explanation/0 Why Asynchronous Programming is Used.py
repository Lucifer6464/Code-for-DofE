# Asynchronous programming is very effective because it allows you to render the most important
# information on the screen at the start and things that take longer can be allowed to take longer
# so that a user can see content before all of it is loaded so that it is quicker to respond
# and interact with a user rather than wait a long time for everything to load before it lets
# you use it. The technical term that people use is called lag.

# Synchronous programming is the term used for if you let the entire page load when a user
# clicks on it

# Synchronous is like if you have a fifty year old car in front of a lamborghini
# the lamborghini can only go as fast as the car in front
# Asynchronous programming allows the lamborghini to overtake those in front of it

# They best way to unblock multiple cars behind each other is to add more lanes (threads)
# You can fix race conditions using locks but locks make other threads wait a long time
# the GIL is a global lock that prevents two threads from accessing the same object at the same time
# the GIL is very controversial because it means you can't have multiple threads interacting
# with the same thing at the same time in python without using third-party libraries or a
# free-threaded python implementation. However, the GIL does actually make python faster
# a experiment made found that removing the GIL made python slower and this speed
# could not be compensated without rewriting a lot of python's structure

# the goal of async is to maximize the usage of a single thread by:
# handling I/O asynchronously
# enabling multithreading using coroutines

# it essentially makes a thread do other tasks while it is waiting for the lock of a
# object or database to be released

