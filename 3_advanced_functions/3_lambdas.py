def celcius_to_farenheit(temp):
    return (temp * 9/5) + 32


def farenheit_to_celcius(temp):
    return (temp - 32) * 5/9


def main():
    ctemps = [0, 12, 34, 100]
    ftemps = [32, 65, 100, 212]

    # use regular functions to convert temps
    print(list(map(celcius_to_farenheit, ctemps)))
    print(list(map(farenheit_to_celcius, ftemps)))

    # use lambdas to accomplish the same result
    print(list(map(lambda t: (t * 9 / 5) + 32, ctemps)))
    print(list(map(lambda t: (t - 32) * 5 / 9, ftemps)))


if __name__ == "__main__":
    main()
