# DOCSTRINGS BEST PRACTICES
# 1. Enclose docstrings in triple-quotes
# 2. First line should be summary sentence of functionality
# 3. Modules: List important classes, functions, and exceptions
# 4. Classes: List important methods.
# 5. Functions:
#   5a. List parameters and explain each, one per line.
#   5b. If there's a return value, list it; otherwise omit.
#   5c. If the function raises exceptions, list them
# For more information, refer to PEP 257

def my_function(arg1, arg2=None):
    """
    my_function(arg1, arg2=None) --> prints the given arguments
    :param arg1: The first argument. Whatever you feel like passing
    :param arg2: The second argument. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(my_function.__doc__)


if __name__ == "__main__":
    main()
