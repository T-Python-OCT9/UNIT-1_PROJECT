class Admin:
    def __init__(self,name: str, id: str, password: str):
        self.__name = name
        self.__id = id
        self.__password = password
    
     # user_name getter and setter
    def set_name(self, value: str):
        if  not value.isdigit():
            self.__name = value
        else:
            raise ValueError('The Name Should Be string !!')
    
    def get_name(self):
        return self.__name

    # password getter and setter
    def set_password(self, value: str):
        if len(value) > 8:
            self.__password = value
        else:
            raise ValueError('The Password Should Be More Than 8 Digits !!')
    
    def get_password(self):
        return self.__password
    
    # phone_number getter and setter
    def set_id(self, value: str):
        if len(value) == 10:
            self.__id = value
        else:
            raise ValueError("The ID Should Be 10 Digits !!")

    def get_id(self):
        return self.__id



