from functools import reduce
from confLoader import Configuration as Configuration
from common.objectiveFunction import *

def checkTakenPackages(trace):
    taken = set()
    for i in range(1, len(trace)):
        takenInThisTurn = set(trace[i][2]) - set(trace[i-1][2])
        for package in takenInThisTurn:
            if package in taken:
                print("BŁĄD NUMER PACZKI: ",package," W TRACE: ", trace, "\n")
                return False
            taken.add(package)
    return True

def checkCitiesTrace(trace):
    for i in range(1, len(trace)):
        previous_step = trace[i-1]
        current_step = trace[i]
        if previous_step[1] != current_step[0]:
            return False
    return True

def printObjFuncStepByStep(cities, packages, trace, max_sum):
    profit = 0
    total_fuel_cost = 0
    trailer_old = []
    for current_city, next_city, trailer in trace:
        # packages profit
        trailer_diff = [x for x in trailer_old if x not in trailer]
        should_remove_in_current_city = [x for x in trailer_old if Configuration.packagesId[x]['to'] == current_city]
        trailer_old = trailer
        packages_info = getPackagesWithIds(packages, trailer_diff)
        print(current_city,"->",next_city, "\n\t trailer:", trailer)
        print("\t current profit:", profit)
        print("\t removed:", trailer_diff, "\n\t should remove:", should_remove_in_current_city)
        if set(should_remove_in_current_city) != set(trailer_diff):
            print("BAD REMOVAL")

        for p in packages_info:
            profit += p["price"]
            print("\t package: ", p["id"], " price: ", p["price"])
        print("\t after delivery profit:", profit)
        # fuel cost
        distance = cities[current_city][next_city]
        fuel_cost = fuel(distance)
        print("\t fuel cost:", fuel_cost)
        profit -= fuel_cost
        total_fuel_cost += fuel_cost
        print("\t after fuel profit:", profit)
        print("\t total fuel cost:", total_fuel_cost)
        print("\t free profit:", profit+total_fuel_cost)
        print("\t max free profit - free profit:", max_sum - (profit+total_fuel_cost))
    
    return profit


def checkBadRemoval(trace):
    trailer_old = []
    for current_city, _, trailer in trace:
        trailer_diff = [x for x in trailer_old if x not in trailer]
        should_remove_in_current_city = [x for x in trailer_old if Configuration.packagesId[x]['to'] == current_city]
        trailer_old = trailer
        if set(should_remove_in_current_city) != set(trailer_diff):
            print("should_remove_in_current_city ",should_remove_in_current_city,"trailer_diff",trailer_diff)
            return True
    
    return False

def runAllTraceTest(trace):
    if checkBadRemoval(trace):
        print("checkBadRemoval ", trace)
        print("checkBadRemoval ", trace)

    if not checkCitiesTrace(trace):
        print("checkCitiesTrace ", trace)
        print("checkCitiesTrace ", trace)

    if not checkTakenPackages(trace):
        print("checkTakenPackages ", trace)
        print("checkTakenPackages ", trace)