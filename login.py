import os
from getpass import getpass
from cli_view import CommandLineView


class LoginView(CommandLineView):

    def __init__(self, user: str, password: str) -> None:
        self.__user = user
        self.__password = password

    def commandLineListener(self) -> str:
        insert_user: str = ''
        insert_password: str = ''
        while not (insert_user == self.__user and insert_password == self.__password):
            if len(insert_user or insert_password) >= 2:
                os.system('clear')
                print(f"\n\t\tLogin\n\n")
                print(' \t# Username or password is wrong\n')
            else:
                os.system('clear')
                print(f"\n\t\tLogin\n\n")
            insert_user = input(' Username: ')
            insert_password = getpass(prompt=' Password: ')
        return super() == 'logged'