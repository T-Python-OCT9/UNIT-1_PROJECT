import os
from cli_view import CommandLineView
from manager import managerLogin
from employee import employeeLogin


main_view = CommandLineView({
    'message': '\n\t\tWelcome to HR System\n\n Type one of these commands to execute:\n\t(M) \t\t- Manager login.\n\t(E)\t\t- Employe login. \n\t(EXIT)\t\t- Exit the system. \n\n',
    'commands': ['m', 'e', 'exit']
})


def mainView():
    command = main_view.commandLineListener()
    if command == 'm':
        managerLogin()
        os.system('clear')
        print("\n\t\tLogged out...\n\t\tThank you for using HR System.\n")
    elif command == 'e':
        employeeLogin()
        os.system('clear')
        print("\n\t\tLogged out...\n\t\tThank you for using HR System.\n")
    elif command == 'exit':
        os.system('clear')
        print("\n\t\tThank you for using HR System.\n")


mainView()

