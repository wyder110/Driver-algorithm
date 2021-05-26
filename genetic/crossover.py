import random
from copy import copy

from confLoader import Configuration as Configuration


def copyFirstPart(listFrom, cross, crossingPlace, takenPackeges):
    '''kopiuje pierwszą część treca'''
    for j in range(crossingPlace): #kopiuje pierwszą część crossa
        tup = (listFrom[j][0], listFrom[j][1], copy(listFrom[j][2]))
        cross.append(tup)
        for pac in listFrom[j][2]: 
            takenPackeges.add(pac)

def deliverAndCopyPackages(cross, newTrailer, takenPackeges):
    '''kopiuje paczki z poprzedniego traca i wyrzuca paczki które dotarły do lokalizacji'''
    currentCarry = 0
    for idOfPack in cross[-1][2]:
        if Configuration.packagesId[idOfPack]['to'] != cross[-1][1]:
            newTrailer.append(idOfPack)
            takenPackeges.add(idOfPack)
            currentCarry += Configuration.packagesId[idOfPack]['weigth'] 
    return currentCarry

def takeNewPackages(listTo, newTrailer, takenPackeges, takenTo, currentCarry, parameters):
    for pac in takenTo:
        if pac not in takenPackeges:
            if currentCarry + Configuration.packagesId[pac]['weigth'] <= parameters["maxCarry"]:
                takenPackeges.add(pac)
                newTrailer.append(pac)
                currentCarry += Configuration.packagesId[pac]['weigth']


def copySecondPart(listTo, cross, crossingPlace, takenPackeges):
    '''kopiuje drugą część treca'''
    for j in range(crossingPlace+1, len(listTo)):
        newTrailer = []
        currentCarry = deliverAndCopyPackages(cross, newTrailer, takenPackeges)
        takenTo = list(set(listTo[j][2]) - set(listTo[j-1][2]))
        takeNewPackages(listTo, newTrailer, takenPackeges, takenTo, currentCarry, Configuration.parameters)
        tup = (listTo[j][0], listTo[j][1], newTrailer)
        cross.append(tup)

        # checkIfTraceIsCorrect(cross)



def crossover(cities, l1, l2):
    '''Single-point crossover'''
    
    randomList = list(range(1, len(l1)-1))
    random.shuffle(randomList)

    for i in randomList:
        rand = random.randint(0, 1) == 1
        listFrom = l1 if rand else l2
        listTo = l2 if rand else l1

        if listTo[i][1] in cities[listFrom[i][0]]: #można w tym miejscu przeciąć trace
            cross = []
            taken = set()
            copyFirstPart(listFrom, cross, i, taken)
            cross.append((listFrom[i][0], listTo[i][1], copy(listFrom[i][2]))) #punkt przecięcia pierwszej części z drugą częścią

            for idPack in listFrom[i][2]:
                    taken.add(idPack)

            copySecondPart(listTo, cross, i, taken)
            return cross
            

def checkIfTraceIsCorrect(trace):
    taken = set()
    left = set()
    
    for i in range(len(trace)):
        if i != 0:
            
            takenNow = set(trace[i][2]) - set(trace[i-1][2])
            if(len(taken.intersection(takenNow)) > 0):
                print("Paczki ",taken.intersection(takenNow)," wzięte są dwa razy w ",trace[2])

        taken = taken.union(set(trace[i][2]))



# checkIfTraceIsCorrect([(1,1,[1,2]),(1,1,[2]),(1,1,[1,2]),(1,1,[1,2])])