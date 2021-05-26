from functools import reduce

def objectiveFunction(cities, packages, trace):
    profit = 0
    trailer_old = []
    for current_city, next_city, trailer in trace:
        # packages profit
        trailer_diff = [x for x in trailer_old if x not in trailer]
        trailer_old = trailer
        packages_info = getPackagesWithIds(packages, trailer_diff)

        for p in packages_info:
            profit += p["price"]

        # fuel cost
        distance = 0
        if current_city != next_city:
            distance = cities[current_city][next_city]
        profit -= fuel(distance)
    
    return profit


def getPackagesWithIds(packages, ids):
    return list(filter(lambda x : x["id"] in ids, reduce(list.__add__, list(packages.values()))))

def fuel(length):
    return 2 * length