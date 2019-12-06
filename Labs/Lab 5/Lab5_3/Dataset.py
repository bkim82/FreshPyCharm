class Dataset (object):

    def __init__ (self, file_name):

        scores = []
        file = open(file_name, "r")
        line1 = file.readline().strip()
        line2 = file.readline().strip()
        for number in file:
            number = int(number.strip())
            scores.append(number)

        self.testTopic = line1
        self.testDate = line2
        self.__numList = scores


    def getMean (self):

        total = 0

        for n in self.__numList:
            total += n

        return total / len(self.__numList)

    def getRange (self):
        return max(self.__numList) - min(self.__numList)

    def getMedian (self):
        # self.__numList.sort()
        #
        # if len(self.__numList) % 2 == 0:
        #
        #     pos = len(self.__numList)
        #     pos2 = pos + 1
        #     pos3 = pos2 // 2
        #     return self.__numList[pos3]
        #
        # else:
        #
        #     pos = len(self.__numList) % 2
        #     return self.__numList[pos]

        # med_scores = self.__numList[:]
        # while len(med_scores) > 2:
        #     del(med_scores[0])
        #     del(med_scores[-1])
        # if len(med_scores) == 2:
        #     return(med_scores[0] + med_scores[1]) / 2
        # else:
        #     return med_scores[0]

        n = len(self.__numList)

        if n % 2 == 1:
            return sorted(self.__numList)[n // 2]
        else:
            return sum(sorted(self.__numList)[n // 2 - 1:n // 2 + 1]) / 2.0


    def getStdDev (self):
        m = self.getMean()
        dev = 0

        for i in range(len(self.__numList)):
            s = self.__numList[i]
            s -= m
            s **= 2
            dev += s

        dev /= len(self.__numList)
        dev **= .5

        return dev
