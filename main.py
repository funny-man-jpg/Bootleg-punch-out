# Author: Sabin Caragea
# This program is a game where you must win a boxing match.

from game import Game

# Define the main class, get it to run our game and such
def main():
  game = Game(500, 300)
  game.run()

# Call main so it runs
if __name__ == "__main__":
  main()

