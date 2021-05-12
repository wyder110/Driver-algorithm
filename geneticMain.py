from copy import copy

import confLoader
import genetic.crossover as crossover
import genetic.mutation as mutation
from common.objectiveFunction import *
from genetic.selection import *
from genetic.startPopGen import generateFirstPopulation

cities, packages, parameters = confLoader.confLoader("config/conf.json")

population_count = 100
number_of_tests = 1000
number_of_iterations = 1000
selection_type = 0 # 0 - ranking, 1 - tournament, 2 - roulette
selected_percent = 0.2

max_sum = sum([x['price'] for x in Configuration.packagesId.values()])

best_pop = []
max_cash = 0
for _ in range(number_of_tests):
    pop = generateFirstPopulation(cities, packages, parameters, population_count)
    for _ in range(number_of_iterations):
        pop = ranking_selection(pop, int(population_count*selected_percent))
        for i in range(len(pop)):
            trace_copy = copy(pop[i])
            mutation.replacement(trace_copy)
            pop.append(trace_copy)
            # for j in range(i):
                # cross = crossover.crossover(cities, pop[i], pop[j])
                # pop.append(cross)
                # pop.append(generateFirstPopulation(cities, packages, parameters, 1)[0])

    pop.sort(key=sortingFun, reverse=True)
    current_cash = sortingFun(pop[0])
    # for p in pop[0]:
    #     print(p)
    # print(current_cash)
    cost = 0
    for current_city, next_city, trailer in best_pop:
        distance = cities[current_city][next_city]
        cost += 2*distance
    if max_sum-(current_cash+cost) < 0:
        for p in pop[0]:
            print(p)
        print(current_cash)
        print("difference", max_sum-(current_cash+cost))
    if current_cash > max_cash:
        max_cash = current_cash
        best_pop = pop[0]

for p in best_pop:
    print(p)

cost = 0
for current_city, next_city, trailer in best_pop:
    distance = cities[current_city][next_city]
    cost += 2*distance

print("max sum ",  max_sum)
print("best sum ", max_cash)
print("fuel cost ", cost)
print("difference", max_sum-(max_cash+cost))
