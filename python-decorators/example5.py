# First practical implementation of the decorators

# create decorator function to save logs
def logs(original_func):
    def wrapper(*args, **kwargs):
        func_name = original_func.__name__
        value = original_func(*args, **kwargs)
        with open('mylogs.txt', 'a') as f:
            print(f'{func_name} function returned the value {value}')
            f.write(f'{func_name} function returned the value {value}\n')
    return wrapper

# apply decorator on add function
@logs
def add(a, b):
    return a + b

# call the add function
add(9000, 10)

# Recap:
# decorators are handy when we want to write logs
# for our functions