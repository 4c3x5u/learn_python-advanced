import itertools


def test_func(x):
    return x < 40


def main():
    # cycle iterators can be used to cycle over a collection (INFINITE)
    seq1 = ["Joe", "John", "Mike"]
    # cycle1 = itertools.cycle(seq1)
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))
    # print(next(cycle1))

    # use count() to create a simpler counter (INFINITE)
    # count1 = itertools.count(100, 10)
    # print(next(count1))
    # print(next(count1))
    # print(next(count1))

    # accumulate() creates an iterator that accumulates values
    vals = [10, 20, 30, 40, 50, 40, 30]
    # acc1 = itertools.accumulate(vals, max)
    # print(list(acc1))

    # use chain() to connect sequences together
    x = itertools.chain("ABCD", "1234")
    print(list(x))

    # dropwhile() and takewhile() will return values until a certain condition
    # is met
    print(list(itertools.dropwhile(test_func, vals)))
    print(list(itertools.takewhile(test_func, vals)))


if __name__ == "__main__":
    main()
