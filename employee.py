from distutils.cmd import Command
from cli_view import CommandLineView
from login import LoginView


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


employee_home = CommandLineView({
    'message': '\n\t Authorization: Employee \n\n Type one of these commands to execute:\n\t(S) \t\t- Salaries list.\n\t(P)\t\t- Promotion. \n\t(R)\t\t- Resignation. \n\t(C)\t\t- Complaints. \n\t(LOGOUT)\t- Logut from the system. \n\n',
    'commands': ['s', 'p', 'r', 'c', 'logout']
})

employee1 = Employee('Khaled', 'Engineer', 3.2,
                     '0555555555', '92126', 'khaled', '1234')
employee1_login = LoginView(employee1.userGetter(), employee1.passwordGetter())


def employeeLogin():
    login_command: str = employee1_login.commandLineListener()
    if (login_command == 'logged'):
        employee_home.commandLineListener()
