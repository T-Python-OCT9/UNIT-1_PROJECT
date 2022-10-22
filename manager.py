from cli_view import CommandLineView
from login import LoginView


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


manager_home = CommandLineView({
    'message': '\n\t Authorization: Manager \n\n Type one of these commands to execute:\n\t(S) \t\t- Show employees list.\n\t(A)\t\t- Add new employee. \n\t(C)\t\t- Change employee profile. \n\t(R)\t\t- Remove employee.\n\t(E)\t\t- Evaluate an employee. \n\t(LOGOUT)\t- Logut from the system. \n\n',
    'commands': ['s', 'a', 'c', 'r', 'e', 'logout']
})



manager1 = Manager('Ahmed', '0555555555', '92126', 'ahmed', '1234')
login_manager1 = LoginView(manager1.userGetter(), manager1.passwordGetter())


def managerLogin():
    command: str = login_manager1.commandLineListener()
    if command == 'logged':
        manager_home.commandLineListener()
