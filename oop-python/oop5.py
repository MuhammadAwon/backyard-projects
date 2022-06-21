# property (getter), setter, and deleter decorators

class SoftwareEngineer:
    def __init__(self):
        # access and work with protected attributes pythonic way
        self._salary = None

    # create getter method to access salary
    @property
    def salary(self):
        return self._salary

    # create setter method to set salary
    @salary.setter
    def salary(self, value):
        self._salary = value

    # create deleter method to delete salary
    @salary.deleter
    def salary(self):
        del self._salary

# create instance
se1 = SoftwareEngineer()

# set salary
se1.salary = 5500

# # delete salary
# del se1.salary

# access salary (will throw error if the salary is deleted)
print(se1.salary)

# Recap:
# getter -> @property
# setter -> @x.setter
