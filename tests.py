import unittest

from backgammon import Backgammon
from utils import Utils

class TestBackgammonGame(unittest.TestCase):
    def setUp(self):
        self.game = Backgammon()

    def test_initial_setup(self):
        self.assertEquals(self.game.players[0], 
                          [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 
                           5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])
        self.assertEquals(self.game.players[1], 
                          [0, 0, 0, 0, 0, 5, 0, 3, 0, 0, 0, 0, 
                           5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])

    def test_generated_dice_order(self):
        (dice1, dice2) = Utils.roll_dice()
        self.assertTrue(dice1 >= dice2)

        (dice1, dice2) = Utils.roll_dice()
        self.assertFalse(dice1 < dice2)        


if __name__ == '__main__':
    unittest.main()
