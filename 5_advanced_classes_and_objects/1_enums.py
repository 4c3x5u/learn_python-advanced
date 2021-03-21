# define enumerations using the Enum base class
from enum import Enum, unique, auto


# enums have duplicate values but cannot have duplicate names
# the `unique` decorator prevents even the duplicate values
@unique
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    # use auto() to automatically assign a value to a name
    PEAR = auto()


def main():
    # enums have human-readable types and values
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have `name` and `value` properties
    print(f"name: {Fruit.APPLE.name}, value: {Fruit.APPLE.value}")

    # print an auto-assigned value
    print(Fruit.PEAR.value)

    # enums are hashable – can be used as keys
    my_fruits = {Fruit.BANANA: "Come Mr. Tally-man"}
    print(my_fruits[Fruit.BANANA])


if __name__ == "__main__":
    main()
