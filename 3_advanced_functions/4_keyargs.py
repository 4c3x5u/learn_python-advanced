# use keyword-only arguments to help ensure code clarity
def my_func(arg1, arg2, *, suppressExceptions=False):
    pass


def main():
    # try to call the function with and without the keyword
    # my_func(1, 2, True) # ERROR
    my_func(1, 2, suppressExceptions=True)


if __name__ == "__main__":
    main()
