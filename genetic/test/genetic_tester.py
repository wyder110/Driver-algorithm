from copy import copy
import config.confLoader as confLoader
import genetic.crossover as crossover
import genetic.mutation as mutation
from common.objectiveFunction import *
from common.test import *
from genetic.selection import *
from genetic.startPopGen import generateFirstPopulation
import time
import random


def genetic_driver(config_path="config/conf3.json", number_of_tests=100, number_of_iterations=100, population_count=100, selection_type=1, selected_percent=0.2, mutation_type=1, mutation_p=1, cross_p=0):
    print_start_info(config_path, number_of_tests, number_of_iterations, population_count, selection_type, selected_percent, mutation_type, mutation_p, cross_p)

    cities, packages, parameters = confLoader.confLoader(config_path)
    max_sum = sum([x['price'] for x in Configuration.packagesId.values()])

    max_cash = 0
    startTime = time.time()

    for _ in range(number_of_tests):
        # create starting population
        population = generateFirstPopulation(cities, packages, parameters, population_count)
        
        # select, mutate and cross specimens
        for _ in range(number_of_iterations):
            # choose selection type 
            if selection_type == 0: # ranking selection
                population = ranking_selection(population, int(population_count*selected_percent))
            elif selection_type == 1: # tournament selection
                population = tournament_selection(population, int(population_count*selected_percent))
            elif selection_type == 2: # roulette selection
                population = roulette_selection(population, int(population_count*selected_percent))
            else:
                raise Exception("Selection type number not defined")

            for i in range(len(population)):
                trace_copy = copy(population[i])
                # check if mutation takes place
                if random.uniform(0, 1) <= mutation_p:
                    # choose mutation type
                    if mutation_type == 0: # random delete and random insert
                        mutation.delete_and_insert(trace_copy)
                    elif mutation_type == 1: # random delete and insert - replacement
                        mutation.replacement(trace_copy)
                
                population.append(trace_copy)

                # optimization - crossing only half of population
                for j in range(i):
                    # check if cross takes place
                    if random.uniform(0, 1) <= cross_p:
                        cross = crossover.crossover(cities, population[i], population[j])
                        population.append(cross)

        # sort by objective function
        population.sort(key=sortingFun, reverse=True)

        # set new max sum 
        current_cash = sortingFun(population[0])
        if current_cash > max_cash:
            max_cash = current_cash

    stoptime = time.time()
    elapsed_time = stoptime - startTime

    print_end_info(max_sum, max_cash, elapsed_time)
    
    return max_sum, max_cash, elapsed_time

def print_end_info(max_sum, max_cash, elapsed_time):
    print("test ended with results: ")
    print("\t max_sum:", max_sum)
    print("\t max_cash:", max_cash)
    print("\t elapsed_time:", elapsed_time)
    print("- - - - - - - - - - - -")

def print_start_info(config_path, number_of_tests, number_of_iterations, population_count, selection_type, selected_percent, mutation_type, mutation_p, cross_p):
    print("starting test with parameters: ")
    print("\t config_path:", config_path)
    print("\t number_of_tests:", number_of_tests)
    print("\t number_of_iterations:", number_of_iterations)
    print("\t population_count:", population_count)
    print("\t selection_type:", selection_type)
    print("\t selected_percent:", selected_percent)
    print("\t mutation_type:", mutation_type)
    print("\t mutation_p:", mutation_p)
    print("\t cross_p:", cross_p)

