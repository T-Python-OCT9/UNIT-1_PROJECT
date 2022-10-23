import CoffeeType as coffee
import Classes


#main class
#explain programming for user
print("_"*50)
print("\nHi, this is coffee machine, we have past coffee her\nTo order you must chose to start\"*\"\nTo chose your coffee enter \" \"\nTo complete your order enter \" \"\nTo chang your order enter \"\"\nTo cansel your order enter \"\"\nNow we will list the menue:\n")
#Dictionary for coffee menue
coffeeDictionary={"coffee1":15,
    "coffee2":13 ,
    "coffee3":12,
    "coffee4":14,
    "coffee5":16,
    "coffee6":15}
#list coffee menue
item_coffee=coffeeDictionary.items()
coffee.coffee_menu(item_coffee)


#lambda 
tax_calculation=lambda price_lambda:price_lambda+(price_lambda*0.15)

#To start program
start=input("\nIf you want drink coffee enter \"*\"\n")
while(start=="*"):
    print("\nTo chose coffee1 enter \"1\"\nTo chose coffee2 enter \"2\"\nTo chose coffee3 enter \"3\"\nTo chose coffee4 enter \"4\"\nTo chose coffee5 enter \"5\"\nTo chose coffee6 enter \"6\"")
    choice=input("Chose coffee you want plese:")
    try:
        price=coffee.coffeePrice(choice)
        coffee_name=coffee.coffeeName(choice)
        print(f"price is : {price}")
    except ValueError as error:
        print(error)
        break
    complete_order=input("if you want to complete your order enter \"y\",if you want to cancel your order enter\"n\":\n")
    if complete_order=="y"or complete_order=="Y":
        print("How do you want to \'?\'\n*Note, If you buy from card you will have discount 20%")
        buy=input("enter \"1\" to chose card or \"2\" to cash: \n")
        if buy=="1":
            card_buy=Classes.Card(price)
            discount_price=card_buy.printInfo()
            print(f"Your order is {coffee_name} and the price after discount is {discount_price}, The price after calculator tax is {tax_calculation(discount_price)}")
            complete_with_card= input("enter C to buy, if you want to cancel enter n:\n")
            if complete_with_card=="c" or complete_with_card=="C":
                print(f"your coffee {coffee_name} is ready, take it pleas ")
                start=input("do you want order another coffee ? if you want enter \"*\" if you do not enter no")
            elif complete_with_card=="n" or complete_with_card=="N":
                pass
        elif buy=="2":
            user_m=input("enter your mony plese: \n")
            try:
                cash_buy=Classes.Cash(price,float(user_m))
                mouny_p:float=cash_buy.printInfo()
            except TypeError as error:
                print(error)
                break
            print(f"Your order is {coffee_name} and the mony after discount price is {mouny_p}, The price after calculator tax is {tax_calculation(price)}\nTake \'?\'")
            print(f"your coffee {coffee_name} is ready, take it pleas ")
            start=input("do you want order another coffee ? if you want enter \"*\" if you do not enter no")

    elif complete_order=="n" or complete_order=="N":
        break

print("Thank you for use coffee machine")








