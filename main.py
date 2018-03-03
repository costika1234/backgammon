#!/usr/local/bin/python

from backgammon import Backgammon

def main():
    game = Backgammon(known_dice=[(6, 6), (6, 3)], 
                      known_moves=[(24, 24, 13, 13), (17, 17)],
                      terminate_on_auto=False)
    game.play()

if __name__ == "__main__":
    main()
