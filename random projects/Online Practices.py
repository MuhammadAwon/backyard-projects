# def sum(n1,n2):
#     return n1 + n2

# total = sum(10, 20)
# print(total)
# print(sum(5, total))


# def checkDriverAge(age):
#     if int(age) < 18:
#         return "Sorry, you are too young to drive this car. Powering off"
#     elif int(age) > 18:
# 	    return "Powering On. Enjoy the ride!"
#     else:
# 	    return "Congratulations on your first year of driving. Enjoy the ride!"


# print(checkDriverAge(age = input("What is your age?: ")))

# def test(a):
#     '''
#     info: this is a function
#     '''
#     print(a)

# test('ok')
# help(test)
# print(test.__doc__)


# def test(name, *args, age=34, **kwargs):
#     print(name)
#     for item in args:
#         print(item)
#     print(age)
#     for key, value in kwargs.items():
#         print(key, value)

# test('awon', 8, 24, team='manutd', stadium='old trafford')


'''create a function 'highest_even' that takes a list and displays
the highest even number of the list'''

# def highest_even(alist):
#     evens = []
#     for ele in alist:
#         if ele % 2 == 0:
#             evens.append(ele)
#     return max(evens)

# print(highest_even([2,3,4,8,10,11]))


# class Player:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def run(self):
#         return (f'{self.name} running is a good habit')

# plyr1 = Player('Awon', 34)
# plyr2 = Player('Ahmed', 28)

# print(plyr1.run())
# print(plyr2.age)



'''
Create a class "Cat" that has three cats object, then create a function to find the oldest cat,
print out "The oldest cat is x years old".
'''
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# cat1 = Cat('emmi', 1)
# cat2 = Cat('timmi', 3)
# cat3 = Cat('jimmi', 5)


# def oldest(*args):
#   return max(args)


# print(f'The oldest cat is {oldest(cat1.age, cat2.age, cat3.age)} years old')


# class Person:
#     totalObjects=0
#     def __init__(self):
#         Person.totalObjects=Person.totalObjects+1

#     @classmethod
#     def showcount(cls):
#         print("Total objects: ",cls.totalObjects)


#     @staticmethod
#     def greet():
#         print("Hello!")


# p1=Person()
# p2=Person()
# Person.showcount()
# p2.showcount()
# Person.greet()
# p1.greet()


# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f'{self.name} is just walking around'

# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #1 Add another Cat
# class Kitty(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# #2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Cat('Simon', 3), Cat('Sally', 8), Cat('Kitty', 5)]

# #3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)

# #4 Output all of the cats walking using the my_pets instance
# my_pets.walk()

# class Toy():
#     def __init__(self, color, age):
#         self.color = color
#         self.age = age
#         self.my_dict = {
#             'name': 'Awon',
#             'has_pets': False
#         }

#     def __str__(self):
#         return f'{self.color}'

#     def __len__(self):
#         return 5

#     def __call__(self):
#         return ('say whatt??')

#     def __getitem__(self, index):
#         return self.my_dict[index]

# wolverine = Toy('black', 2)
# print(str(wolverine))
# print(len(wolverine))
# print(wolverine())
# print(wolverine['name'])

'''Create a class 'SuperList' and this SuperList is going to have some special dender method like
'len' which always return 1000 no matter what.
We can then instantiate the list like 'super_list1' and it is going to allow us to perform len,
append and access the list by index'''

# class SuperList(list):
#     def __len__(self):
#         return 1000

# super_list1 = SuperList()
# print(len(super_list1))
# super_list1.append(8)
# super_list1.append(24)
# print(super_list1[1])
# # to double check we can use built-in function issubclass()
# print(issubclass(SuperList, list))


# class User():
#     def sign_in(self):
#         return 'User is logged in'

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power

#     def attack(self):
#         return f'{self.name} is attacking with the power of {self.power}'

# class Archer(User):
#     def __init__(self, name, arrows):
#         self.name = name
#         self.arrows = arrows

#     def check_arrows(self):
#         return f'{self.arrows} remaining'

#     def run(self):
#         return f'{self.name} ran so fast'

# class Ogre(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Wizard.__init__(self, name, power)
#         Archer.__init__(self, name, arrows)

# ogre1 = Ogre('Simon', 80, 25)
# print(ogre1.sign_in())
# print(ogre1.attack())
# print(ogre1.check_arrows())
# print(ogre1.run())

