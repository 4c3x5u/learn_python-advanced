# define a function that takes variable-length arguments
def addition(*args):
    result = 0
    for i in args:
        result += i
    return result


def main():
    # pass different arguments
    print(addition(5, 10, 20, 45))
    print(addition(1, 2, 3))

    # pass an existing list
    nums = [5, 10, 20, 45]
    print(addition(*nums))


if __name__ == "__main__":
    main()
