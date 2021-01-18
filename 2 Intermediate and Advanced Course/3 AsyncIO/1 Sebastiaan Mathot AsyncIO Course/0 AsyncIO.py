import time
import asyncio


def is_prime(x):
    return not any(x // i == x / i for i in range(x - 1, 1, -1))


async def highest_prime_below(x):
    print('Highest prime below', x)
    for y in range(x - 1, 0, -1):
        if is_prime(y):
            print('Highest prime below %s is %s' % (x, y))
            return y
        # this causes the code to do other things when it has finished, it will go for the
        # quickest code first. It will also make finishing far faster by 50ms in this program
        # the 10ms sleeping is used to perform other functions instead of doing nothing
        await asyncio.sleep(0.01)
        # time.sleep(0.01)
    return None


# to make a function asynchronous you have to put async before its name and then
# either call it using await or passed to a async event loop
async def main():
    start = time.time()
    # asynchronous wait introduces randomness, it doesn't care which function executes first
    await asyncio.wait([
        highest_prime_below(100000),
        highest_prime_below(10000),
        highest_prime_below(1000)
    ])
    end = time.time()
    print(f'this took {(1000*(end-start))} ms')


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
