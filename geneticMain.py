import confLoader
from genetic.startPopGen import generateFirstPopulation
from genetic.objectiveFunction import objectiveFunction
import genetic.crossover as crossover
import genetic.mutation as mutation
from copy import copy
from genetic.objectiveFunction import *
from genetic.selection import *

cities, packages, parameters = confLoader.confLoader("config/conf3.json")


best_pop = []
max_cash = 0
for _ in range(10):
    pop = generateFirstPopulation(cities, packages, parameters, 100)
    for _ in range(100):
        pop = ranking_selection(pop, 20)
        for i in range(len(pop)):
            trace_copy = copy(pop[i])
            mutation.replacement(trace_copy)
            pop.append(trace_copy)
            for j in range(i):
                cross = crossover.crossover(cities, pop[i], pop[j])
                pop.append(cross)
                pop.append(generateFirstPopulation(cities, packages, parameters, 1)[0])

    pop.sort(key=sortingFun, reverse=True)
    current_cash = sortingFun(pop[0])
    print(sortingFun(pop[0]))
    if current_cash > max_cash:
        max_cash = current_cash
        best_pop = pop[0]

for p in best_pop:
    print(p)

cost = 0
for current_city, next_city, trailer in best_pop:
    distance = cities[current_city][next_city]
    cost += 2*distance

max_sum = sum([x['price'] for x in Configuration.packagesId.values()])
print("max sum ",  max_sum)
print("best sum ", max_cash)
print("fuel cost ", cost)
print("difference", max_sum-(max_cash+cost))
