import unittest

from backgammon import Backgammon

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


if __name__ == '__main__':
    unittest.main()
