# decorators example 2

# create decorator function and pass the original function
def my_decorator(original_func):
    def wrapper():
        return original_func()

    return wrapper

# apply decorator function
@my_decorator
# create simple function (without parameter)
def intro():
    print('Good to see you in a better way!!')

# call the function
intro()


# Recap:
# using @my_decorator is same as myfunc = my_decorator(intro)