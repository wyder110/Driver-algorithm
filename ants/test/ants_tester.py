
import time
import ants.pheromones as pheromones
from ants.ants import *
from ants.pheromones import printPheromones
from common.objectiveFunction import *
from config.confLoader import *


def sortingFun(trace): return objectiveFunction(Configuration.cities, Configuration.packages, trace)

def ants_driver(config_path="config/conf3.json", number_of_tests=100, number_of_iterations=100, starting_population=10, alpha=0.8, beta=0.5, ro=0.01):
    print_start_info(config_path, number_of_tests, number_of_iterations, starting_population, alpha, beta, ro)

    cities, _, _ = confLoader(config_path)

    max_sum = sum([x['price'] for x in Configuration.packagesId.values()])
    max_steps = Configuration.parameters["maxSteps"]
    startingCity = Configuration.parameters["start"]

    max_cash = 0
    trace_len = 0

    startTime = time.time()

    for _ in range(number_of_tests):
        pheromoneMap = pheromones.createPheromonesMap(cities)
        ants = []

        for _ in range(starting_population):
            ants.append(newAnt(startingCity, pheromoneMap, alpha, beta))

        for _ in range(number_of_iterations):
            ants.append(newAnt(startingCity, pheromoneMap, alpha, beta))

            for ant in ants:
                if len(ant) < max_steps:
                    cityFrom = ant[-1][1]
                    trailer = ant[-1][2]
                    nextCity = nextStep(pheromoneMap, cityFrom, trailer, alpha, beta)
                    newPackages = antTakeLeavePackages(ant)
                    ant.append((cityFrom, nextCity, newPackages))

            pheromones.updatePheromoneMap(pheromoneMap, ants, ro)

        ants.sort(key=sortingFun, reverse=True)
        best_ants = ants[0]
        current_best_cash = sortingFun(best_ants)
        if current_best_cash > max_cash:
            max_cash = current_best_cash
            trace_len = len(best_ants)

    stoptime = time.time()
    elapsed_time = stoptime - startTime

    print_end_info(max_sum, max_cash, elapsed_time, trace_len)

    return max_sum, max_cash, elapsed_time, trace_len


def print_end_info(max_sum, max_cash, elapsed_time, trace_len):
    print("test ended with results: ")
    print("\t max_sum:", max_sum)
    print("\t max_cash:", max_cash)
    print("\t elapsed_time:", elapsed_time)
    print("\t trace_len:", trace_len)
    print("- - - - - - - - - - - -")


def print_start_info(config_path, number_of_tests, number_of_iterations, starting_population, alpha, beta, ro):
    print("starting test with parameters: ")
    print("\t config_path:", config_path)
    print("\t number_of_tests:", number_of_tests)
    print("\t number_of_iterations:", number_of_iterations)
    print("\t starting_population:", starting_population)
    print("\t alpha:", alpha)
    print("\t beta:", beta)
    print("\t ro:", ro)
