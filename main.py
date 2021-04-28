import confLoader
from startPopGen import generateFirstPopulation
from objectiveFunction import objectiveFunction
import crossoverMutation

cities, packages, parameters = confLoader.confLoader("config/conf3.json")



pop = generateFirstPopulation(cities, packages, parameters, 100)
sortingFun = lambda trace : objectiveFunction(cities, packages, trace)

packagesId = dict()
for city in packages.items():
    for pac in city[1]:
        packagesId[pac["id"]] = pac

# cross = crossoverMutation.crossover(cities, packagesId, parameters, pop[0], pop[1])

for _ in range(100):
    pop.sort(key = sortingFun, reverse=True)
    pop = pop[:20]
    for i in range(len(pop)):
        for j in range(i):
            cross = crossoverMutation.crossover(cities, packagesId, parameters, pop[i], pop[j])
            pop.append(cross)
            # pop.append(generateFirstPopulation(cities, packages, parameters, 1)[0])

    




print(sortingFun(pop[0]))



# for t in pop:
#     print("Trace")
#     for e in t:
#         print(e)
#     profit = objectiveFunction(cities, packages, t)
#     print("profit:", profit)
#     print()

