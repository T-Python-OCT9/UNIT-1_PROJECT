#suber class

class Buy :
    #intilaize value
    def __init__(self,price:float) -> None:
        self.__price=price
    
    def setPrice(self,price:float):
        self.__price=price
    
    def getPrice(self):
        return self.__price

    def printInfo(self):
        return f"{self.getPrice()}"



#sub class one

class Card(Buy):

    discount_price=0
    #overwrite method
    def printInfo(self):
        self.discount_price=(self.getPrice()-(self.getPrice()*0.20))
        return self.discount_price

#sub class two

class Cash(Buy):

    price_b:float=0

    #intilaize value
    def __init__(self, price: float,user_money:float) -> None:
        super().__init__(price)
        self.user_money=user_money

    #overwrite method
    def printInfo(self):
        tax=self.getPrice()+(self.getPrice()*0.15)
        if not (tax > self.user_money or isinstance(self.user_money,str)):
            self.price_b=self.user_money-tax
        else:
            raise TypeError("\nYour mony less than price coffee, or you enter incorrect type value\n")
        return self.price_b
