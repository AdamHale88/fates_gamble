import main_game
import player_module
import computer_module
import math_functions
def checkGameState ():
    if main_game.playerSelection.upper() == "T":
                math_functions.bullet
                player_module.playerShot
                computer_module.computersShot
                if player_module.playersShot == math_functions.bullet:
                    print()
                    print()
                    print("YOU ARE DEAD!")
                    print()
                    math_functions.totalShotsFired = 0
                elif computer_module.computersShot == math_functions.bullet:
                    print()
                    print("Computer is Dead. You win!")
                    print()
                    print("Continue?")
                    print()
                    print()
                    strUserSelection = input( "(Y) for Yes or (N) for No :      ")
                    print()
                    print()
                    if strUserSelection.upper() == ("Y"):
                        math_functions.totalShotsFired = 0
                        math_functions.playersScore = math_functions.playersScore + 100
                    else:
                        strUserSelection = "X"   