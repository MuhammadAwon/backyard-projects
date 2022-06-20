# ENCAPSULATION and ABSTRACTION

class SoftwareEngineer:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        # create private attributes
        self._salary = None
        self._num_bugs_solved = 0

    # create method to check protected attribute '_num_bugs_solved'
    def bugs_fixed(self):
        self._num_bugs_solved += 1       

    # create public getter method to access '_salary' attribute
    def get_salary(self):
        return self._salary

    # create public setter method to set value for '_salary' attribute
    def set_salary(self, base_salary):
        # check value, enforce constraints
        self._salary = self._calculate_salary(base_salary)

    # create protected method to calculate employee's salary
    def _calculate_salary(self, base_salary):
        if self._num_bugs_solved <= 10:
            return base_salary
        elif self._num_bugs_solved <= 100:
            return base_salary * 2
        else:
            return base_salary * 4


# create instance with public attributes
se1 = SoftwareEngineer('John', 25)
print(se1.name, se1.age)

# set num of bugs fixed by the employer (protected attribute)
for i in range(100):
    se1.bugs_fixed()

# set salary (protected attribute)
se1.set_salary(2000)
# display result of protected attribute
print(se1.get_salary())

# Recap:
# the concept of public, protected (_), and private (__)
# attributes and methods
# encapsulation is hiding data implementation and
# restricting the access
# getter and setter methods to access protected attributes
# protected method (_calculate_salary())
# Abstraction: it is the natural extension of encapsulation
# it's a process of handling complexity by hiding unnecessary
# information. e.g. the 'set_salary()' method is applying abraction
# by hiding other functionality being applied on salary
