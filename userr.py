
from User import *




#print(f"{nestle_most_sold_product} {nestle_most_sold_product_figure} US Dollars")

def welcom(name):
    print("welcome", name)

def order_menu():
    print("1.Menu")
    print("2.Payment")
    print("3.Exit")

def dataUser():
    name= input("Please enter your name")
    phone_number= input("Please enter your phone number")
    order_menu()
   
print("************Resurant**************")
dataUser()