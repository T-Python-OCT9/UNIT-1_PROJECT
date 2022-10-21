import CoffeeType as coffee


#main class
#explain programming for user
print("_"*50)
print("\nHi, this is coffee machine, we have past coffee her\nTo order you must chose to start\"*\"\nTo chose your coffee enter \" \"\nTo complete your order enter \" \"\nTo chang your order enter \"\"\nTo cansel your order enter \"\"\nNow we will list the menue:\n")
#start program
coffeeDictionary={"coffee1":15,
    "coffee2":13 ,
    "coffee3":12,
    "coffee4":14,
    "coffee5":16,
    "coffee6":15}
   #list coffee menu
item_coffee=coffeeDictionary.items()
coffee.coffee_menu(item_coffee)

start=input("\nIf you want drink coffee enter \"*\"\n")
while(start=="*"):
    print("\nTo chose coffee1 enter \"1\"\nTo chose coffee2 enter \"2\"\nTo chose coffee3 enter \"3\"\nTo chose coffee4 enter \"4\"\nTo chose coffee5 enter \"5\"\nTo chose coffee6 enter \"6\"")
    chose_coffee=input("Chose coffee you want plese:")
    complete_order=input("if you want to complete your order enter \"y\",if you want to cancel your order enter\"n\":\n")
    if complete_order=="y"or complete_order=="Y":
        print("price")
        break
    elif complete_order=="n" or complete_order=="N":
        break
    
    #pass
    #coffee menu









