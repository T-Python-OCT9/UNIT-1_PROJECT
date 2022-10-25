class Employee:
    def __init__(self, name, Salary, officer, years_of_service) -> None:
        self.__name = name
        self.__Salary = Salary
        self.__officer = officer
        self.__years_of_service = years_of_service

        name= inpot("Please write the employee's name")
