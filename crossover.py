import random
from copy import copy
from confLoader import Configuration as Configuration

def copyFirstPart(listFrom, cross, crossingPlace, takenPackeges):
    '''kopiuje pierwszą część treca'''
    for j in range(crossingPlace): #kopiuje pierwszą część crossa
        tup = (listFrom[j][0], listFrom[j][1], copy(listFrom[j][2]))
        cross.append(tup)
        for pac in listFrom[j][2]: takenPackeges.add(pac)

def deliverAndCopyPackages(cross, newTrailer):
    '''kopiuje paczki z poprzedniego traca i wyrzuca paczki które dotarły do lokalizacji'''
    currentCarry = 0
    for idOfPack in cross[len(cross)-1][2]:
        if not Configuration.packagesId[idOfPack]['to'] == cross[len(cross)-1][1]:
            newTrailer.append(Configuration.packagesId[idOfPack]['id'])
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
        currentCarry = deliverAndCopyPackages(cross, newTrailer)
        takenTo = list(set(listTo[j][2]) - set(listTo[j-1][2]))
        takeNewPackages(listTo, newTrailer, takenPackeges, takenTo, currentCarry, Configuration.parameters)
        tup = (listTo[j][0], listTo[j][1], newTrailer)
        cross.append(tup)


def crossover(cities, l1, l2):
    randomList = list(range(1, len(l1)-1))
    random.shuffle(randomList)

    for i in randomList:
        rand = random.randint(0, 1) == 1
        listFrom = l1 if rand else l2
        listTo = l2 if rand else l1

        taken = set()

        if listTo[i][1] in cities[listFrom[i][0]]: #można w tym miejscu przeciąć trace
            cross = []

            copyFirstPart(listFrom, cross, i, taken)
            cross.append((listFrom[i][0], listTo[i][1], copy(listFrom[i][2]))) #punkt przecięcia pierwszej części z drugą częścią
            copySecondPart(listTo, cross, i, taken)

            return cross
            

