N = 5000
snakes = [(6,5),(13,7)] 
ladders = [(2,5),(3,9)]

import random #Exclude 1st, include 2nd
import math

def solution(N, snakes, ladders):
    average = 0
    #MULTI-TEST START
    testNum = 1 # <---------------------- Change this to adjust number of tests performed
    for test in range(testNum):#<---------- Number of tests to form average
        #Establish starting values
        position = 0
        turnCount = 0
        #print("Snakes: ",snakes)
        #print("Ladders: ",ladders)

        #GAME LOOP
        while True:
            #Increment turn
            turnCount += 1
            #print("------>")
            #print("Turn: ",turnCount)
            
            #Roll the die
            dRoll = random.randint(0,6)
            #print("dRoll: ",dRoll)

            #Move approporiate number of squares (without going over last tile)
            position += dRoll
            #print("Position: ",position)
            if position > (N-1): #Win condition
                position = (N-1)
                break

            #Check for snakes or ladders, then move (or not) accordingly
            if position <= N/2:
                for square in range(math.ceil(len(snakes))):
                    if position == snakes[square][0]:
                        position = snakes[square][1]
                        #print("Down Snake")
                        break
                for square in range(math.ceil(len(ladders))):
                    if position == ladders[square][0]:
                        position = ladders[square][1]
                        #print("Up Ladder")
                        break
            ## <-------------------------------------------------> Double "if" should mean half the volume of numbers are being tested
            if position > N/2:
                for square in range(math.floor(len(snakes)/2)):
                    if position == snakes[len(snakes) - square -1] [0]:
                        position = snakes[len(snakes) - square -1][1]
                        #print("Down Snake")
                        break
                for square in range(math.floor(len(ladders))):
                    if position == ladders[len(ladders) - square -1][0]:
                        position = ladders[len(ladders) - square -1][1]
                        #print("Up Ladder")
                        break
        average += turnCount
    averageFinal = math.floor(average / testNum)
    return averageFinal

print(solution(N, snakes, ladders))
