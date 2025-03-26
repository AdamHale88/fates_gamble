import math_functions
import os
def main ():
    dash = ("_")*40
    playerSelection = ""
    while math_functions.totalShotsFired != 5 and playerSelection !='X':
        try:
            print()
            print(dash)
            print("         Fates Gamble            ")
            print()
            print(dash)
            print()
            print("Total Shots: ",math_functions.totalShotsFired, " | " "Cash: $",math_functions.playersScore)
            print()
            print(dash)
            print()
            print("( T ): Trigger")
            print()
            print("( P ): Pass")
            print()
            print("( X ): Easy Way Out")
            print() 
            print()
            playerSelection = input("Selection:  ")
            print()
        finally:
            if math_functions.totalShotsFired == 5:
                print()          
                print("New game ?")
                print()
                print()
                playerSelection = input( "(Y) for Yes or (N) for No :      ")
                print()
                print()
                if playerSelection.upper() == ("Y"):
                        math_functions.totalShotsFired = 0
                        math_functions.playerScore = 0
                else:
                    playerSelection = "X"
            else:
                None  
main()