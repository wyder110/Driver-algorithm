import confLoader
from startPopGen import generateFirstPopulation
from objectiveFunction import objectiveFunction
import crossover
from mutation import *

cities, packages, parameters = confLoader.confLoader("config/conf3.json")



pop = generateFirstPopulation(cities, packages, parameters, 100)
sortingFun = lambda trace : objectiveFunction(cities, packages, trace)

for p in pop[0]:
    print(p)
print()
for i in range(4, len(pop[0])):
    if can_be_deleted(pop[0], i):
        print("deleted ", i)
        deletion(pop[0], i)
        break
for p in pop[0]:
    print(p)

# cross = crossover.crossover(cities, packagesId, parameters, pop[0], pop[1])

# # ranking selection :O
# for _ in range(100):
#     pop.sort(key = sortingFun, reverse=True)
#     pop = pop[:20]
#     for i in range(len(pop)):
#         for j in range(i):
#             cross = crossover.crossover(cities, pop[i], pop[j])
#             pop.append(cross)
#             # pop.append(generateFirstPopulation(cities, packages, parameters, 1)[0])

    




print(sortingFun(pop[0]))



# for t in pop:
#     print("Trace")
#     for e in t:
#         print(e)
#     profit = objectiveFunction(cities, packages, t)
#     print("profit:", profit)
#     print()

