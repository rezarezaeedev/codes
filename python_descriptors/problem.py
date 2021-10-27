'''
    property(getter), setter and deleter help us for managing better on class attribiutes, such as validations,
    but if we have more of two fields ,this way has been very hard and long codes,
    python descriptors solved this problems.
    see desc.py file.
'''

class Human:
    def __init__(self, name, age):
        self._name = name
        self._age=age
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value,str):
            raise ValueError("Value must be string")
        self._name=value

    @name.deleter
    def name(self):
        self._name=None

    
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value,int):
            raise ValueError("Value must be integer")
        self._age=value

    @age.deleter
    def age(self):
        raise ValueError('age field cant delete')

first_human = Human('reza', 22)
print(first_human.name, first_human.age)

first_human.name='reza'
first_human.age=44
print(first_human.name, first_human.age)

del first_human.name
print(first_human.name, first_human.age)


'''error prints ,please uncommend only one line'''
# set not str for name error
first_human.name=46456456
#

# set not int for age error
first_human.age='fsdfsdf'
#

# delete error
del first_human.age
#


