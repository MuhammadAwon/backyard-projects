# decorator example 3

def decorator_func(original_func):
    # wrapper_func to accept arguments
    def wrapper_func(*args, **kwargs):
        print(f'wrapper function executed the {original_func.__name__} function.')
        # print display function output within wrapper function
        print(original_func(*args, **kwargs))
        # print some more information after original function executed
        print('function executed fine')

    return wrapper_func

@decorator_func
# create function with parameters
def display(name, age):
    # return output to print the result in the wrapper function
    return f'The person name is {name} and {name} is {age} years old.'

# call display function
display('awon', 36)

# Recap:
# setting *args and **kwargs allow us to using arbitrary number
# of arguments from the original function