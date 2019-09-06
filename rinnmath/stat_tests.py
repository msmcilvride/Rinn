import rinnmath.game_functions as gf


def generic_round(attacker, defender, attack, defense, iterations=1000):
    """
    Tests a generic attack against a generic defense.

    attacker = the character performing the melee attack
    defender = the character defending with a avoid
    iterations = the number of times to run the test
    """
    results = []
    for _ in range(iterations):
        damage = gf.generic_attack(attacker,
                                   initial_successes=attack['initial_successes'],
                                   initial_damage=attack['initial_damage'],
                                   additional_successes=attack['additional_successes'],
                                   additional_damage=attack['additional_damage'])
        damage = gf.generic_defense(defender, damage,
                                    initial_successes=defense['initial_successes'],
                                    initial_negated=defense['initial_negated'],
                                    additional_successes=defense['additional_successes'],
                                    additional_negated=defense['additional_negated'])
        results.append(damage)

    return results
