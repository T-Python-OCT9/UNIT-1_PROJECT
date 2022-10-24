from cli_view import commandLine
from manager import managerView
from employee import employeeView, employees_list
import os


def homeView() -> None:
    result = 'home'
    while result == 'home':
        result = commandLine(
            '# Welcome to HR System\n\t----------------------\n\n \tType one of these commands:\n\t (M)    - Manager Login.\n\t (E)    - Employee Login.\n\t (EXIT) - Exit the system.')
        if result == 'm':
            managerView(result)
        elif result == 'e':
            employeeView(result)
        elif result == 'exit':
            os.system('clear')
            print('\n\t\tThank you for using the HR System\n\n')
            break
        result = 'home'


homeView()
