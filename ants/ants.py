import random
from copy import copy
from confLoader import Configuration

def nextStep(pheromoneMap, cityFrom, alpha):
    # TODO add eta and beta
    probabilities = dict()

    divisor = 0
    for city in pheromoneMap[cityFrom]:
        divisor += (pheromoneMap[cityFrom][city] ** alpha).real

    
    for city in pheromoneMap[cityFrom]:
        if divisor != 0:
            probabilities[city] = (pheromoneMap[cityFrom][city] ** alpha).real / divisor
        else:
            probabilities[city] = 1
    
    # print("cities", list(pheromoneMap[cityFrom]))
    # print("probs", list(probabilities.values()))
    return random.choices(list(pheromoneMap[cityFrom]), weights=list(probabilities.values()))[0]

    # allPheromones = []
    # for trace in pheromoneMap[cityFrom]:
    #     allPheromones.append(pheromoneMap[cityFrom][trace])

    # return random.choices(list(pheromoneMap[cityFrom]), weights=allPheromones)[0]


def takeLeavePackages(ant):
    
    packagesAlreadyTaken = set()
    for _,_,packages in ant:
        packagesAlreadyTaken = packagesAlreadyTaken.union(set(packages))

    # print("ant", ant)
    # print("packagesAlreadyTaken", packagesAlreadyTaken)
    currentCity = ant[-1][1]
    packages = Configuration.packages[currentCity]

    newPackages = leavePackages(ant[-1][2], currentCity)
    

    for package in packages:
        if package['id'] not in packagesAlreadyTaken:
            if canAntTakePackage(ant, package['id']):
                newPackages.append(package['id'])

    return newPackages
    
    
def leavePackages(packages, currentCity):
    newPackages = []
    for packageId in packages:
        package = Configuration.packagesId[packageId]
        if package['to'] != currentCity:
            newPackages.append(packageId)
    return newPackages


def canAntTakePackage(ant, packageToTake):
    currentPackages = ant[-1][2]
    currentWeigth = 0
    for packageId in currentPackages:
        currentWeigth += Configuration.packagesId[packageId]["weigth"]

    currentWeigth += Configuration.packagesId[packageToTake]["weigth"]

    return currentWeigth <= Configuration.parameters["maxCarry"]

