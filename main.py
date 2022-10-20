from account import *

print('---WELCOME TO SAUD BANK---')
def create_account():
    while True:
        try:
            user_name = user_object = input("ENTER YOUR NAME TO CREATE AN ACCOUNT: ")  
            user_object = Account() 
            user_object.set_name(user_name)
            password = input("ENTER YOUR PASSWORD: ")
            user_object.set_password(password)
            _id = input("ENTER YOUR ID: ")
            user_object.set_id(_id)
            balance = input("ENTER YOUR Balance: ")
            user_object.set_balance(balance)

        except ValueError as e:
            print(e)
            print("---Try Again---")
            
        else:
            print("---Account Created Successfully---")
            print(Account.get_name(user_object))
            print(Account.get_password(user_object))
            print(Account.get_id(user_object))
            print(Account.get_balance(user_object))
            break
    
            

        


    
        

    




  
    
 



