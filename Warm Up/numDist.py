def readFile(fileName):
    textFile = open(fileName, "r")
    d = {}

    for line in textFile:
        nums = line.split(",")
        for num in nums:
            num = int(num)
            d[num] = d.get(num, 0) + 1

    return(d)


def main():
    d = readFile("num_dist_1.txt")
    print(d)

    keyList = list(d.keys())

    keyList.sort()
    for k in keyList:
        print ("%d: %d" % (k, d[k]))




main()