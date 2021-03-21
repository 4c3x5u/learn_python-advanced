from collections import defaultdict


def main():
    # define a list of items that we want to count
    fruits = ["apple", "pear", "orange", "banana",
              "apple", "grape", "banana", "banana"]

    # use defaultdict to create a dictionary that of which values, if we try
    # to access, will be initialised by the constructor function passed in
    fruit_counter = defaultdict(lambda: 100)

    # count the elements in the list
    for f in fruits:
        fruit_counter[f] += 1

    # print the results
    for k, v in fruit_counter.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    main()
