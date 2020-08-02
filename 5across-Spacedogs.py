#masses = [2,6,1,8,4,32,2] #Solution Unknown
#locations = [(10,),(9,),(1,),(2,),(7,),(16,),(50,)]
#masses = [5,2,1] #Solution 3 or 3.75
#locations = [(1,),(6,),(7,)] 

import math

def solution(masses, locations):

    #Sort dogs into ascending order
    
    sorted = merge_sort(masses, locations)
    masses = sorted[0]
    locations = sorted[1]
    
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
        coordMagFinLowest = 99999999999999999999999999
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
                closestDog = dogInd#masses = [2,6,1,8,4,32,2] #Solution Unknown
#locations = [(10,),(9,),(1,),(2,),(7,),(16,),(50,)]
#masses = [5,2,1] #Solution 3 or 3.75
#locations = [(1,),(6,),(7,)] 

import math

def solution(masses, locations):

    #Sort dogs into ascending order
    
    sorted = merge_sort(masses, locations)
    masses = sorted[0]
    locations = sorted[1]
    
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
        coordMagFinLowest = 99999999999999999999999999
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








def merge_sort(my_list, loc_list):
        #Find the lowest larger power of 2 than the size of the list
    log_2_len_u = math.ceil(math.log2(len(my_list)))
    req_len = math.pow(2,log_2_len_u)
    diff = int(req_len - len(my_list))

    my_max = max(my_list)+1
    for i in range(diff):
        my_list.append(my_max)
        loc_list.append(0)

    group_size = 1
    while(group_size < len(my_list)):
            #Double the size of the subgroups
        group_size = int(group_size)

            #new_list is the list after sorting the subgroups
        new_list = []
        new_list_loc = []
        ind_list = []
            #For loop to find the sublists to consider
        for i in range(math.floor(len(my_list)/(group_size*2))):
            ind_list.append( 2*group_size*i )

        for i in ind_list:
            sub_1 = []
            sub_2 = []
            sub_1_loc = []
            sub_2_loc = []
            for j in range(group_size):
                sub_1.append(my_list[i+j])
                sub_2.append(my_list[i+group_size+j])
                
                sub_1_loc.append(loc_list[i+j])
                sub_2_loc.append(loc_list[i+group_size+j])
            #print("sub_1: ", sub_1)
            #print("sub_2: ", sub_2)
            #print("")
            #print("")
            
            sorted_list_comp = pairwise_sorting(sub_1,sub_2,sub_1_loc,sub_2_loc)
            sorted_list = sorted_list_comp[0]
            sorted_list_loc = sorted_list_comp[1]

            for value in sorted_list:
                new_list.append( value )
            for value in sorted_list_loc:
                new_list_loc.append( value )
        my_list = new_list
        loc_list = new_list_loc
        #print("my_list: ", my_list)
        group_size *= 2
    my_list = my_list[0:len(my_list)-diff]
    loc_list = loc_list[0:len(loc_list)-diff]
    #print("Final List: ", my_list)
    
    return [my_list, loc_list]
    

def pairwise_sorting(list1,list2,loc1,loc2):
    return_list = []
    return_list_loc = []
    while (len(list1) != 0 and len(list2) != 0):
        if (list1[0] <= list2[0]):
            return_list.append( list1.pop(0) )
            return_list_loc.append( loc1.pop(0) )
        else:
            return_list.append( list2.pop(0) )
            return_list_loc.append( loc2.pop(0) )
    if (len(list1) == 0):
        for i in range(len(list2)):
            value = list2[i]
            return_list.append( value )
            return_list_loc.append( loc2[i] )
    else:
        for i in range(len(list1)):
            value = list1[i]
            return_list.append( value )
            return_list_loc.append( loc1[i] )
    return [return_list,return_list_loc]



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








def merge_sort(my_list, loc_list):
        #Find the lowest larger power of 2 than the size of the list
    log_2_len_u = math.ceil(math.log2(len(my_list)))
    req_len = math.pow(2,log_2_len_u)
    diff = int(req_len - len(my_list))

    my_max = max(my_list)+1
    for i in range(diff):
        my_list.append(my_max)
        loc_list.append(0)

    group_size = 1
    while(group_size < len(my_list)):
            #Double the size of the subgroups
        group_size = int(group_size)

            #new_list is the list after sorting the subgroups
        new_list = []
        new_list_loc = []
        ind_list = []
            #For loop to find the sublists to consider
        for i in range(math.floor(len(my_list)/(group_size*2))):
            ind_list.append( 2*group_size*i )

        for i in ind_list:
            sub_1 = []
            sub_2 = []
            for j in range(group_size):
                sub_1.append(my_list[i+j])
                sub_2.append(my_list[i+group_size+j])
                
                sub_1_loc.append(loc_list[i+j])
                sub_2_loc.append(loc_list[i+group_size+j])
            #print("sub_1: ", sub_1)
            #print("sub_2: ", sub_2)
            #print("")
            #print("")
            
            sorted_list_comp = pairwise_sorting(sub_1,sub_2,sub_1_loc,sub_2_loc)
            sorted_list = sorted_list_comp[0]
            sorted_list_loc = sorted_list_comp[1]

            for value in sorted_list:
                new_list.append( value )
            for value in sorted_list_loc:
                new_list_loc.append( value )
        my_list = new_list
        loc_list = new_list_loc
        #print("my_list: ", my_list)
        group_size *= 2
    my_list = my_list[0:len(my_list)-diff]
    loc_list = loc_list[0:len(loc_list)-diff]
    #print("Final List: ", my_list)
    
    return [my_list, loc_list]
    

def pairwise_sorting(list1,list2,loc1,loc2):
    return_list = []
    return_list_loc = []
    while (len(list1) != 0 and len(list2) != 0):
        if (list1[0] <= list2[0]):
            return_list.append( list1.pop(0) )
            return_list_loc.append( loc1.pop(0) )
        else:
            return_list.append( list2.pop(0) )
            return_list_loc.append( loc2.pop(0) )
    if (len(list1) == 0):
        for i in range(len(list2)):
            value = list2[i]
            return_list.append( value )
            return_list_loc.append( loc2[i] )
    else:
        for i in range(len(list1)):
            value = list1[i]
            return_list.append( value )
            return_list_loc.append( loc1[i] )
    return [return_list,return_list_loc]

