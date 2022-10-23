from cli_view import commandLine
from manager import managerView
from employee import employeeView, employees_list
import os


def homeView() -> None:
    result = 'home'
    while result == 'home':
        result = commandLine(
            'Welcome to HR System\n\n \tType one of these commands:\n\t (M) - Login as manager.\n\t (E) - Login as employee.\n\t (EXIT) - Exit the system.')
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
