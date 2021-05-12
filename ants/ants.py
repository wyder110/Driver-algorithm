import random
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


def antTakeLeavePackages(ant):
    currentCity = ant[-1][1]
    trailer = ant[-1][2]

    taken = set()
    for _, _, packages in ant:
        taken = taken.union(set(packages))
    
    return takeLeavePackages(trailer, taken, currentCity)
    

def takeLeavePackages(trailer, taken, currentCity):
    packages = Configuration.packages[currentCity]

    newPackages = leavePackages(trailer, currentCity)
    
    for package in packages:
        if package['id'] not in taken:
            if canTakePackage(trailer, package['id']):
                newPackages.append(package['id'])

    return newPackages
    
def leavePackages(packages, currentCity):
    newPackages = []
    for packageId in packages:
        package = Configuration.packagesId[packageId]
        if package['to'] != currentCity:
            newPackages.append(packageId)
    return newPackages


def canTakePackage(trailer, packageToTake):
    currentWeigth = 0
    for packageId in trailer:
        currentWeigth += Configuration.packagesId[packageId]["weigth"]

    currentWeigth += Configuration.packagesId[packageToTake]["weigth"]

    return currentWeigth <= Configuration.parameters["maxCarry"]

