class Point (object):
    def __init__(self,posx, posy):
        self.x = posx
        self.y = posy

    def translate (self, dx, dy):
        self.x += dx
        self.y += dy

    def dilate (self, factor):
        self.x *= factor
        self.y *= factor

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Rectangle(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def getWidth(self):
        return abs(self.p1.x - self.p2.x)

    def getHeight(self):
        return abs(self.p1.y - self.p2.y)

    def getArea(self):
        return self.getWidth() * self.getHeight()

    def getPerimeter(self):
        return 2*(self.getWidth() * self.getHeight())

    def dilate(self, factor):
        self.p1.dilate(factor)
        self.p2.dilate(factor)

    def translate(self, dx, dy):
        self.p1.translate(dx, dy)
        self.p2.translate(dx, dy)

    def __str__(self):
        return "Rect: " + str(self.p1) + ", " + str(self.p2)