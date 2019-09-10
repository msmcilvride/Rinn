import pandas as pd
import rinnmath.character_classes as cc
import rinnmath.game_functions as gf
import rinnmath.analytics as an
import rinnmath.stat_tests as st

# character parameters
char = cc.Villager()

# ability parameters
ability = {
    'initial_successes': 1,
    'initial_output': 1,
    'additional_successes': 1,
    'additional_output': 1
}

# laboratory
test_name = '1Fast'
data = an.level_test(st.generic_ability_test, char, ability, iterations=10000)
df = pd.DataFrame(data)
df.to_csv('outputs/' + test_name + '.csv', index=False)

# TODO
# Roll for generic abilities, not attack v defense. Only look at the raw damage done/mitigated in a matrix.
