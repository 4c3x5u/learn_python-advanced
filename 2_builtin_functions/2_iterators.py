if __name__ == "__main__":
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    days_fr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter() to create an iterator over a collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))

    # iterate using a function and a sentinel
    with open("textfile.txt") as fp:
        for line in iter(fp.readline, ""):
            print(line)

    # use regular iteration over the days with an index
    for i in range(len(days)):
        print(i+1, days[i])

    # use enumerate() to reduce code and provide a counter
    for i, d in enumerate(days, start=1):
        print(i, d)

    # use zip to combine sequences
    for i, (d, d_fr) in enumerate(zip(days, days_fr), start=1):
        print(f"{i} {d} = {d_fr} in French")
