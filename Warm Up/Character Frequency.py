
def readFile(filename):
    dist = {}
    file = open (filename,"r")
    for line in file:
        line = line.upper()
        for c in line:
            if c.isalpha():
                dist[c] = dist.get(c,0) + 1

    return dist


def main():
    d = readFile("story.txt")

    chars = list(d.keys())
    chars.sort()

    for c in chars:
        print (c + ": " + d(c))


main()
