from Classwork.Chapter_5.Geometry import Point, Rectangle

def main():
    p1 = Point(3,2)
    p2 = Point(-9,4)

    print("Point 1: ", p1)
    print("Point 2L ", p2)

    p1.dilate(2)
    p2.translate(5,-1)

    print("Point 1: " + str(p1))
    print("Point 2: " + str(p2))

    r = Rectangle(p1, p2)
    print(r)
    r.translate(1,-2)
    print(r)

    print ("Area: ", r.getArea())
    print ("Perimeter: ", r.getPerimeter())


main()