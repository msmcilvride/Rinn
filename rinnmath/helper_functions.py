import random as rd


# helper functions


def roll_d6(num, stat):
    """
    Returns an array of dice results:
        results: raw dice results
        successes: the number of successes rolled
        failures: the number of failures rolled

    num = the number of dice to roll
    stat = the number to meet or beat to generate a success


    """
    results = []
    successes = 0
    failures = 0

    # roll the dice
    for die in range(num):
        result = rd.randint(1, 6)
        results.append(result)

    # calculate successes
    for result in results:
        if result <= stat:
            successes += 1
        else:
            failures += 1

    # catalog data
    data = {
        'results': results,
        'successes': successes,
        'failures': failures
    }

    return data
