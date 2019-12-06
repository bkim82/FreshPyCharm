from Lab5_3.Dataset import Dataset

def main():
    d1 = Dataset("test1.txt")
    d2 = Dataset("test2.txt")
    d3 = Dataset("test3.txt")
    d4 = Dataset("test4.txt")


    print("%15s %15s %15s %15s %15s" % ("Test Name:", d1.testTopic, d2.testTopic, d3.testTopic, d4.testTopic))
    print("%15s %15s %15s %15s %15s" % ("Test Date:", d1.testDate, d2.testDate, d3.testDate, d4.testDate))
    print("%15s %15.1f %15.1f %15.1f %15.1f" % ("Median:", d1.getMedian(), d2.getMedian(), d3.getMedian(), d4.getMedian()))
    print("%15s %15.1f %15.1f %15.1f %15.1f" % ("Mean:", d1.getMean(), d2.getMean(), d3.getMean(), d4.getMean()))
    print("%15s %15.1f %15.1f %15.1f %15.1f" % ("Range:", d1.getRange(), d2.getRange(), d3.getRange(), d4.getRange()))
    print("%15s %15.1f %15.1f %15.1f %15.1f" % ("Std. Dev:", d1.getStdDev(),d2.getStdDev(),d3.getStdDev(),d4.getStdDev()))


main()
