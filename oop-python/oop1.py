# it will be cumbersome if we want to create more of the following objects
# also it'll be more error-prone
# position, name, age, level, salary (a list a list of people job description)
se1 = ['Software Engineer', 'Max', 20, 'Junior', 5000]
se2 = ['Software Engineer', 'Lisa', 25, 'Senior', 7000]

# create class
class SoftwareEngineer:
    # class attribute
    nickName = 'Keyboard Warrior'

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary


# create instances
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)

# retrieve instance attributes
print(se1.name, se1.level)
print(se2.name, se2.level)

# retrieve class attribute
print(se2.name, se2.nickName)
print(SoftwareEngineer.nickName)

# recap
# create a class (blueprint)
# create a instance (object)
# difference between class vs instances
# instances attributes: defined in __init__(self)
# class attribute (can be accessed by an instance or a class itself)