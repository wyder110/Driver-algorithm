from confLoader import Configuration as Configuration

# where, cities?
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
        
        for i in range(index+1, len(trace)):
            step = trace[i]
            if step[0] != currrent_step[0]: # different city
                # remove "taken" packages
                packages = [p for p in step[2] if p not in packages_taken_from_current_city]
                trace[i] = (step[0], step[1], packages)
            else:
                break

        # calculating free space in trailer
        minimal_space_left = Configuration.parameters['maxCarry']
        for i in range(index+1, len(trace)):
            step = trace[i]
            if step[0] != currrent_step[0]: # different city
                weight = sum([Configuration.packagesId[p_id]['weigth'] for p_id in step[2]]) 
                space_left = Configuration.parameters['maxCarry'] - weight
                if space_left < minimal_space_left:
                    minimal_space_left = space_left
        
        packages_to_add = []
        for p in packages_delivered_to_current_city:
            weight = Configuration.packagesId[p]['weigth']
            if weight <= minimal_space_left:
                minimal_space_left -= weight
                packages_to_add.append(p)

        if len(packages_to_add) > 0:
            # adding "delivered" packages until we reach "deleted" city
            for i in range(index+1, len(trace)):
                step = trace[i]
                if step[0] != currrent_step[0]: # different city
                    # add "delivered" packages
                    packages = step[2] + packages_to_add
                    trace[i] = (step[0], step[1], packages)
                else:
                    break
        trace[index-1] = (previuos_step[0], next_step[0], previuos_step[2])
        trace.remove(currrent_step)
    else:  # delete from the end of trace
        trace.pop()


def check_and_delete():
    # TODO
    pass

def insertion():
    # TODO
    pass


def insertion_and_deletion():
    # TODO
    pass


def replacement():
    # TODO
    pass  # the ball
