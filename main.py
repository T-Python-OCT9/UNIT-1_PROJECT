from mybank import *

def user():
    while True:   
            try:
                operation = input('To Deposit Type "1"\nTo Withdraw Type "2"\nTo Print Balance Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
                if operation == '1':
                    obj1.deposit(int(input('Please Enter The Number: ')))
                elif operation == '2':
                    obj1.withdraw(int(input('Please Enter The Number: ')))
                elif operation == '3':
                    print(Bank.get_balance(obj1))
                elif option == '4':
                    print('---Good Bey---')
                    break
                else:
                    print('This Operation Is Not Valid')
            except ValueError as error_massage:
                print(error_massage)
        

def admin():
    while True:
        option = input('To Change User Name Type "1"\nTo Change User ID Type "2"\nTo Change User Stats Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
        if option == '1':
            value = input('Please Enter The Name: ')
            Bank.set_name(obj1, value)
            print(Bank.get_name(obj1))
        elif option == '2':
            value = input('Please Enter The ID: ')
            Bank.set_id(obj1,value)
        elif option == '3':
            value = input('Please Enter The Name: ')
            Bank.set_stats(obj1,value)
        elif option == '4':
            print('---Good Bey---')
            break
        else:
            print('This Operation Is Not Valid')


def chick_password(value: str)-> bool:
    text = Bank.get_password(obj1)
    index = text.find(':')
    password = text[index+1:]
    if password.strip() == value:
        return True


def main():
    print('---WELCOME TO SAUD BANK---')
    while True:
        name = input('ENTER YOUR NAME: ')
        password = input('ENTER YOUR PASSWORD: ')

        if chick_password(password):
            user() 
            break  
        elif password == 'aa':
            admin()
            break
        else:
            print('invalid input!!')


obj1 = Bank('saud', '123', '11', 1000)

main()

                


        
    
            

        


    
        

    




  
    
 



