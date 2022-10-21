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

start=input("\nIf you want drink coffee enter \"*\"")
while(start=="*"):
    chose_coffee=input("Chose coffee you want plese:")
    break
    #pass
    #coffee menu









