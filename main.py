from store_data import store_data


# class 

class soccerkit:

    def __init__(self, brand:str, team:str , coulor : str, price : int, size: str) -> None:

        
        self.brand = brand
        self.team = team
        self.coulor = coulor
        self.price = price
        self.size = size

      soccerkit1 = soccerkit("adidas","arsenal" "black", "200")

class shoes:

    def __init__(self, brand:str, name:str , coulor : str, release_date : int, price: str) -> None:
        
        self.name = name
        self.brand = brand
        self.coulor = coulor
        self.release_date = release_date
        self.price = price

# intro to the store

class intro ():

    def main():

        print("*--Welcome To our website -*\n")

        kit_list, shoes_list, shorts_list = store.data.read_file()
        
        
# displaying option menu

store_sections = ["*- 1.brand", "*- 2. team", "*- 3. size ",]

for option in store_menu:
               
 print(option)


print("  Please choose !\n")


# add new item for the store manager

storelist =("teamkit": )
def storelist():

    print('1-add sport team kit')
    print('2-add brand name')
    print('3-add size release')


def addsportkit(storeList):
    team = input("enter the team kit: ")
    brand = input("choose the brand: ")
    coulor = input("choose the colour: ")
    team = input("choose the brand: ")
    price = input("choose the brand: ")


sportkit = kit(brand, team, coulor, price, size)
print(storelist.order())

storelist.append(newitem)

print("it was added \n") 

return storelist 

def addss(kitlist,storelist):

brand= input ("choose the brand: ")

brandlist=[brand]

item = True
 while (item):
        try:
            i = 0
            while i < len(storeList):
                print(1 + i, "-", storelist[i].getteamName())
                i = i + 1
            print(i+1,"- end")

            brand = int(input("choose the brand: "))
            x=i+1
       
            if brand == i+1:
                print(" have been added")
                break


# payments 

from store_data import store_data



list_price ={"tshirts": 150, "shoes": 60, "hat": 15, "shorts": 55},

   

def payment():
    p = int(input("Please enter your purchased item : "))
    if p == 1:
        payment()
    if p == 2:
        payment()   
    if p == 3:
        payment()
    if p == 4:
        payment()

def menu(list_store):
    
    print("1.tshirt\t 2.shoes\t 3.hat\t 4.Shorts")
    for d in list_price:
        print(f'{d["tshirt"]}\t\t{d["shoes"]}\t\t{d["hat"]}\t\t{d["Shorts"]}')
        payment()


 






