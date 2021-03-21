class Person():
    def __init__(self):
        self.fname = "Alican"
        self.lname = "Demirtas"
        self.age = 22

    # use __repr__ to create a string useful for debugging
    def __repr__(self):
        return f"<Person Class - fname: {self.fname}, lname: {self.lname}," \
               f" age: {self.age}"

    # use __str__ for a more human-readable string
    def __str__(self):
        return f"Person {self.fname} {self.lname} is {self.age}"

    # use __bytes__ to control how an instance should be converted to bytes
    def __bytes__(self):
        val = f"Person:{self.fname}:{self.lname}:{self.age}"
        return bytes(val.encode("utf-8"))


def main():
    # create a new Person object
    my_person = Person()

    # use different python functions to convert it to string
    print("repr: " + repr(my_person))
    print("str: " + str(my_person))
    print("formatted: {0}".format(my_person))
    print(f"printf: {my_person}")
    print(f"bytes: {bytes(my_person)}")


if __name__ == "__main__":
    main()
