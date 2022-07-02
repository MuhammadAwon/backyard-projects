# decorators example 1

# create decorator function and pass the original function
def my_decorator(original_func):
    def wrapper():
        return original_func()

    return wrapper


# create simple function (without parameter)
def intro():
    print('Good to see you!!')

# pass intro function to the decorator function and assign 
# result to the variable
dec_intro = my_decorator(intro)

# call the function
dec_intro()


# Recap:
# a decorator function allows to add new functionality to
# an existing function without modifying its code base