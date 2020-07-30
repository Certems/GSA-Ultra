#import pickle
import math
#masses = [5,2,1]
#locations = [(1,),(6,),(7,)]

#masses = pickle.load(open("sl_spacedogs.pkl","rb"))[0]
#locations = pickle.load(open("sl_spacedogs.pkl","rb"))[1]

def solution(masses, locations):

    #Find dimensions
    dogDim = len( locations[0] ) #Number of coords for any given spacedog => number of dimensions
        
    while True:
        dist = 0
        #print(masses)
        #print(locations)
        #Find smallest dog
        smallDog = 0#1st dog (0) as base smallest
        for Dog in  range(len(masses)):
            #print("Dog: ",Dog)
            #print("smallDog test: ",smallDog)
            if masses[Dog] < masses[smallDog]:#DOES NOT ACCOUNT FOR EQUAL MASSES OF DOG
                smallDog = Dog
                #print("Final: ",smallDog)
            #print(" ")

        #Find dog to fight ( find closest dog )
        Cdist = 0 #Current iterations distance
        Sdist = 99999999999999999999999999 #Shortest distance for given dog
        closeDog = 0#smallDog's closest dog
        winDog = 0#The dog which wins fight
        for oppDog in range(len(masses)):
            if oppDog == smallDog:#Skip fighting yourself MIGHT NEED END CASE E.G IF LAST ELEMENT MAY BREAK WHEN CONTINUING
                continue
            for coord in range(dogDim):
                dist = ( ( locations[smallDog][coord]  -  locations[oppDog][coord] ) )**2#Pythag for abs leng
                Cdist += dist
            Cdist = Cdist**(1/2)
            if Cdist < Sdist: # CURRENTLY NO EDGECASE RESOLUTION ** e.g multiple same dist is first come first serve
                closeDog = oppDog
                Sdist = Cdist
                
        #Opponent ( close ) dog always wins
        newMass = masses[closeDog] + masses[smallDog]

        #Move winning dog to middle
        
        Fcoords = ()
        for coords in range(dogDim):
            Ccoord = []
            Ccoord.append( math.floor(( locations[smallDog][coords] + locations[closeDog][coords] )/2 ) )
            Fcoords = Fcoords + tuple(Ccoord)

        #CloseDog DNA
        masses.insert(closeDog, newMass)
        locations.insert(closeDog, Fcoords)
        #Darwinism CloseDog
        masses.pop(closeDog +1)
        locations.pop(closeDog +1)
        #Clean Genepool (of smallDog)
        masses.pop(smallDog)
        locations.pop(smallDog)

        #Now loop cycle ( until one left )
        if len( masses ) == 1:
            break

    #Output sum of coords
    sumation = 0
    for coords in range(dogDim):
        sumation += (locations[0][coords])
    return sumation

#print( solution(masses, locations) )
