# First-class and closures before into decorators concepts

# # first example (takes no argument)
# # create outer function
# def outer_function():
#     # create inner function
#     def inner_function():
#         print('Hello world!')

#     # return inner function (note: without () means we're just returning the function, not calling it)
#     return inner_function

# # assign the outer function to the variable
# myfunc = outer_function()
# # call the outer function stored through the variable myfunc
# myfunc()


# second example (takes argument)
def outer_function(msg):
    def inner_function():
        print(msg)

    return inner_function

hifunc = outer_function('Hi')
byefunc = outer_function('Bye')

hifunc()
byefunc()

# Recap:
# first-class functions are objects like everything else in Python:
# 1. can be used as parameters
# 2. can be used as a return value
# 3. can be assigned to variables
# 4. can be stored in data structures such as hash tables, lists etc
# Closures are the inner functions that are enclosed within the outer function
# closures can access variables present in the outer function scope