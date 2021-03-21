def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a list of fahrenheit temperatures
    ftemp_list = [(t*9/5)+35 for t in ctemps]
    print(f"ftemp_list: {ftemp_list}")

    # build a set of unique fahrenheit temperatures
    ftemp_set = {(t*9/5)+35 for t in ctemps}
    print(f"set: {ftemp_set}")

    # built a set from an input source
    strval = "The quick brown fox jumped over the lazy dog"
    chars = {c.upper() for c in strval if not c.isspace()}
    print(chars)


if __name__ == "__main__":
    main()
