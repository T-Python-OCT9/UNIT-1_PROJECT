
#for lis menu to user
from nis import match

def coffee_menu(item):
    for key,valu in item:
       print(f"{key}\t\t\t{valu}")

    
def coffeePrice(number):
    count=0
    coffeeType={"1":15, "2":13, "3":12, "4":14, "5":16, "6":15}
    for n in coffeeType:
        if n==number:
            item=coffeeType.get(n)
            count=1
    if count==0:
        raise ValueError("you must chose coffee ")
    return item

def coffeeName(number):
    count=0
    coffeeType={"1":"coffee1", "2":"coffee2", "3":"coffee3", "4":"coffee4", "5":"coffee5", "6":"coffee6"}
    for n in coffeeType:
        if n==number:
            item=coffeeType.get(n)
            count=1
    if count==0:
        raise ValueError("you must chose coffee ")
    return item

