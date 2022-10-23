from mybank import Bank

def login():
    name = input('Please Enter Your Name: ')
    if name == Bank.get_name(obj1):
        password = input('Please Enter Your Password: ')
        if password == Bank.get_password(obj1):
            user()
    else:
        print('invalid input !!')


def signin():
    Bank.set_name(obj1, input('Please Enter Your Name: '))
    Bank.set_password(obj1, input('Please Enter Your Password: '))
    print('---Thank You---')
    main()


def user():
    while True:
        print('-------------------------')
        option = input('To Deposit Type "1"\nTo Withdraw Type "2"\nTo Print Balance Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
        if option == '1':
            obj1.deposit(int(input('Please Enter The Number: ')))
            print(f'Your New Balance Is: {Bank.get_balance(obj1)}\n{Bank.get_date()}')
        elif option == '2':
            obj1.withdraw(int(input('Please Enter The Number: ')))
            print(f'Your New Balance Is: {Bank.get_balance(obj1)}\n{Bank.get_date()}')
        elif option == '3':
            print(f'Your Balance Is: {Bank.get_balance(obj1)}\n\n{Bank.get_date()}')
        elif option == '4':
            print('---Thank You---')
            main()
        else:
            print('This Option Is Not Valid')

        
def admin(): 
    while True: 
        print('-------------------------')
        option = input('To Change User Name Type "1"\nTo Change User ID Type "2"\nTo Change User Stats Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
        if option == '1':
            Bank.set_name(obj1, input('Please Enter The New Name: '))
            print(f'The New Name Is :{Bank.get_name(obj1)}')
        elif option == '2':
            Bank.set_id(obj1,input('Please Enter The New ID: '))
            print(f'The New ID Is: {Bank.get_id(obj1)}')
        elif option == '3':
            Bank.set_status(obj1,input('Please Enter The New Status: '))
            print(f'The New Status Is: {Bank.get_status(obj1)}')
        elif option == '4':
            print('---Thank You---')
            main()
        else:
            print('This Operation Is Not Valid')


def main():
    print('-------------------------')
    print('---WELCOME TO SAUD BANK---')
    while True:
        print('-------------------------')
        option = input('Type "1" If You Have An Account\nType "2" To Create An Account\nType "exit" To Terminate The Program\nPlease Type The Command :')
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
        elif option == 'aa':
            try:
                admin()
                break
            except ValueError as error_massage:
                print(error_massage)
        elif option == 'exit':
            print("---Good Bey---")
            break 
        else:
            print('This Operation Is Not Valid')


obj1 = Bank('saud', '123', '1234567890')
main()

                


        
    
            

        


    
        

    




  
    
 



