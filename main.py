import confLoader
from startPopGen import generateFirstPopulation
from objectiveFunction import objectiveFunction

cities, packages, parameters = confLoader.confLoader("config/conf3.json")
pop = generateFirstPopulation(cities, packages, parameters, 10)


for t in pop:
    print("Trace")
    for e in t:
        print(e)
    profit = objectiveFunction(cities, packages, t)
    print("profit:", profit)
    print()



