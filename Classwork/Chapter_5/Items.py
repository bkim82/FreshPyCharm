class Item (object):
    def __init__ (self, n, q, p):
        self.name = n
        self.quantity = q
        self.price = p

    def totalPrice(self):
        return self.price * self.quantity

    def __str__ (self):
        return "Name: " + self.name + "; Quantity: " + str(self.quantity)

class Invoice (object):
    def __init__ (self):
        self.itemList = []

    def addItem (self, item):
        self.itemList.append(item)

    def getGrandTotal (self):
        total = 0
        for item in self.itemList:
            total += item.totalPrice()
        return total

    def __str__(self):
        s = ""
        for item in self.itemList:
            s += str(item) + "\n"
        return s


# def main():
#     inv = Invoice()
#     item1 = Item("Frogs", 14, 1.35)
#     item2 = Item("Dogs", 2, 15)
#
#     inv.addItem(item1)
#     inv.addItem(item2)
#
#     #print ("Item 1: ", item1)
#     #print("Item 2: ", item2)
#
#     #print("Item 1 total: %.2f" % item1.totalPrice())
#
#     print(inv)
#
#
# main()