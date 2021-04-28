import random
from copy import copy

def crossover(cities, packagesId, parameters, l1, l2):
    randomList = list(range(1, len(l1)-1))
    random.shuffle(randomList)

    for i in randomList:
        rand = random.randint(0, 1) == 1
        listFrom = l1 if rand else l2
        listTo = l2 if rand else l1

        taken = set()

        if listTo[i][1] in cities[listFrom[i][0]]:
            cross = []
            for j in range(i): #kopiuje pierwszą część crossa
                tup = (listFrom[j][0], listFrom[j][1], copy(listFrom[j][2]))
                cross.append(tup)
                for pac in listFrom[j][2]: taken.add(pac) 

                           
            cross.append((listFrom[i][0], listTo[i][1], copy(listFrom[i][2]))) #punkt przecięcia pierwszej części z drugą częścią

            for j in range(i+1, len(l1)):
                newTrailer = []
                currentCarry = 0
                for idOfPack in cross[len(cross)-1][2]:
                    if not packagesId[idOfPack]['to'] == cross[len(cross)-1][1]:
                        newTrailer.append(packagesId[idOfPack]['id'])
                        currentCarry += packagesId[idOfPack]['weigth'] #wypierdalamy paczki które dotarły do lokalizacji

                takenTo = list(set(listTo[j][2]) - set(listTo[j-1][2]))
                for pac in takenTo:
                    if pac not in taken:
                        if currentCarry + packagesId[pac]['weigth'] <= parameters["maxCarry"]:
                            taken.add(pac)
                            newTrailer.append(pac)
                            currentCarry += packagesId[pac]['weigth']
                        

                
                tup = (listTo[j][0], listTo[j][1], newTrailer)
                cross.append(tup)

            return cross
            