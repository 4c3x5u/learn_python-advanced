def main():
    # define two lists of numbers
    evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

    # perform mapping and filtering on a list
    evens_sqrd = list(map(lambda a: a**2, filter(lambda a: 4 < a < 16, evens)))
    print(evens_sqrd)

    # derive a new list of numbers from a given list (comprehension)
    evens_sqrd = [a ** 2 for a in evens]
    print(evens_sqrd)

    # limit the items operated on with a predicate condition (comprehension)
    odds_sqrd = [a ** 2 for a in odds if 3 < a < 17]
    print(odds_sqrd)


if __name__ == "__main__":
    main()
