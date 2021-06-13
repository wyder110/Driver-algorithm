import random
import time
from copy import copy

import config.conf_loader as confLoader
import genetic.crossover as crossover
import genetic.mutation as mutation
from common.objective_function import *
from common.test import *
from genetic.selection import *
from genetic.start_pop_gen import generateFirstPopulation

cities, packages, parameters = confLoader.confLoader("config/conf3.json")

population_count = 100
number_of_tests = 1
number_of_iterations = 100
selection_type = 0 # 0 - ranking, 1 - tournament, 2 - roulette
selected_percent = 0.2
mutation_type = 1 # 0 - random delete and insert, 1 - replacement
mutation_p = 1
cross_p = 0 

max_sum = sum([x['price'] for x in Configuration.packagesId.values()])

best_pop = []
max_cash = 0
start = time.time()
bad_removal_count = bad_packages_count = bad_trace_count = bad_sum_count = 0

for number_test in range(number_of_tests):
    pop = generateFirstPopulation(cities, packages, parameters, population_count)
    
    for _ in range(number_of_iterations):
        # choose selection type 
        if selection_type == 0: # ranking selection
            pop = ranking_selection(pop, int(population_count*selected_percent))
        elif selection_type == 1: # tournament selection
            pop = tournament_selection(pop, int(population_count*selected_percent))
        elif selection_type == 2: # roulette selection
            pop = roulette_selection(pop, int(population_count*selected_percent))
        else:
            raise Exception("Selection type number not defined")

        
        for i in range(len(pop)):
            trace_copy = copy(pop[i])
            # check if mutation takes place
            if random.uniform(0, 1) <= mutation_p:
                # choose mutation type
                if mutation_type == 0: # random delete and random insert
                    mutation.delete_and_insert(trace_copy)
                elif mutation_type == 1: # random delete and insert - replacement
                    mutation.replacement(trace_copy)
            
            pop.append(trace_copy)

            # optimization - crossing only half of population
            for j in range(i):
                # check if cross takes place
                if random.uniform(0, 1) <= cross_p:
                    cross = crossover.crossover(cities, pop[i], pop[j])
                    pop.append(cross)

    pop.sort(key=sortingFun, reverse=True)
    current_cash = sortingFun(pop[0])
    if current_cash > max_cash:
        max_cash = current_cash
        best_pop = pop[0]

stoptime = time.time()

print("BEST TRACE")
for p in best_pop:
    print(p)
print()
print("obj function:",  max_cash)

fuel_cost = 0
for current_city, next_city, trailer in best_pop:
    distance = cities[current_city][next_city]
    fuel_cost += fuel(distance)

print()
print("elapsed time:", stoptime - start)
print("max revenue:", max_sum)
print("obj function:", max_cash)
print("fuel cost:", fuel_cost)
# print("difference", max_sum - (max_cash + cost))
