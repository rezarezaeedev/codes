class desc:
    def __set_name__(self, name ,owner):
        self.name = name

    def __init__(self,  typefield):
        self.typefield=typefield

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.typefield):
            raise ValueError(f'value must be {self.typefield}')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        instance.__dict__[self.name] = None
    
class Human:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    name = desc(str)
    age = desc(int)

first_human = Human('reza',33)

print('1:',first_human.name, first_human.age)

first_human.name='alireza'
first_human.age=44
print('2:',first_human.name, first_human.age)

del first_human.name
del first_human.age
print('del:',first_human.name, first_human.age)

# errors ,please uncomment one line
first_human.name=546
# first_human.age='44'




