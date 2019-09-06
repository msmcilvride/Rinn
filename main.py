import pandas as pd
import rinnmath.character_classes as cc
import rinnmath.game_functions as gf
import rinnmath.analytics as an
import rinnmath.stat_tests as st

# character parameters
x = cc.Villager()
y = cc.Villager()

# attack/defense parameters
attack = {
    'initial_successes': 1,
    'initial_damage': 3,
    'additional_successes': 1,
    'additional_damage': 2
}

defense = {
    'initial_successes': 1,
    'initial_negated': 1,
    'additional_successes': 2,
    'additional_negated': 1
}

# laboratory
data = an.test_for_levels(st.generic_round, x, y, attack, defense, iterations=10000)
df = pd.DataFrame(data)
df.style.hide_index()

# TODO
# Roll for generic abilities, not attack v defense. Only look at the raw damage done/mitigated in a matrix.
