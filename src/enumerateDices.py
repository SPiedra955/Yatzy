from enum import Enum,unique

@unique
class Pips(Enum):

    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6

#__call__(cls, value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)
#This method is called in two different ways:
#to look up an existing member:(cls) The enum class being called.
#value,the value to lookup.to use the cls enum to create a new enum:
# we use (cls) inside a method to call enum values or name.

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())
    
    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - { pip.value }

