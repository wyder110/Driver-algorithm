
def checkIfTraceIsCorrect(trace):
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