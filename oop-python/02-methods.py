# position, name, age, level, salary (a list of people job description)
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

    # instance method
    def se_work(self):
        print(f'{self.name} makes mobile apps at work')

    # instance method with parameter
    def fav_lang(self, lang):
        print(f'{self.name} favorite programming language is {lang}')

    # dunder methods
    def __str__(self):
        engineer_info = f'name={self.name}, age={self.age}, level={self.level}'
        print(engineer_info)

    def __eq__(self, other):
        return self.age == other.age and self.salary == other.salary

    # methods with decorators, note: we can't access
    # the instance attributes with these methods
    @staticmethod
    def entry_salary(age):
        if age < 25:
            return 5000
        elif age < 30:
            return 7000
        return 10000

# create instances
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)
se3 = SoftwareEngineer('David', 25, 'Lead', 7000)

# call instance methods
se1.se_work()
se2.fav_lang('Python')

# call dunder methods
se1.__str__()
print(se2 == se3) # output True
print(se1 == se3) # output False

# call method with decorators
print(se1.entry_salary(25))
print(se3.entry_salary(30))

# Recap:
# instance method (self)
# methods can take arguments and can return values
# special "dunder methods" (__str__ and __eq__)
# method with decorator
# decorator method can not access the instance attritutes (i.e. self)