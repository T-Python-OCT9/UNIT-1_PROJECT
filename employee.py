class Employee:
    def __init__(self, name: str, role: str, evaluate: float, phone_number: str, employee_id: int, user: str, password: str) -> None:
        self.__name = name
        self.__role = role
        self.__evaluate = evaluate
        self.__user = user
        self.__password = password
        self.__phone_number = phone_number
        self.__employee_id = employee_id

    def userGetter(self):
        return self.__user

    def passwordGetter(self):
        return self.__password