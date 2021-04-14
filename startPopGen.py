import random


def generateFirstPopulation(cities, packages, parameters):
    startCity = parameters.get("start")
    maxSteps = parameters.get("maxSteps")
    maxCarry = parameters.get("maxCarry")

    
    currentCity = startCity
    trailer = []

    trace = []
    for i in range(maxSteps):
        # oddaj paczki chamie
        deliverPackages(trailer, currentCity)
        # wybierz paczke/i
        packagesInCurrentCity = list(packages.get(currentCity))
        choosePackages(trailer, packagesInCurrentCity, maxCarry)
        # wybierz sasiada
        adjacentCities = list(cities.get(currentCity).keys())
        nextCity = chooseNeighbour(adjacentCities)
        # dodaj wpis w trasie
        packagesNumber = [x["id"] for x in trailer]
        trace.append((currentCity, nextCity, packagesNumber))
        # zmien obecne miasto
        currentCity = nextCity
    for t in trace:
        print(t)


def deliverPackages(trailer, currentCity):
    for package in trailer:
        if package["to"] == currentCity:
            trailer.remove(package)


def choosePackages(trailer, packagesToTake, maxCarry):
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
