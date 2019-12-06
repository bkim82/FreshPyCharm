from Lab5_1.Triangle import Triangle

def main():
    t1 = Triangle (5, 4, 6)

    print("Created 5, 4, 6 triangle")
    print(t1)
    
    if not t1.isIsosceles():
        print("Passed 1")
    else:
        print("Failed 1")
    
    if t1.isScalene():
        print("Passed 2")
    else:
        print("Failed 2")
    
    if t1.getPerimeter() == 15:
        print("Passed 3")
    else:
        print("Failed 3")
    
    t1.dilate(2)
    if t1.getPerimeter() == 30:
        print("Passed 4")
    else:
        print("Failed 4")
    
    print("\n--------------------------------\n")

    t2 = Triangle(12,12,8)
    print("Created 12,12,8 triangle")
    print(t2)
    
    if t2.isIsosceles():
        print("Passed 5")
    else:
        print("Failed 5")
    
    if not t2.isScalene():
        print("Passed 6")
    else:
        print("Failed 6")
    
    if t2.getPerimeter() == 32:
        print("Passed 7")
    else:
        print("Failed 7")
    
    t2.dilate(.5)
    if t2.getPerimeter() == 16:
        print("Passed 8")
    else:
        print("Failed 8")
    
    if not t1.isCongruent(t2):
        print("Passed 9")
    else:
        print("Failed 9")
    
    t3 = Triangle(10, 8, 12)
    
    if (t1.isCongruent(t3)):
        print("Passed 10")
    else:
        print("Failed 10")

main()