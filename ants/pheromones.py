from common.objectiveFunction import *
from config.confLoader import *


def createPheromonesMap(cities):
    pheromones = {}
    for city in cities:
        pheromones[city] = {}
        for connection in cities[city]:
            pheromones[city][connection] = 1

    return pheromones


def updatePheromoneMap(pheromones, ants, ro):
    # evaporating
    for i in pheromones:
        for j in pheromones[i]:
            pheromones[i][j] *= (1 - ro)
    
    for ant in ants:
        if len(ant) < Configuration.parameters["maxSteps"]:
            lastMove = ant[len(ant)-2:len(ant)]
            obj = objectiveFunction(Configuration.cities, Configuration.packages, lastMove)
            # obj = objectiveFunction(Configuration.cities, Configuration.packages, ant)
            if obj > 0:
                cityFrom = ant[-1][0]
                cityTo = ant[-1][1]
                pheromones[cityFrom][cityTo] += obj
                # pheromones[cityTo][cityFrom] += obj


def printPheromones(pheromones):
    for i in pheromones:
        print((i + ": ").ljust(12), end="")
        keys = list(pheromones[i].keys())
        values = list(pheromones[i].values())
        for i in range(len(pheromones[i])):
            print((keys[i] + ": {:.3f} ".format(values[i])).ljust(23), end="")
        print()
    print()
