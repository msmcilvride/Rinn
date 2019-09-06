import statistics as st

# analytics


def test_for_levels(test, attacker, defender, attack, defense, iterations=1000, min_lvl=1, max_lvl=10):
    """
    Performs the specified test for each of the specified levels.

    test = the test function to be used
    attacker = the attacking character
    defender = the defending character
    iterations = the number of times to run the test per level
    min_lvl = the lowest level to test
    max_lvl = the highest level to test
    """
    # declare variables
    data = {
        'level': [],
        'mean': [],
        'median': [],
        'mode': [],
        'min': [],
        'max': [],
        'mode per': [],
        'min per': [],
        'max per': []
    }

    # lower vitality by 1 for the for loop
    attacker.vitality = min_lvl - 1
    defender.vitality = min_lvl - 1

    for lvl in range(max_lvl):
        attacker.vitality += 1
        defender.vitality += 1

        # perform the test
        results = test(attacker, defender, attack, defense, iterations=iterations)

        # record aggregates
        # TODO: make this a function
        data['level'].append(attacker.vitality)
        data['mean'].append(st.mean(results))
        data['median'].append(int(st.median(results)))
        data['mode'].append(st.mode(results))
        data['min'].append(min(results))
        data['max'].append(max(results))
        data['mode per'].append(results.count(st.mode(results)) / iterations)
        data['min per'].append(results.count(min(results)) / iterations)
        data['max per'].append(results.count(max(results)) / iterations)

    return data


# TODO: use this to process analytics
def standard_spread():
    pass
