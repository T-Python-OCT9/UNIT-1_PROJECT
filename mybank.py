class Bank:

    def __init__(self, name, password, id, balance):
        self.__name = name
        self.__password = password
        self.__id = id
        self.__balance = balance
        self.__stats = 'open'
        
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

    # stats getter and setter
    def set_stats(self, value):
        self.__stats = value
    
    def get_stats(self):
        return f'{get_name()} Account Is: {self.__stats}'

    # methods
    def deposit(self,value):
        if not isinstance(value, int):
            raise ValueError('Please Enter Integer Value')
        else:
            self.__balance = self.__balance + value
            

    def withdraw(self, value):
        if not isinstance(value, int) and value <= 0:
            raise ValueError('Please Enter Value Larger Than Zero')
        else:
             if self.__balance > value:
                self.__balance = self.__balance - value
             else:
                print('This Number is Not Avialable In Your Account')
           
            
    
   



        





        
    



