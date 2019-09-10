import rinnmath.game_functions as gf


def generic_ability_test(character, ability, iterations=1000):
    """
    Tests a generic attack against a generic defense.

    attacker = the character performing the melee attack
    defender = the character defending with a avoid
    attack =
    defense =
    iterations = the number of times to run the test
    """
    results = []
    for _ in range(iterations):
        output = gf.generic_ability(character,
                                   initial_successes=ability['initial_successes'],
                                   initial_output=ability['initial_output'],
                                   additional_successes=ability['additional_successes'],
                                   additional_output=ability['additional_output'])
        results.append(output)

    return results
