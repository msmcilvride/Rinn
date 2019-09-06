import rinnmath.helper_functions as hf


def generic_attack(attacker, initial_successes, initial_damage, additional_successes, additional_damage):
    """
    Performs a generic melee attack and returns the damage dealt.

    attacker = the character initiating the attack
    initial_successes = the minimum number of successes for the move to activate
    initial_damage = the initial damage dealt by the ability
    additional_successes =
    additional_damage =
    """
    # roll the dice
    results = hf.roll_d6(num=attacker.vitality, stat=attacker.body)
    successes = results['successes']

    # check for minimum successes (turn this into a function)
    if successes < initial_successes:
        return 0

    # calculate initial damage
    successes -= initial_successes
    damage = initial_damage

    # allow additional_successes to buy additional_damage
    while successes - additional_successes >= 0:
        successes -= additional_successes
        damage += additional_damage

    return damage


def generic_defense(defender, damage, initial_successes, initial_negated, additional_successes, additional_negated):
    """
    Performs a generic defense against damage and returns the damage dealt.

    defender = the character performing the defense
    damage = the amount of incoming damage
    initial_successes = the minimum number of successes for the move to activate
    initial_negated = the initial damage negation of the ability
    scaled_negated = the additional damage negation purchased with extra successes
    """
    # roll the dice
    results = hf.roll_d6(num=defender.vitality, stat=defender.body)
    successes = results['successes']

    # check for minimum successes (turn this into a function)
    if successes < initial_successes:
        return damage

    # calculate initial save
    successes -= initial_successes
    dam_negated = initial_negated

    # allow additional_successes to buy additional_damage
    while successes - additional_successes >= 0:
        successes -= additional_successes
        dam_negated += additional_negated

    # calculate damage_dealt, and prevent negative damage
    dam_dealt = damage - dam_negated
    if dam_dealt < 0:
        dam_dealt = 0

    return dam_dealt
