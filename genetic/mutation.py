from confLoader import Configuration as Configuration
import random
from copy import copy


def can_be_deleted(trace, index):
    if index < 1 or index > len(trace)-1:
        return False
    elif index == len(trace)-1:
        return True
    else:
        previuos_step = trace[index-1]
        currrent_step = trace[index]
        next_step = trace[index+1]  # (from, to, packages)
        return next_step[0] in list(Configuration.cities.get(previuos_step[0]).keys()) # connection beetwen cities


def deletion(trace: list, index):
    if index < len(trace) - 1:  # delete from middle of trace
        previuos_step = trace[index-1]
        currrent_step = trace[index]
        next_step = trace[index+1]  # (from, to, packages)
        # paczki ogarnąć?
        packages_taken_from_current_city = list(set(currrent_step[2]) - set(previuos_step[2]))
        packages_delivered_to_current_city = list(set(previuos_step[2]) - set(currrent_step[2]))

        # removing "taken" packages until we reach "deleted" city
        revisited_index = len(trace)
        for i in range(index+1, len(trace)):
            step = trace[i]
            if step[0] == currrent_step[0]: # same city
                revisited_index = i
                break
                # remove "taken" packages
            packages = [p for p in step[2] if p not in packages_taken_from_current_city]
            trace[i] = (step[0], step[1], packages)
            
        # remove city to delete and connect its neighbours
        trace[index-1] = (previuos_step[0], next_step[0], previuos_step[2])
        trace.remove(currrent_step)
        # change future xD
        for i in range(index, len(trace)):
            next_and_previous = [x for x in trace[i][2] if x in trace[i-1][2]]
            packages = packages_delivered_to_current_city + next_and_previous
            if i >= revisited_index-1:
                packages = next_and_previous 
            carry = sum([Configuration.packagesId[x]['weigth'] for x in packages])
            for p in [x for x in trace[i][2] if x not in packages]:
                weight = Configuration.packagesId[p]['weigth']
                if weight+carry <= Configuration.parameters['maxCarry']:
                    packages.append(p)
                    carry += weight
            trace[i] = (trace[i][0], trace[i][1], packages)
        
    else:  # delete from the end of trace
        trace.pop()


def check_and_delete(trace, index):
    if can_be_deleted(trace, index):
        deletion(trace, index)
        return True
    
    return False

def can_be_inserted(trace, index):
    if index < 1 or index > len(trace):
        return False
    elif index == len(trace):
        return True
    else:
        prev_step = trace[index-1]
        next_step = trace[index]
        neighbours_prev = list(Configuration.cities.get(prev_step[0]).keys())
        neighbours_next = list(Configuration.cities.get(next_step[0]).keys())
        common_neighbours = [x for x in neighbours_next if x in neighbours_prev]
        return len(common_neighbours) > 0

def insertion(trace, index):
    if index < len(trace): # insert in the middle
        prev_step = trace[index-1]
        next_step = trace[index]
        # find neighbours
        neighbours_prev = list(Configuration.cities.get(prev_step[0]).keys())
        neighbours_next = list(Configuration.cities.get(next_step[0]).keys())
        common_neighbours = [x for x in neighbours_next if x in neighbours_prev]
        # choose one neighbour
        chosen_neighbour = random.choice(common_neighbours)
        # deliver packages
        prev_packages = copy(prev_step[2])
        packages_to_chosen_city = [i for i in prev_packages if chosen_neighbour == Configuration.packagesId[i]['to']]
        # packages that are not delivered yet
        packages = [x for x in prev_packages if x not in packages_to_chosen_city]
        # already used packages
        used_packages = set()
        for i in range(index):
            used_packages.update(trace[i][2]) 
        # packages we can optionally take 
        packages_from_chosen_city = [i for i in range(1, len(Configuration.packagesId)+1) if chosen_neighbour == Configuration.packagesId[i]['from'] and i not in used_packages]
        # try to take those packages
        taken = []
        carry = sum([Configuration.packagesId[x]['weigth'] for x in packages])
        for p in packages_from_chosen_city:
            weight = Configuration.packagesId[p]['weigth']
            if weight+carry <= Configuration.parameters['maxCarry']:
                taken.append(p)
                carry += weight

        # change next city in previous step
        trace[index-1] = (trace[index-1][0], chosen_neighbour, trace[index-1][2])
        # insert new step in trace
        trace.insert(index, (chosen_neighbour, trace[index][0], packages+taken))
        # remove delivered packages from next cities
        for i in range(index+1, len(trace)):
            step = trace[i]
            # remove delivered packages packages
            new_packages = [p for p in step[2] if p not in packages_to_chosen_city and p not in taken]
            trace[i] = (step[0], step[1], new_packages)
        for i in range(index+1, len(trace)):
            previous = trace[i-1]
            current = trace[i]
            previous_and_current = [x for x in previous[2] if x in current[2]] # intersection
            # deliver packages from taken
            if len(taken) > 0:
                packages_to_current_city = [x for x in taken if current[0] == Configuration.packagesId[x]['to']]
                taken = [x for x in taken if x not in packages_to_current_city]
            # try to take packages from old timeline xD
            current_packages = previous_and_current + taken
            current_carry = sum([Configuration.packagesId[x]['weigth'] for x in current_packages])
            for p in [x for x in current[2] if x not in previous[2]]:
                weight = Configuration.packagesId[p]['weigth']
                if weight+current_carry <= Configuration.parameters['maxCarry']:
                    current_packages.append(p)
                    current_carry += weight
            # change future
            trace[i] = (trace[i][0], trace[i][1], current_packages)

    else:
        prev_step = trace[index-1]
        chosen_neighbour = prev_step[1]
        # deliver packages
        prev_packages = copy(prev_step[2])
        packages_to_chosen_city = [i for i in prev_packages if chosen_neighbour == Configuration.packagesId[i]['to']]
        # packages that are not delivered yet
        packages = [x for x in prev_packages if x not in packages_to_chosen_city]
        # change next city in previous step
        trace[index-1] = (trace[index-1][0], chosen_neighbour, trace[index-1][2])
        # choose neighbour for new city
        new_neighbour = random.choice(list(Configuration.cities.get(chosen_neighbour)))
        # insert new step in trace
        trace.insert(index, (chosen_neighbour, new_neighbour, packages))


def check_and_insert(trace, index):
    if can_be_inserted(trace, index):
        insertion(trace, index)
        return True
    
    return False

def insert(trace, index=None):
    if index is None:
        index = random.randint(1, len(trace)-1)
    return check_and_insert(trace, index)

def delete(trace, index=None):
    if index is None:
        index = random.randint(1, len(trace)-1)
    return check_and_delete(trace, index)

def delete_and_insert(trace):
    return delete(trace) and insert(trace)

def replacement(trace, index=None):
    if index is None:
        index = random.randint(1, len(trace)-1)
    return check_and_delete(trace, index) and check_and_insert(trace, index)
