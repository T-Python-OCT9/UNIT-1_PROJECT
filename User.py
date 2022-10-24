class User:
    global Coffee_List
    global Cart_Item
    global Total_price
    global Prices

    Coffee_List = ["Cappuccino","Espresso","Latte","Americano","Turkish","Hot-Chocolate","White-Mocha"]
    Prices = {1:20 , 2:16 , 3:20 , 4:16 , 5:16 , 6:18 , 7:18}
    Cart_Item = {}
    

    def View_Coffee_list(self):
        for num , item in enumerate(Coffee_List):
            print(num+1 , ". " , item ,"  ", Prices[num+1],"$" )
    

    def View_Cart_Item(self):
        for Item  in Cart_Item:
            print(Cart_Item[Item]," ",Item)
        print("-------------------------------\n")
        

    def Add_Item(self):
        New_Item = input("Enter name of item: ")
        if (New_Item in Coffee_List):
            Quantity =int(input("Enter the quantity of item: ")) 
            Cart_Item[New_Item] = Quantity
        else:
            print("The item not avalibal...")
        
        while True:
            More_Item_Added = input("Do you want continu Add to cart yes or no? ")
            if More_Item_Added.lower() == "yes":
                New_Item = input("Enter name of item: ")
                if (New_Item in Coffee_List):
                    Quantity =int(input("Enter the quantity of item: ")) 
                    Cart_Item[New_Item] = Quantity
                else:
                    print("The item not avalibal...")
            elif More_Item_Added.lower() == "no":
                break
            else:
                print("Your enter not valid..")
        print("-------------------------------\n")


    def Remove_Item(self):
        self.View_Coffee_list()
        Delete_Item = input("Enter the name of item you want remove: ")
        if (Delete_Item in Cart_Item):
            del Cart_Item[Delete_Item]
            print(f"The item {Delete_Item} has been deleted...")
        else:
            print("The item not in the cart...")
    
    def Receipt(self):
        Total_price = 0
        for item in Cart_Item:
            if item =="Cappuccino":
                 print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[1]} $")
                 Total_price = Cart_Item[item] *Prices[1]+ Total_price
            elif item == "Espresso":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item]*Prices[2]} $")
                Total_price = Cart_Item[item] *Prices[2]+ Total_price
            elif item == "Latte":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[3]} $")
                Total_price = Cart_Item[item] *Prices[3]+ Total_price
            elif item == "Americano":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[4]} $")
                Total_price = Cart_Item[item] *Prices[4]+ Total_price
            elif item == "Turkish":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[5]} $")
                Total_price = Cart_Item[item] *Prices[5]+ Total_price
            elif item == "Hot-Chocolate":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[6]} $")
                Total_price = Cart_Item[item] *Prices[6]+ Total_price
            elif item == "White-Mocha":
                print(f"{Cart_Item[item]} {item}  : {Cart_Item[item] *Prices[7]} $")
                Total_price = Cart_Item[item] *Prices[7]+ Total_price
            else:
                pass

        print("\n\nThe total:  " , Total_price,"$ ")
        Discount = lambda x : x*0.2
        Discount_Code = input("Enter the discount code if you have: ")
        if Discount_Code.lower() =="coffee":
            print("The total after the discount: ",Total_price - Discount(Total_price)," $")
        else:
            pass
        print("\n-------------------------------")
    
    def Clear_List(self):
        Cart_Item.clear()