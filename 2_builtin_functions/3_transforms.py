def filter_func(num):
    if num % 2 == 0:
        return False
    return True


def filter_func2(x):
    if x.isupper():
        return False
    return True


def map_func(x):
    return x ** 2


def to_grade(x):
    if x >= 90:
        return "A"
    elif 80 <= x < 90:
        return "B"
    elif 70 <= x < 80:
        return "C"
    elif 65 <= x < 70:
        return "D"
    elif 60 <= x < 65:
        return "E"
    else:
        return "F"


if __name__ == "__main__":
    # some sample sequences to operate on
    numbers = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    characters = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter() to remove items from a sequence
    odds = list(filter(filter_func, numbers))
    print(odds)

    # use filter() on a non-numeric sequence
    lowers = list(filter(filter_func2, characters))
    print(lowers)

    # use map() to create new sequence of values
    squared_numbers = list(map(map_func, numbers))
    print(squared_numbers)

    # use sorted() and map() to change numbers to grades
    sorted_grades = sorted(grades)
    letter_grades = list(map(to_grade, sorted_grades))
    print(letter_grades)