# inp = int(input('num: ?'))
# for i in range(inp):
#     n = int(input('n: ?'))
#     result = n**2 % 10
#     print(result)



# function to multiply by 2
# def multiply_by2(item):
#     return item * 2

# print(list(map(multiply_by2, [1,2,3])))


# make a list of user names and turn all names into upper case
# def block_letter(name):
#     return name.upper()

# print(list(map(block_letter, ['awon', 'ahmed', 'zain', 'umair'])))


# make a list of users whose name doesnt start with the letter A.

# users = ['awon', 'ahmed', 'zain', 'umair']
# def without_A(item):
#     return item[0] != 'a'

# print(list(filter(without_A, users)))


# make a list of odd numbers only
# li = [1,2,3]
# def only_odd(item):
#     return item % 2 != 0

# print(list(map(only_odd, li)))
# print(list(filter(only_odd, li)))
# print(li)


# make a function to paired to lists using zip() and return tuple
# users = ['awon', 'ahmed', 'zain', 'umair']
# phones = [22782, 11458, 36974, 54869, 78787]

# print(list(zip(users, phones)))


# my_list = [1,2,3]

# from functools import reduce
# def mult(x,y):
#     print(x,y)
#     return x*y

# fact= reduce(mult, my_list)
# print (fact)


# from functools import reduce

#1 Write all of the pet names in upper case and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']

# def cap_names(item):
#     return item.upper()

# print(list(map(cap_names, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
# my_strings = ['a', 'b', 'c', 'd', 'e']
# my_numbers = [5,4,3,2,1]

# new_nums = sorted(my_numbers)

# print(list(zip(my_strings, new_nums)))


#3 Filter the scores that pass over 50%
# scores = [73, 20, 65, 19, 76, 100, 88]

# def passing_scores(item):
#     return item > 50

# print(list(filter(passing_scores, scores)))


'''4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores).
 What is the total?'''
# my_numbers = [5,4,3,2,1]
# scores = [73, 20, 65, 19, 76, 100, 88]

# total = my_numbers + scores

# def combo(acc, item):
#     return acc + item

# print(reduce(combo, total))

# from functools import reduce
# my_list = [1,2,3]

# print('multiply by 2:', list(map(lambda item: item*2, my_list)))
# print('only odd:', list(filter(lambda item: item%2 != 0, my_list)))
# print('accumulate:', reduce(lambda acc, item: acc + item, my_list))


# Using lambda create square of each item in the list:
# my_list = [5,4,3]

# new_list = list(map(lambda num: num**2, my_list))
# print(new_list)


# Using lambda sort out the list of tuples based on the second value of each tuple:
# a = [(0,2), (4,3), (9,9), (10,-1)]

# print(sorted(a, key=lambda item: item[1]))

# li = [num for num in range(0,20) if num%2 == 0]
# print(li)

# my_set = {char for char in 'hello'}
# print(my_set)

# my_set2 = {num*2 for num in range(0,11)}
# print(my_set2)

# my_set3 = {num for num in range(0,11) if num%2 == 0}
# print(my_set3)

# simple = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }

# my_dict = {key:value*2 for key,value in simple.items()}
# print(my_dict)

# my_dict = {num:num*2 for num in [1,2,3]}
# print(my_dict)

# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicate = list(set([x for x in some_list if some_list.count(x)>1]))
# print(duplicate)

# def my_decorator(func):
#     def wrap_func():
#         print('*******')
#         func()
#         print('*******')
#     return wrap_func

# @my_decorator
# def hello():
#     print('Hello')

# @my_decorator
# def bye():
#     print('See ya later')

# hello()
# bye()
# my_decorator(hello)()
# my_decorator(bye)()
# a = my_decorator(hello)
# b = my_decorator(bye)
# a()
# b()


# def my_decorator(func):
#     def wrap_func(x):
#         print('*******')
#         func(x)
#         print('*******')
#     return wrap_func

# @my_decorator
# def hello(greeting):
#     print(greeting)

# hello('morning')


# from time import time
# def performance(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         t2 =time()
#         print(f'it took {t2-t1} s')
#         return result
#     return wrapper




# @performance
# def test():
#     for i in range(100000000):
#         i*5

# test()


# Create an @authenticated decorator that only allows the function to run
# if user1 has 'valid' set to True:
# user1 = {
#     'name': 'Sorna',
#     'valid': True #changing this will either run or not run the message_friends function.
# }

