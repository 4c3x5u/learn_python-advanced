class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Point x:{self.x},y:{self.y}>"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __iad__(self, other):
        self.x += other.x
        self.y += other.y


def main():
    p1 = Point(10, 20)
    p2 = Point(30, 30)
    print(f"p1: {p1}, p2: {p2}")

    # add two points
    p3 = p1 + p2
    print(f"p3: {p3}")

    # subtract two points
    p4 = p2 - p1
    print(f"p4: {p4}")

    # perform in-place addition
    p1 += p2
    print(f"p1: {p1}")


if __name__ == "__main__":
    main()
