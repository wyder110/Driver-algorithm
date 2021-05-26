import ants.pheromones as pheromones
from ants.ants import *
from ants.pheromones import printPheromones
from common.objectiveFunction import *
from confLoader import *
from common.test import runAllTraceTest 

cities, packages, parameters = confLoader("config/conf3.json")
startingCity = Configuration.parameters["start"]

pheromoneMap = pheromones.createPheromonesMap(cities)
ants = []

alpha = 0.8
beta = 0.5
ro = 0.01

starting_population = 10
iterations = 100

for _ in range(starting_population):
    ants.append(newAnt(startingCity, pheromoneMap, alpha, beta))

for _ in range(iterations):
    ants.append(newAnt(startingCity, pheromoneMap, alpha, beta))

    # printPheromones(pheromoneMap)

    for ant in ants:
        runAllTraceTest(ant)
        if len(ant) < Configuration.parameters["maxSteps"]:
            cityFrom = ant[-1][1]
            trailer = ant[-1][2]
            nextCity = nextStep(pheromoneMap, cityFrom, trailer, alpha, beta)
            newPackages = antTakeLeavePackages(ant)
            ant.append((cityFrom, nextCity, newPackages))
        
    pheromones.updatePheromoneMap(pheromoneMap, ants, ro)


sortingFun = lambda trace : objectiveFunction(Configuration.cities, Configuration.packages, trace)
ants.sort(key=sortingFun, reverse=True)
print("BEST")
for p in ants[0]:
    print(p)
print("len:", len(ants[0]))
print(sortingFun(ants[0]))

    