# user2 = {
#     'name': 'Mojo',
#     'valid': False
# }

# def authenticated(fn):
#     def wrapper(*args, **kwargs):
#         if args[0]['valid']:
#             fn(*args, **kwargs)
#         else:
#             print('invalid user')
#     return wrapper

# @authenticated
# def message_friends(user):
#     print('message has been sent')

# message_friends(user1)
# message_friends(user2)


# while True:
#     try:
#         age = int(input('what is your age?'))
#         10/age
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter number higher than zero')
#     else:
#         print('thank you')
#         break


# def add(n1,n2):
#     try:
#         return n1/n2
#     except (TypeError, ZeroDivisionError) as err:
#         return err

# print(add(1,"1"))



# while True:
#     try:
#         age = int(input('whats your name?'))
#         10/age
#     except ValueError:
#         print('please enter a number')
#     except ZeroDivisionError:
#         print('please enter number higher than zero')
#     else:
#         print('thankyou!')
#         break
#     finally:
#         print('ok, I am done')


# while True:
#     try:
#         age = int(input('whats your name?'))
#         10/age
#         raise ValueError('cut it out')
#     except ZeroDivisionError:
#         print('please enter number higher than zero')
#     else:
#         print('thankyou!')
#         break
#     finally:
#         print('ok, I am done')

# sample_data = [
#     {"userId": 1,  "name": "awon", "completed": False}, 
#     {"userId": 2, "name": "ahmed", "completed": False}, 
#     {"userId": 3,  "name": "hassan", "completed": False}, 
# ] 
  
# print("With Python 3.8 Walrus Operator:")  
# for entry in sample_data:  
#     if name := entry.get("name"): 
#         print(f'the name is: "{name}"')



# # a = [1,2,3,4]
# if (n := len(a)) > 3:
#     print(f'the list has {n}')


# def gen_func(num):
#     for item in range(num):
#         yield item*2

# g = gen_func(10)
# next(g)
# next(g)
# print(next(g))

# from time import time
# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper

# @performance
# def long_time():
#     print('1')
#     for i in range(10000000):
#         i*5
# @performance
# def long_time2():
#     print('2')
#     for i in list(range(10000000)):
#         i*5


# long_time()
# long_time2()


# for loop underneath the hood
# def special_for(iterable):
#   iterator = iter(iterable)
#   while True:
#     try:
#       print(iterator)
#       print(next(iterator)*2)
#     except StopIteration:
#       break

# special_for([1,2,3,4,5,6,7,8,9,10])




# range() underneath the hood
# class MyGen():
#     current = 1
#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         MyGen.current = self.first
    
#     def __iter__(self):
#         return self

#     def __next__(self):
#         if MyGen.current <= self.last:
#             num = MyGen.current
#             MyGen.current += 1
#             return num
#         raise StopIteration

# gen = MyGen(1, 100)
# for item in gen:
#     print(item)



''' Using generator make a sequence of first 21 fibonacci numbers and also make it using list as well.'''
# def fib(num):
#     a = 0
#     b = 1
#     for item in range(num):
#         yield a
#         item = a
#         a = b
#         b = item + b

# for x in fib(21):
#     print(x)

# def fib2(num):
#     a = 0
#     b = 1
#     result = []
#     for item in range(num):
#         result.append(a)
#         item = a
#         a = b
#         b = item + b
#     return result

# print(fib2(21))

# from collections import Counter, defaultdict, OrderedDict

# li = [1,2,3,4,4,5,6]

# print(Counter(li))

# dict = defaultdict(lambda: 5, {'a': 1, 'b': 2})

# print(dict['c'])


# import datetime
# from array import array

# print(datetime.date.today())

# arr = array("i", [1,2,3])
# print(arr[0:2])


'''
Create an email and password checker and user password has to have few requirments:
# At least 8 characters long
# Contains any sort of letters, numbers and only symbols like $%#@
# Has to end with a number
'''
# import re

# email_pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# pass_pattern = re.compile(r"^[a-zA-Z0-9$%#@]{7,}\d$")


# while True:
#     Email = input('Please enter your email: ')
#     email_checker = email_pattern.search(Email)
    
#     while email_checker:
#         Password = input('Please enter your password: ')
#         pass_checker = pass_pattern.search(Password)

#         if pass_checker:
#            print('Thanks for signing up')
#            break
#         else:
#             print("Invalid password")
            
#     if email_checker:
#         break
#     else:
#         print('Invalid email entered')


