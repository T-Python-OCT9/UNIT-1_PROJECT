
from main import city

from main import user1


class User  :
    def __init__(self, email : str , password : str) -> None:
        self.__email = email
        self.__password= password


    def get_email (self) :
        return self.__email

    def set_email (self,vaule : str):
        self.get_email = vaule

    def set_password(self, value: str):
        if len(value) > 8:
            self.__password = value
        else:
            raise ValueError('The Password Should Be More Than 8 Digits !!')

    def get_password(self):
        return self.__password                




    def login(self):
        name = input('Please Enter Your Email: ')
        if name == user1.get_email():
            password = input('Please Enter Your Password: ')
            if lambda : password == user1.get_password(): # if password == Bank.get_password(obj1)
                city()
        


