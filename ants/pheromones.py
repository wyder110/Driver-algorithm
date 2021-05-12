from ants.objectiveFunction import *
from confLoader import *

def createPheromonesMap(cities):
    pheromones = {}
    for city in cities:
        pheromones[city] = {}
        for connection in cities[city]:
            pheromones[city][connection] = 1

    return pheromones

def pheromonesEvaporating(pheromones, ro):
    for city in pheromones:
        for connection in pheromones[city]:
            pheromones[city][connection] *= (1 - ro)

def updatePheromoneMap(pheromones, ants, ro):
    Q = 1
    L = 1

    # evaporating
    for i in pheromones:
        for j in pheromones[i]:
            pheromones[i][j] *= (1 - ro)
    
    for ant in ants:
        if len(ant) < Configuration.parameters["maxSteps"]:
            cityFrom = ant[-1][0]
            cityTo = ant[-1][1]
            obj = objectiveFunction(Configuration.cities, Configuration.packages, ant)
            if obj > 0: 
                pheromones[cityTo][cityFrom] += obj
                pheromones[cityFrom][cityTo] += obj

    # for i in pheromones:
    #     for j in pheromones[i]:
    #         # evaporating
    #         pheromones[i][j] *= (1 - ro)
    #         # delta sum
    #         for k in ants:
    #             if len(k) < Configuration.parameters["maxSteps"]:
    #                 if (k[-1][0] == i and k[-1][1] == j) or (k[-1][1] == i and k[-1][0] == j):
    #                     obj = objectiveFunction(cities, packages, k)
    #                     pheromones[i][j] += obj
                
