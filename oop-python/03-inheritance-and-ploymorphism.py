# parent class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # create parent class method
    def work(self):
        print(f'{self.name} is working...')

# child class
class SoftwareEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    # create child class method
    def debug(self):
        print(f'{self.name} is debugging...')

# child class
# note: we don't necessary define the __init__ function to access attributes
class Designer(Employee):

    # create child class method
    def draw(self):
        print(f'{self.name} is drawing...')

    # create same function as parent class but
    # change the print statement to override it
    def work(self):
        print(f'{self.name} is designing...')

# create instance for software engineers
se1 = SoftwareEngineer('John', 25, 7000, 'Junior')

# create instance for designers
de1 = Designer('Lisa', 28, 5000)

## attributes inherited from parent class plus extented attribute (i.e. level)
# print(se1.name, se1.age, se1.salary, se1.level)

## attributes inherited from the parent class 
# print(de1.name, de1.age)

## call child class methods 
# se1.debug()
# de1.draw()

## call the method inherited from parent class
# se1.work()

## call the method inherited from parent class but overridden
# de1.work()

# PLOYMORPHISM
# create a list of employees for each child class
employees = [SoftwareEngineer('Max', 29, 9000, 'Senior'),
             SoftwareEngineer('Henry', 32, 11000, 'Lead'),
             Designer('David', 28, 5000)]

def motivate_employees(employees):
    for employee in employees:
        employee.work() # SoftwareEngineer will always inherit the 'work' method from parent class because it doesn't exit in the child class itself

# call the function
motivate_employees(employees)

# Recap:
# inheritance: ChildCLass(ParentClass)
# inherit, extend, override concept
# super.()__init__(ParentClass attributes) to inherit into ChildClass
# ploymorphism