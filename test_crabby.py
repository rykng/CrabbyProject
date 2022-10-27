import unittest

from crabby import CrabbyEngine

class TestCrabby(unittest.TestCase):

    def test_6_dices(self):
        result:list = CrabbyEngine.roll_crabby_dices(num_dice=6)
        self.assertTrue(len(result) == 6, msg="Crabby should return 6 outcomes in the list.")

    def test_roll(self):
        result:list = CrabbyEngine.roll_crabby_dices()
        self.assertTrue(len(result) == 3, msg="Crabby should return 3 outcomes in the list.")


