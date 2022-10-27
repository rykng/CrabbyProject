import random

class CrabbyEngine(object):

    CRABBY_D6 = ["fish", "crab", "prawn", "coin", "bottle", "roaster"]

    @classmethod
    def roll_crabby_dices(cls, num_dice=3) -> list:
        result = []
        for x in range(num_dice):
            outcome:str = random.choice(cls.CRABBY_D6)
            #print(f"{x}->{outcome}")
            result.append(outcome)

        return result





