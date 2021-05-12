from confLoader import *
import ants.pheromones as pheromones
from ants.ants import *
from copy import deepcopy
from ants.objectiveFunction import *
from genetic.crossover import chceckIfTraceIsCorrect

# confLoader.Configuration.parameters
cities, packages, parameters = confLoader("config/conf3.json")
startingCity = Configuration.parameters["start"]


pheromoneMap = pheromones.createPheromonesMap(cities)
ants = []

alpha = 1
beta = 0
ro = 0.5

starting_population = 1
iterations = 1000

for _ in range(starting_population):
    ants.append([(startingCity, nextStep(pheromoneMap, startingCity, alpha), [])])
    ants[-1][0] = (startingCity, nextStep(pheromoneMap, startingCity, alpha), takeLeavePackages(ants[-1]))

for _ in range(iterations):
    ants.append([(startingCity, nextStep(pheromoneMap, startingCity, alpha), [])])
    ants[-1][0] = (startingCity, nextStep(pheromoneMap, startingCity, alpha), takeLeavePackages(ants[-1]))

    for ant in ants:
        if len(ant) < Configuration.parameters["maxSteps"]:
            cityFrom = ant[-1][1]
            nextCity = nextStep(pheromoneMap, cityFrom, alpha)
            newPackages = takeLeavePackages(ant)
            ant.append((cityFrom, nextCity, newPackages))
        
    pheromones.updatePheromoneMap(pheromoneMap, ants, ro)


sortingFun = lambda trace : objectiveFunction(Configuration.cities, Configuration.packages, trace)
ants.sort(key=sortingFun, reverse=True)
print("BEST")
print(ants[0])
print(sortingFun(ants[0]))

    