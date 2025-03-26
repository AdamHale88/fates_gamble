import random
 
totalShotsFired = 0
def increaseShotCounter () :
    totalShotsFired = totalShotsFired + 1
    return(totalShotsFired)

playersScore = 0
def increasePlayersScore ():
    playersScore = playersScore + 100
    return(playersScore)

bullet = random.randint(1,5)