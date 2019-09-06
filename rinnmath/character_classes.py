class Villager:
    def __init__(self):
        self.level = 1
        self.wounds = 0
        self.vitality = self.level - self.wounds
        # this should be a lambda function
        # or there could be a method that updates vitality

        self.body = 4
        self.mind = 4
        self.spirit = 4
        self.magic = 4


class Fighter:
    def __init__(self):
        self.level = 1
        self.wounds = 0
        self.vitality = self.level - self.wounds

        self.body = 3
        self.mind = 4
        self.spirit = 4
        self.magic = 5
