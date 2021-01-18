# Generator expressions aren't actually comprehensions but they are very similar to list comprehensions


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# non expression
def gen_func(nums):
    for n in nums:
        yield n ** 2


my_gen = gen_func(nums)
for i in my_gen:
    print(i)
print('----------')

# expression
my_gen = (n**2 for n in nums)

for i in my_gen:
    print(i)
