from account import *
print('---WELCOME TO SAUD BANK---')

while True:
    operatino = input("TO CREATE ACCOUNT TYPE '1'\nTO SEE YOUR ACCOUNT DATA TYPE '2'\n TO EXIT TYPE '3'\n ENTER THE OPERATION CODE: ")
    if operatino == '1':
        name = input("ENTER YOUR NAME TO CREATE AN ACCOUNT: ")
        password = input("ENTER YOUR PASSWORD: ")
        phone_number = input("ENTER YOUR PHONE NUMBER: ")
        balance = input("ENTER YOUR BALANCE: ")
    elif operatino == '2':
        pass
    elif operatino == '3':
        print("GOOD BEY")
        break 
    else:
        print("THE OPERATION IS NOT VALID !!")   
    
    name = Account(name, password, phone_number, balance)



