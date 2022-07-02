# Second practical implementation of decorators

import time

# create decorator function to calcuate the execution time
# of a function
def timer(original_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        original_func(*args, **kwargs)
        end = time.time()-start
        func_name = original_func.__name__
        print(f'{func_name} function took {end} seconds to execute!')

    return wrapper

# apply decorator
@timer
def multiply(num):
    result = 1
    for i in range(1, num):
        result *= i
    return result

# call the multiply function
multiply(100000)