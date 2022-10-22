#import BooksName 
class BooksPrice:
    def FunctionPrice2():
        price = {35 : "History remains open", 42 : "Les Misérables",78 : "Night train to Lisbon",15 : "Do not give up"}
       
        for j in price:
           price_list = price.keys()
        
           price_list_new =  list(filter(lambda price_list : price_list < 50 , price))
           print(price_list_new)

           break

        for i in price_list_new:
            
             if i in price.keys():
                print(price.values())
                break


    FunctionPrice2()        