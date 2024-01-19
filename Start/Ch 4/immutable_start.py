# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen = True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def someFunc(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

#after instance initiated, data can't be changed (login, e-mail, password)
obj2 = ImmutableClass("Another string", 20)
print(obj2.value1, obj2.value2)
# TODO: attempting to change the value of an immutable class throws an exception
obj.value1 = "Another string"
print(obj.value1)
# TODO: even functions within the class can't change anything
print(obj.someFunc(10))
