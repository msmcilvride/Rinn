import rinnmath.helper_functions as hf


def generic_body_ability(character, initial_successes, initial_output, additional_successes, additional_output):
    """
    Performs a generic ability and returns the output.

    character = the character using the ability
    initial_successes = the minimum number of successes for the move to activate
    initial_output = the initial output of the ability
    additional_successes =
    additional_output =
    """
    # roll the dice
    results = hf.roll_d6(num=character.vitality, stat=character.body)
    successes = results['successes']

    # check for minimum successes (turn this into a function)
    if successes < initial_successes:
        return 0

    # calculate initial damage
    successes -= initial_successes
    total_output = initial_output

    # allow additional_successes to buy additional_damage
    while successes - additional_successes >= 0:
        successes -= additional_successes
        total_output += additional_output

    return total_output
