# 1 = collude
# 0 = defect

def play(opponentMove):
    if opponentMove == 'start':
        return 1
    opponentHistory = []
    opponentHistory.append(opponentMove)
    average = sum(opponentHistory) / len(opponentHistory)
    if average > 0.7:
        return 1
    else:
        return 0


def name():
    return 'Sanjin'

