class Employee:
    def __init__(self, fname, lname, level, yrs_service):
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = yrs_service

    # implement comparison functions by emp level
    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    def __eq__(self, other):
        return self.level == other.level


def main():
    # define some employees
    dept = [Employee("Tim", "Sims", 5, 9),
            Employee("John", "Doe", 4, 12),
            Employee("Jane", "Smith", 6, 6),
            Employee("Rebecca", "Robinson", 5, 13),
            Employee("Tyler", "Durden", 5, 12)]

    # who's more senior?
    print(dept[0] > dept[2])
    print(dept[4] < dept[3])

    # sort the items
    emps = sorted(dept)
    for e in emps:
        print(e.fname, end=" ")


if __name__ == "__main__":
    main()
