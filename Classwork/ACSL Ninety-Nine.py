def playCard(card,score):
    if card == 9:

        return score
    elif card == 4:
        return score - 10
    else:
        del(x[total - 1])
        return score + card





def runInput(filename):
    d = []
    textFile = open(filename, "r")
    for line in textFile:
        game = line.split(",")
        runInput(game)




    return d

def main():
    total = len("acsl_jr_1.txt")
    d = runInput("acsl_jr_1.txt")
    print(d)