from Lab5_2.Vehicle import Vehicle

def main():
    civic = Vehicle("Honda", "Civic", 12.4, 35)

    print(civic)

    if civic.fuelLevel == 12.4:
        print("Passed 1")
    else:
        print("Failed 1")

    if civic.make == "Honda":
        print("Passed 2")
    else:
        print("Failed 2")

    if civic.model == "Civic":
        print("Passed 3")
    else:
        print("Failed 3")

    if civic.mpg == 35:
        print("Passed 4")
    else:
        print("Failed 4")

    civic.addGas(15)

    if civic.fuelLevel == 12.4:
        print("Passed 5")
    else:
        print("Failed 5")

    if civic.getRange() == 434:
        print("Passed 6")
    else:
        print("Failed 6")

    civic.drive(40)
    civic.drive(100)

    if civic.getRange() == 294:
        print("Passed 7")
    else:
        print("Failed 7")


    if civic.totalMiles == 140:
        print("Passed 8")
    else:
        print("Failed 8")

    if int(civic.fuelLevel) == 8:
        print("Passed 9")
    else:
        print("Failed 9")

    civic.addGas(1)

    if int(civic.fuelLevel) == 9:
        print("Passed 10")
    else:
        print("Failed 10")

    print(civic)

    civic.drive(1000)

    if civic.fuelLevel == 0:
        print("Passed 11")
    else:
        print("Failed 11")

    if civic.totalMiles == 469:
        print("Passed 12")
    else:
        print("Failed 12")

    print(civic)

main()
