import random
import timeit

MAX_NUMBER = 1000000
quantity = 40000
loops = 10000

numbers = random.sample(range(MAX_NUMBER), quantity)

time = timeit.timeit(stmt="random.randrange(MAX_NUMBER) in numbers", number=loops, globals=globals())
print(f"It took {time}s to search {loops} times through a list of {quantity} items!")
