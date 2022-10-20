class Account:

    def __init__(self,user_name: str,password: str,phone_number: str ,balance: int):
        self.__user_name = user_name
        self.__password = password
        self.__phone_number = phone_number
        self.__balance = 0

    # user_name getter and setter
    def set_user_name(self,user_name: str):

        if not isinstance(user_name, str):
            raise ValueError('The User Name Should Be String')
        else:
            self.__user_name =user_name
    
    def get_user_name(self):
        return f'The Name Is: {self.__user_name}'

    # password getter and setter
    def set_password(self,password: str):

        if len(password) < 8:
            print('The Password Should Be More Than 8 Characters')
        else:
            self.__password =password
    
    def get_password(self):
        return f'The PassWrod Is: {self.__password}'
    
    # phone_number getter and setter
    def set_phone_number(self,phone_number: str):
        if len(phone_number) < 10:
            print("The Phone Number Should Be More Than 10 Numbers")
        self.__phone_number =phone_number
    
    def get_phone_number(self):
        return f'The Phone Number Is: {self.__phone_number}'

    # balance getter and setter    
    def set_balance(self,balance: int):
        
        if not isinstance(blance, int) and balance == 0:
            raise ValueError('The Balance Should Be Integer And More Than Zero')
        else:
            self.__balance =balance
    
    def get_balance(self):
        return f'The Balance Is: {self.__balance}'





