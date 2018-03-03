#!/usr/local/bin/python

from backgammon import Backgammon

def main():
    game = Backgammon(manual_dice=[(6, 6)])
    game.play()

if __name__ == "__main__":
    main()
