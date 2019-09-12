import pandas as pd
import rinnmath.character_classes as cc
import rinnmath.game_functions as gf
import rinnmath.analytics as an
import rinnmath.stat_tests as st

# character parameters
char = cc.Villager()

char.body = 3

# ability parameters
ability = {
    'initial_successes': 1,
    'initial_output': 1,
    'additional_successes': 1,
    'additional_output': 1
}

ability_name = str(ability['initial_successes']) +\
               str(ability['initial_output']) +\
               str(ability['additional_successes']) +\
               str(ability['additional_output'])

# laboratory
data = an.level_test(st.generic_ability_test, char, ability, iterations=10000)
df = pd.DataFrame(data)
df.to_csv('outputs/' + ability_name + '.csv', index=False)

# TODO
# create two outputs: a single csv for each result set, and a single csv for all means, modes, etc
# Automate the process of testing each ability variant and saving the output as a csv
