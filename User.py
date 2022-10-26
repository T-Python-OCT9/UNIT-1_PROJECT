from tkinter import END
from User import *



list_food ={"Burger": 50, "Pizza": 60, "Frizz": 10, "Soft drink": 15},


#print(f"{nestle_most_sold_product} {nestle_most_sold_product_figure} US Dollars")
def payment():
    pay=input("cash or card : ")
    if pay == "cash":
        print("paid")
    if pay == "card":
        print("paid")   

def opOrder():
    op = int(input("Please enter name Food : "))
    if op == 1:
        payment()
    if op == 2:
        payment()   
    if op == 3:
        payment()
    if op == 4:
        payment()

def menu(list_food):
    
    print("1.Burger\t 2.Pizza\t 3.Frizz\t 4.Soft drink")
    for d in list_food:
        print(f'{d["Burger"]}\t\t{d["Pizza"]}\t\t{d["Frizz"]}\t\t{d["Soft drink"]}')
        opOrder()




def opMenu():
    op = int(input("Please choices : "))
    if op == 1:
        menu(list_food)  
    elif op == 2:
        print("bye !")
        END

def order_menu():
    print("1.Menu")
    print("2.Exit")
    opMenu()
    
def welcome(name):
    print("welcome", name)
    order_menu()

def dataUser():
    name= input("Please enter your name : ")
    phone_number= input("Please enter your phone number : ")
    welcome(name)
   
print("************Resurant**************")
dataUser()    