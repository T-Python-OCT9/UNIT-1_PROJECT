
#for lis menu to user
from nis import match


def coffee_menu(item):
    for key,valu in item:
       print(f"{key}\t\t\t{valu}")

def coffee_choise(coffee_chose):
    if coffee_chose=="1":
        print("1")
    elif coffee_chose=="2":
        print("2")
    elif coffee_chose=="3":
        print("3")
    elif coffee_chose=="4":
        print("4")
    elif coffee_chose=="5":
        print("5")
    elif coffee_chose=="6":
        print("6")
    

def itemCoffee(choice):
    coffeeType={"1":13, "2":11, "3":12, "4":13, "5":13, "6":10}
    number=0
    for key ,value in coffeeType.items():
       if key == choice:
           number=1
           return choice
       else:
            continue
    if number==0:
        print("error")


def coffeTy(number):
    count=0
    coffeeType={"1":13, "2":11, "3":12, "4":13, "5":13, "6":10}
    for n in coffeeType:
        if n==number:
            item=coffeeType.get(n)
            count=1
    if count==0:
        raise ValueError("you must chose coffee ")
    return item

