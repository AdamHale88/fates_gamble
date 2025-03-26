import random
import os
def main ():
    def clear_screen():
    # For Windows
        if os.name == 'nt':
            _ = os.system('cls')
    # For macOS and Linux
        else:
            _ = os.system('clear')
    bullet = random.randint(1,5)
    dash = '-' * 40
    totalShotsFired = 0
    userScore = 0
    strUserSelection = ""
    while totalShotsFired != 5 and strUserSelection !='X':
        try:    
            print()
            print(dash)
            print("         Fates Gamble            ")
            print()
            print(dash)
            print()
            print("Total Shots: ",totalShotsFired, " | " "Cash: $",userScore)
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
            strUserSelection = input("Selection:  ")
            print()
            if strUserSelection.upper() == "T":
                userShot = random.randint(1,5)
                computersShot = random.randint(1,5)
                if userShot == bullet:
                    print()
                    print()
                    print("YOU ARE DEAD!")
                    print()
                    totalShotsFired = 0
                else:
                    totalShotsFired = totalShotsFired + 1
                    userScore = userScore + 100
                    if computersShot == bullet:
                        print("Computer Lost!")
                        print()             
                        print("Continue?")
                        print()
                        print()
                        strUserSelection = input( "(Y) for Yes or (N) for No :      ")
                        print()
                        print()
                        if strUserSelection.upper() == ("Y"):
                            totalShotsFired = 0
                            userScore = userScore + 100
                        else:
                            strUserSelection = "X"   
                
            elif strUserSelection.upper() == "P":
                userScore = userScore - 10
                computersShot = random.randint(1,5)
                if computersShot == bullet:
                    print("You Won!")
                    print()             
                    print("Continue?")
                    print()
                    print()
                    strUserSelection = input( "(Y) for Yes or (N) for No :      ")
                    print()
                    print()
                    if strUserSelection.upper() == ("Y"):
                        totalShotsFired = 0
                        userScore = userScore + 100
                        print(dash)
                    else:
                        strUserSelection = "X"  
                else:
                    totalShotsFired = totalShotsFired+ 1
                    print("Choose Again.")
                    print()
                    print()
                    print()             
            else: 
                strUserSelection = "X"
                print()
                print("Death comes for all.......")
                print()
        finally:
            if totalShotsFired == 5:
                print("Gun is Dry , Congrats you survived!")
                print()            
                print("New game ?")
                print()
                print()
                strUserSelection = input( "(Y) for Yes or (N) for No :      ")
                print()
                print()
                if strUserSelection.upper() == ("Y"):
                        totalShotsFired = 0
                        userScore = 0
                else:
                    strUserSelection = "X"
            else:
                None  
main()
 
