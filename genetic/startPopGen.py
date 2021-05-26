import random


def generateFirstPopulation(cities, packages, parameters, count):
    startCity = parameters.get("start")
    maxSteps = parameters.get("maxSteps")
    maxCarry = parameters.get("maxCarry")

    result = []
    for _ in range(count):
        result.append(generateTrace(cities, packages, parameters, startCity, maxSteps, maxCarry))
    
    return result


def generateTrace(cities, packages, parameters, startCity, maxSteps, maxCarry):
    currentCity = startCity
    trailer = []
    taken = set()

    trace = []
    for _ in range(maxSteps):
        
        trailer = deliverPackages(trailer, currentCity)

        if currentCity in packages:
            freePackages = [x for x in list(packages.get(currentCity)) if x["id"] not in taken]
            choosePackages(trailer, freePackages, maxCarry, currentCity)

        adjacentCities = list(cities.get(currentCity).keys())
        nextCity = chooseNeighbour(adjacentCities)

        packagesNumber = [x["id"] for x in trailer]
        taken.update(packagesNumber)
        trace.append((currentCity, nextCity, packagesNumber))

        currentCity = nextCity
    
    return trace

def deliverPackages(trailer, currentCity):
    newTrailer = []
    for package in trailer:
        if package["to"] != currentCity:
            newTrailer.append(package)
    return newTrailer


def choosePackages(trailer, packagesToTake, maxCarry, currentCity):
    currentCarry = sum([x["weigth"] for x in trailer])
    while len(packagesToTake) > 0:
        package = random.choice(packagesToTake)
        if package["weigth"] + currentCarry > maxCarry:
            break
        
        packagesToTake.remove(package)
        trailer.append(package)
        currentCarry += package["weigth"]


def chooseNeighbour(neighbours):
    return random.choice(neighbours)
