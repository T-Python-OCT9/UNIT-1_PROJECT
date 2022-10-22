from mybank import Bank

def user():
    while True:   
            try:
                print('-------------------------')
                option = input('To Deposit Type "1"\nTo Withdraw Type "2"\nTo Print Balance Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
                if option == '1':
                    obj1.deposit(int(input('Please Enter The Number: ')))
                    print(Bank.get_balance(obj1))
                elif option == '2':
                    obj1.withdraw(int(input('Please Enter The Number: ')))
                    print(Bank.get_balance(obj1))
                elif option == '3':
                    print(Bank.get_balance(obj1))
                elif option == '4':
                    print('---Thank You---')
                    break
                else:
                    print('This Option Is Not Valid')
            except ValueError as error_massage:
                print(error_massage)
        

def admin():
    while True:
        try:
            print('-------------------------')
            option = input('To Change User Name Type "1"\nTo Change User ID Type "2"\nTo Change User Stats Type "3"\nTo Exit Type "4"\nPlease Type The Command: ')
            if option == '1':
                Bank.set_name(obj1, input('Please Enter The New Name: '))
                print(Bank.get_name(obj1))
            elif option == '2':
                Bank.set_id(obj1,input('Please Enter The New ID: '))
                print(Bank.get_id(obj1))
            elif option == '3':
                Bank.set_stats(obj1,input('Please Enter The New Stats: '))
                print(Bank.get_stats(obj1))
            elif option == '4':
                print('---Thank You---')
                break
            else:
                print('This Operation Is Not Valid')
        except ValueError as error_massage:
            print(error_massage)


def chick_password(value: str)-> bool:
    text = Bank.get_password(obj1)
    index = text.find(':')
    password = text[index+1:]
    if password.strip() == value:
        return True


def main():
    print('---WELCOME TO SAUD BANK---')
    while True:
        print('-------------------------')
        print('Type "exit" To Terminate The Program')
        
        name = input('Please Enter Your Name: ')
        if name == 'exit':
            print('---Good Bey---')
            break

        password = input('Please Enter Your Password: ')
        if chick_password(password):
            user() 
        elif filter(lambda : password == 'aa', password):
            admin()
        else:
            print('invalid input !!')


obj1 = Bank('saud', '123', '11', 1000)

main()

                


        
    
            

        


    
        

    




  
    
 



