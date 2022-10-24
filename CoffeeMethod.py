

from nis import match



#for lis menu to user
def coffee_menu(item):
    for key,valu in item:
       print(f"{key}\t\t\t\t{valu}")

#print price    
def coffeePrice(number):
    count=0
    coffeeType={"1":16, "2":16, "3":10, "4":11, "5":16, "6":15}
    for n in coffeeType:
        if n==number:
            item=coffeeType.get(n)
            count=1
    if count==0:
        raise ValueError("\nYou must choose from menu\n")
    return item
#print coffee name
def coffeeName(number):
    count=0
    coffeeType={"1":"Cappuccino", "2":"Latte", "3":"Espresso", "4":"Americano", "5":"Mocha", "6":"Hotchocolate"}
    for n in coffeeType:
        if n==number:
            item=coffeeType.get(n)
            count=1
    if count==0:
        raise ValueError("\nYou must choose from menu\n")
    return item

