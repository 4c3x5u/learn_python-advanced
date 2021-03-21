if __name__ == "__main__":
    list1 = [1, 2, 3, 0, 5, 6]

    # any() will return true if any of the sequence values are true
    print(f"any: {any(list1)}")

    # all() will return true if all of the sequence values are true
    print(f"all: {all(list1)}")

    # min() and max() will return minimum and maximum values in a sequence
    print(f"min: {min(list1)}")
    print(f"max: {max(list1)}")

    # sum() adds up all the values in a sequence
    print(f"sum: {sum(list1)}")
