import ants.pheromones as pheromones
from ants.ants import *
from ants.pheromones import printPheromones
from common.objectiveFunction import *
from confLoader import *

cities, packages, parameters = confLoader("config/conf3.json")
startingCity = Configuration.parameters["start"]

pheromoneMap = pheromones.createPheromonesMap(cities)
ants = []

alpha = 0.8
beta = 0
ro = 0.01

starting_population = 1000
iterations = 100

for _ in range(starting_population):
    ants.append([(startingCity, nextStep(pheromoneMap, startingCity, alpha), takeLeavePackages([],[],startingCity))])

for _ in range(iterations):
    ants.append([(startingCity, nextStep(pheromoneMap, startingCity, alpha), takeLeavePackages([],[],startingCity))])

    printPheromones(pheromoneMap)

    for ant in ants:
        if len(ant) < Configuration.parameters["maxSteps"]:
            cityFrom = ant[-1][1]
            nextCity = nextStep(pheromoneMap, cityFrom, alpha)
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

    