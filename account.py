class Account:

    def __init__(self):
        self.__name = None
        self.__password = None
        self.__id = None
        self.__balance = None

    # user_name getter and setter
    def set_name(self, value: str):

        if  not value.isdigit():
            self.__name = value
        else:
            raise ValueError('The Name Should Be string !!')
    
    def get_name(self):
        return f'Your Name Is: {self.__name}'

    # password getter and setter
    def set_password(self, value: str):

        if len(value) > 8:
            self.__password = value
        else:
            raise ValueError('The Password Should Be More Than 8 Digits !!')
    
    def get_password(self):
        return f'Your Passwrod Is: {self.__password}'
    
    # phone_number getter and setter
    def set_id(self, value: str):

        if len(value) == 10:
            self.__id = value
        else:
            raise ValueError("The ID Should Be 10 Digits !!")

    def get_id(self):
        return f'Your ID Is: {self.__id}'

    # balance getter and setter    
    def set_balance(self, value: int):

        if value.isdigit():
            self.__balance = value
        else:
            raise ValueError("The Balance Should Be Integer !!")
            
    def get_balance(self):
        return f'Your Balance Is: {self.__balance}'


# name = input("ENTER YOUR NAME TO CREATE AN ACCOUNT: ")  
# name = Account() 
# name.set_user_name('saud')
# name.set_balance(100)
# print(name.get_balance())
# print(name.get_user_name())



        
    



