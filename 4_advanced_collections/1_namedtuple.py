import collections


def main():
    # create a Point namedtuple
    Point = collections.namedtuple("Point", "x y")
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(p1, p2)

    # use descriptive names to access namedtuple data
    print(p1.x, p2.y)

    # use _replace() to create a new instance
    p1_new = p1._replace(x=100)
    print(p1_new)


if __name__ == "__main__":
    main()
