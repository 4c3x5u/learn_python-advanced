# deque objects are like double-ended queues

import collections
import string


def main():
    # initialise deque with all the lowercase letters
    d = collections.deque(string.ascii_lowercase)

    # print out the number of items in a deque
    print(f"letter count: {len(d)}")

    # iterate over a deque
    for elem in d:
        print(elem.upper(), end=" ")

    # manipulate items from either end
    d.pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(f"\n{d}")

    # rotate the deque
    d.rotate(10)
    print(f"\n{d}")


if __name__ == "__main__":
    main()
