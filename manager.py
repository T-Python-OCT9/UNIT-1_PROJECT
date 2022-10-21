class Manager:
    def __init__(self, name: str, phone_number: str, employe_id: int, user: str, password: str) -> None:
        self.__user = user
        self.__password = password
        self.__name = name
        self.__phone_number = phone_number
        self.__employe_id = employe_id

    def userGetter(self):
        return self.__user

    def passwordGetter(self):
        return self.__password