from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sport_teams = [("Royals", (18, 12)), ("Rockets", (24, 6)),
                   ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                   ("Kings", (15, 15)), ("Chargers", (20, 10)),
                   ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sorted_teams = sorted(sport_teams, key=lambda t: t[1][0], reverse=True)
    print(sorted_teams)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sorted_teams)
    print(teams)

    # use popitem to remove the top item as if we were working with a stack
    tm, wl = teams.popitem(False)
    print(f"Top team: {tm} {wl}")

    # what are the next top 4 teams?
    for i, team in enumerate(teams, start=1):
        print(i, team)
        if i == 4:
            break

    # test regular dict objects for equality (order doesn't matter)
    a = {"a": 1, "b": 2, "c": 3}
    b = {"a": 1, "c": 3, "b": 2}
    print(f"\nequality test: {a == b}")

    # test OrderedDicts for equality (order matters)
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print(f"\nequality test: {a == b}")


if __name__ == "__main__":
    main()
