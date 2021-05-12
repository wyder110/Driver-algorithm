import random

from common.objectiveFunction import *
from confLoader import Configuration


sortingFun = lambda trace : objectiveFunction(Configuration.cities, Configuration.packages, trace)

def ranking_selection(population, count):
    population.sort(key=sortingFun, reverse=True)
    return population[:count]


def tournament_selection(population, count):
    chunk_len = len(population) // count
    last_chunk = chunk_len + len(population) % count
    chunks = [population[x:x+chunk_len] for x in range(0, len(population)-last_chunk, chunk_len)]
    chunks.append(population[-last_chunk:])
    
    result = []
    for ch in chunks:
        ch.sort(key=sortingFun, reverse=True)
        result.append(ch[0])
    return result


def roulette_selection(population, count):
    obj_fun = [objectiveFunction(Configuration.cities, Configuration.packages, trace) for trace in population]
    max = sum(obj_fun)
    result = []
    for i in range(count):
        pick = random.uniform(0, max)
        current = 0
        for j in range(len(population)):
            current += obj_fun[j]
            if current > pick:
                if population[j] not in result:
                    result.append(population[j])
                else:
                    i -= 1
                break
    return result
