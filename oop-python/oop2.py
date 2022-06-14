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


# create instances
se1 = SoftwareEngineer('Max', 20, 'Junior', 5000)
se2 = SoftwareEngineer('Lisa', 25, 'Senior', 7000)