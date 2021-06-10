import random
import warnings
from common.objectiveFunction import *
from config.confLoader import Configuration

def newAnt(startingCity, pheromoneMap, alpha, beta):
    nextCity = nextStep(pheromoneMap, startingCity, [], alpha, beta)
    trailer = takeLeavePackages([], [], startingCity)
    return [(startingCity, nextCity, trailer)]


def nextStep(pheromoneMap, cityFrom, trailer, alpha, beta):
    '''
    it calculates probabilities of going to next cities 
    and then chooses random city according to these probabilities
    '''

    values = dict()
    probabilities = dict()
    
    divisor = 0
    for city in pheromoneMap[cityFrom]:
        tau = pheromoneMap[cityFrom][city]

        new_trailer = leavePackages(trailer, city)
        move = [(cityFrom, city, trailer), (city, city, new_trailer)]
        eta = objectiveFunction(Configuration.cities, Configuration.packages, move)
        
        value = (tau ** alpha).real * (eta ** beta).real
        values[city] = value
        divisor += value

    for city in pheromoneMap[cityFrom]:
        if divisor != 0:
            probabilities[city] = values[city] / divisor
        else:
            probabilities[city] = 1
    
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

