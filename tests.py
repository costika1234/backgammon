#!/usr/local/bin/python

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

    def test_one_simple_move_each(self):
        self.game = Backgammon(known_dice=[(6, 6), (6, 3)], 
                               known_moves=[(24, 24, 13, 13), (17, 17)],
                               terminate_on_auto=True,
                               suppress_output=True)
        self.game.play()
        self.assertEquals(self.game.players[0], 
                          [0, 0, 0, 0, 0, 5, 2, 3, 0, 0, 0, 0, 
                           3, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0])
        self.assertEquals(self.game.players[1], 
                          [0, 1, 0, 0, 1, 5, 0, 1, 0, 0, 0, 0,
                           5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2])


if __name__ == '__main__':
    unittest.main()
