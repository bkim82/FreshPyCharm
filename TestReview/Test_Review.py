def table_by_for_loop():
    print("%7s %15s" % ("Inches", "Centimeters"))
    for inch in range(5, 33, 9):
        print("%7d %15.1f" % (inch, (inch * 2.54)))


def position_of_longest (thelist):
    pos = 0
    for i in range (1, len(thelist)):
        if len(thelist[i]) > len(thelist[pos]):
            pos = i
    return pos

def position_of_longest (thelist):
    pos = 0
    for i in range (1, len(thelist)):
        if len(thelist[i] > len(thelist[pos]):
            pos = i
    return pos


def position_of_lonest(thelist):
    pos = 0
    for n in range(1, len(thelist)):
        if len(thelist[i] > len(thelist[pos]):
            pos = i
def product (thelist):
    total = 1
    for n in thelist:
        product *= n
    return total

def print_semicolon_list(thelist):
    for n in thelist:
        print (n, end = "; ")

def count_vowels(my_str):
    total = 0
    my_str = my_str.upper()
    for n in my_str:
        if n in ("AEIOU"):
            total += 1

    return total

def main():
    table_by_for_loop()

main()