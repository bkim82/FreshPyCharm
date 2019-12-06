from Classwork.Chapter_5.Items import Invoice, Item


def main():
    inv = Invoice()
    
    print("This program will help to calculate the customer's invoice.\n")

    item_name = input("Enter the name of the first item purchased.")
    
    while len(item_name) > 0:
        count = int(input("How many " + item_name + " were purchased? "))
        price = float(input("What was the price for each " + item_name + "? "))
        item = Item (item_name,count, price)
        inv.addItem(item)
        
    print("\n%-30s%10s%12s%10s" % ("Item Name", "Cost Each", "Quantity", "Total"))

    for i in inv.itemList:
        print("%-30s%10.2f%12d%10.2f" % (item.name, item.price, item.quantity, item.totalPrice()))
        
        # Grand total and exit       
    print("\n\tGrand Total: $%.2f" % inv.getGrandTotal())


main()
