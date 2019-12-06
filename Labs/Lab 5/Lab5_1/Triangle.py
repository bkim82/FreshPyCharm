#Brandon Kim
#Triangle 5-1

class Triangle(object):

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def isScalene(self):
        if self.side1 != self.side2 and self.side2 != self.side3:
           if self.side1 != self.side3:
               return True
           else:
               return False

    def isIsosceles(self):
        if self.side1 == self.side2:
            return True
        elif self.side2 == self.side3:
            return True
        elif self.side1 == self.side3:
            return True

        return False

    def isEqualateral(self):
        if self.side1 == self.side2 and self.side2 == self.side3:
            return True

        return False

    def getPerimeter(self):

        return self.side1 + self.side2 + self.side3

    def dilate(self,factor):

        return self.side1/ factor, self.side2 / factor, self.side3 / factor

    def isCongruent(self,tri2):
        if self.side1 == tri2.side1 and self.side2 == tri2.side2 and self.side3 == tri2.side3:
            return True
        else:
            return False


    def __str__(self):

        # self.side1 = str(self.side1)
        # self.side2 = str(self.side2)
        # self.side3 = str(self.side3)

        return ("\t %s %.1f \n\t %s %.1f \n\t %s %.1f" % ("Side 1:",self.side1,"Side 2:",self.side2,"Side 3:", self.side3))