from admin import Admin
from mybank import BankUser


user1 = BankUser('saud', '123', '1234567890')

admin1 = Admin('ali', '1234567890', '123')

def login():
    name = input('Please Enter Your Name: ')
    if name == user1.get_name():
        password = input('Please Enter Your Password: ')
        if lambda : password == user1.get_password(): # if password == Bank.get_password(obj1)
            user()
    elif name == admin1.get_name():
        password = input('Please Enter Your Password: ')
        if lambda : password == (admin1.get_password()):
            admin()
    else:
        print('invalid input !!')

def signin():
    user1.set_name(input('Please Enter Your Name: '))
    user1.set_password(input('Please Enter Your Password: '))
    user1.set_id(input('Please Enter Your Password: '))
    print('---Thank You---')
    main()

def user():
    while True:
        print('-------------------------')
        option = input('To Deposit Type "1"\nTo Withdraw Type "2"\nTo Print Balance Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
        if option == '1':
            user1.deposit(int(input('Please Enter The Number: ')))
            print(f'Your New Balance Is: {user1.get_balance()}\n{BankUser.get_date()}')
        elif option == '2':
            user1.withdraw(int(input('Please Enter The Number: ')))
            print(f'Your New Balance Is: {user1.get_balance()}\n{BankUser.get_date()}')
        elif option == '3':
            print(f'Your Balance Is: {user1.get_balance()}\n{BankUser.get_date()}')
        elif option == '4':
            print('---Thank You---')
            main()
            break
        else:
            print('This Option Is Not Valid')
        
def admin(): 
    while True: 
        print('-------------------------')
        option = input('To Change User Name Type "1"\nTo Change User ID Type "2"\nTo Change User Stats Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
        if option == '1':
            user1.set_name(input('Please Enter The New Name: '))
            print(f'The New Name Is :{user1.get_name()}')
        elif option == '2':
            user1.set_id(input('Please Enter The New ID: '))
            print(f'The New ID Is: {user1.get_id()}')
        elif option == '3':
            user1.set_status(input('Please Enter The New Status: '))
            print(f'The New Status Is: {user1.get_status()}')
        elif option == '4':
            print('---Thank You---')
            main()
            break
        else:
            print('This Operation Is Not Valid')

def main():
    print('-------------------------')
    print('---WELCOME TO SAUD BANK---')
    while True:
        print('-------------------------')
        option = input('Type "1" If You Have An Account\nType "2" To Create An Account\nType "exit" To Terminate The Program\nPlease Type The Command: ')
        if option == '1':
            try:
                login()
                break
            except ValueError as error_massage:
                print(error_massage)
        elif option == '2':
            try:
                signin()
                break
            except ValueError as error_massage:
                print(error_massage)
        elif option == 'exit':
            print("---Good Bey---")
            break 
        else:
            print('This Operation Is Not Valid')


main()

                


        
    
            

        


    
        

    




  
    
 



