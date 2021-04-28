# top kek

# where, cities?
def can_be_deleted(trace, index, connections):
    # TODO
    # if first then no
    pass
# where, cities?


def deletion(trace: list, index):
    if index < len(trace) - 1:  # delete from middle of trace
        previuos_step = trace[index-1]
        currrent_step = trace[index]
        next_step = trace[index+1]  # (from, to, packages)
        # paczki ogarnąć?
        packages_taken_from_current_city = list(set(currrent_step[2]) - set(previuos_step[2]))
        packages_delivered_to_current_city = list(set(previuos_step[2]) - set(currrent_step[2]))

        # removing "taken" packages until we reach "deleted" city
        for i in range(index, len(trace)):
            step = trace[i]
            if step[0] != currrent_step[0]: # different city
                # remove "taken" packages
                step[2] = [p for p in step[2] if p not in packages_taken_from_current_city]
            else:
                break
        minimal_space_left = 0
        # TODO
    else:  # delete from the end of trace
        trace.pop()
    pass


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
