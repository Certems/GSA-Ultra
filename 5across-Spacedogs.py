#masses = [2,6,1,8,4,32,2] #Solution Unknown
#locations = [(10,),(9,),(1,),(2,),(7,),(16,),(50,)]
#masses = [5,2,1] #Solution 3 or 3.75
#locations = [(1,),(6,),(7,)] 

import math

def solution(masses, locations):

    #Sort dogs into ascending order
    moveItem = 0
    while True:
        switched = False
        for dogInd in range(len(masses)):
            if dogInd +1 < len(masses):
                if masses[dogInd +1] < masses[dogInd]:
                    moveItem = masses.pop(dogInd +1)
                    masses.insert(dogInd, moveItem)
                    moveItem = locations.pop(dogInd +1)
                    locations.insert(dogInd, moveItem)
                    switched = True
        if switched == False:
            break
    #Establish number of dimensions
    DimensionNumber = len(locations[0])
    #print("SortedMasses: ",masses)
    #print("SortedLocations: ",locations)
    #print("DimensionNumber: ",DimensionNumber)
    
    while True:
        #Establish smallest dog
        smallestDog = 0
        #print("-----")
        #print("massesStart: ",masses)
        #print("locationsStart: ",locations)
        
        #Find closest dog
        coordMagFinLowest = 999999999999999999999999999999999999
        closestDog = 0
        for dogInd in range(len(masses)):
            coordMag = 0
            coordMagTot = 0
            coordMagFinNew = 0
            if dogInd == 0:
                continue #Skip smallest dog
            for coord in range(DimensionNumber):
                coordMag = ( (locations[smallestDog][coord]) -  (locations[dogInd][coord]) )**2
                coordMagTot += coordMag
            coordMagFinNew = ( coordMagTot )**(1/2)
            if coordMagFinNew < coordMagFinLowest:
                coordMagFinLowest = coordMagFinNew
                closestDog = dogInd

        #Find mass of new dog
        newMass = masses[smallestDog]+masses[closestDog]
        
        #Find midpoint of both dogs
        finalCoords = ()
        for coord in range(DimensionNumber):
            currentCoord = []
            currentCoord.append(  math.floor(( ( locations[smallestDog][coord] ) + ( locations[closestDog][coord] ) )/2)   )
            finalCoords = finalCoords + tuple(currentCoord)
            #print("currentCoord(Mid): ",currentCoord)
            #print("finalCoords(Mid): ",finalCoords)
        
        #Insert new winning dog
        #print("newMass: ",newMass)
        for dogInd in range( len(masses) - closestDog ):
            if ( (dogInd +closestDog +1) == len(masses) ): #Last element of list => by now it is the largest
                masses.append(newMass)
                locations.append(finalCoords)
                break
            lowerBound = masses[dogInd +closestDog] < newMass
            upperBound = masses[dogInd +closestDog +1] > newMass
            if ( (lowerBound) and (upperBound) ): #If it just fits somewhere in the middle of the list
                masses.insert(dogInd +closestDog+1, newMass)
                locations.insert(dogInd +closestDog+1, finalCoords)
                break

        #Remove both old dogs
        #print("---->>")
        #print("Adding mass ",newMass)
        #print("Removing index ",closestDog," and ",smallestDog)
        #print(masses)
        masses.pop(closestDog) #Masses and locations should have unchanged indexs because newMass always inserted after previous two
        #print(masses)
        masses.pop(smallestDog)
        #print(masses)
        locations.pop(closestDog) #(Both smallestDogs should both just be 0)
        locations.pop(smallestDog)

        #Check for one dog left, if so then break
        if len(masses) == 1:
            break
    #Find coord sum for remaining dog
    #print("m2: ",masses)
    #print("loc2: ",locations)
    coordTot = 0
    for coord in range(DimensionNumber):
        #print("locations[0][coord]: ",locations[0][coord])
        coordTot += locations[0][coord]
        
    #Return coord sum
    return coordTot

#print ( solution(masses, locations) )
