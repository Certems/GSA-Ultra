#import pickle
import math
#masses = [5,2,1]
#locations = [(1,),(6,),(7,)]

#masses = pickle.load(open("sl_spacedogs.pkl","rb"))[0]
#locations = pickle.load(open("sl_spacedogs.pkl","rb"))[1]

def solution(masses, locations):

    ##BUBBLESORT (masses and locations) INEFFICIENT, BETTER WITH MERGE SORT
    mItem = 0#Moving item
    while True:
        valSwitch = False#Check for any movement in a given cycle
        for indDog in range(len(masses)):
            if indDog+1 < len(masses):#If not overflowing
                if masses[indDog] > masses[indDog+1]:
                    mItem = masses.pop(indDog+1)
                    masses.insert(indDog,mItem)
                    mItem = locations.pop(indDog+1)
                    locations.insert(indDog,mItem)
                    valSwitch = True#movement occured in given cycle
        if valSwitch == False:
            break
    ##BUBBLESORT
    
    #Find dimensions
    dogDim = len( locations[0] ) #Number of coords for any given spacedog => number of dimensions
        
    while True:
        dist = 0
        #Find smallest dog
        smallDog = 0#1st (0th index) dog is always smallest (sorted)
        
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

        #Remove both dogs
        masses.pop(closeDog)
        masses.pop(smallDog)#Should always pop 0
        locations.pop(closeDog)
        locations.pop(smallDog)#Should always pop 0
        #e.g [{a},b,c,{d},e,f,g] --> [b,c,e,f,g], checking up from (and including) e, index 2, counting 3 times (in terms of masses)

        #Remove from list and re-place newDog (closeDog) into correct place in masses (ordered)
        for indDog in range( len(masses) - closeDog+1 ):#Check all dogs after close dog, because mass only gets larger
            upperCase = (newMass <= masses[indDog + closeDog-1])
            lowerCase = (newMass >= masses[indDog + closeDog-2])
            finalCase = upperCase and lowerCase
            if closeDog == 1:
                masses.insert(0,  newMass)
                locations.insert(0, Fcoords)
                break
            if finalCase == True:#If it fits inbetween the masses
                masses.insert((indDog + closeDog-1),    newMass)
                locations.insert((indDog + closeDog-1),  Fcoords)
                break
            if indDog == len(masses) -1:#DOG AT END OF THE LINE
                masses.append(newMass)
                locations.append(Fcoords)
                break
        if len(masses) == 0:
            masses.append( newMass)
            locations.append(Fcoords)

        #Now loop cycle ( until one left )
        if len( masses ) == 1:
            break

    #Output sum of coords
    sumation = 0
    for coords in range(dogDim):
        sumation += (locations[0][coords])
    return sumation

#print( solution(masses, locations) )
