import time

import ants.pheromones as pheromones
from ants.ants import *
from ants.pheromones import printPheromones
from common.objective_function import *
from common.test import runAllTraceTest
from config.conf_loader import *

cities, packages, parameters = confLoader("config/conf3.json")
startingCity = Configuration.parameters["start"]
max_sum = sum([x['price'] for x in Configuration.packagesId.values()])

pheromoneMap = pheromones.createPheromonesMap(cities)
ants = []

alpha = 0.8
beta = 0.5
ro = 0.01

starting_population = 10
iterations = 100

start = time.time()

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

stoptime = time.time()

sortingFun = lambda trace : objectiveFunction(Configuration.cities, Configuration.packages, trace)
ants.sort(key=sortingFun, reverse=True)
best_ant = ants[0]
max_cash = sortingFun(best_ant)

print("BEST TRACE")
for p in best_ant:
    print(p)
print()
print("obj function:", max_cash)

fuel_cost = 0
for current_city, next_city, trailer in best_ant:
    distance = cities[current_city][next_city]
    fuel_cost += fuel(distance)

print()
print("elapsed time:", stoptime - start)
print("trace len:", len(best_ant))
print("max revenue:", max_sum)
print("obj function:", max_cash)
print("fuel cost:", fuel_cost)
    