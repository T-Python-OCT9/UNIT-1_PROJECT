from cli_view import commandLine
import os
from login import loginEmployee


class Employee:
    def __init__(self, name: str, role: str, evaluate: float, employee_id: int, user: str, password: str, complaints: list) -> None:
        self.name = name
        self.role = role
        self.evaluate = evaluate
        self.employee_id = employee_id
        self.user = user
        self.password = password
        self.complaints = complaints


employee1 = Employee('Khaled Abdullah', 'Engineer', 3.2,
                     921183, 'khaled', '1234', [''])
employee2 = Employee('Yasser Ali', 'CFO', 3.2,
                     921184, 'khaled', '1234', [''])
employees_list: list = [employee1, employee2]


def employeeView(result: str) -> str:
    while result == 'e':
        os.system('clear')
        print(f"\n\t\tEmployee Login \n\n")
        employee_login = loginEmployee(employees_list)
        if employee_login == True:
            employee = 'main'
            while employee == 'main':
                employee = commandLine('Employee view')
                if employee == 'l':
                    commandLine('Show Salaries')
                    employee = 'main'
                elif employee == 'c':
                    commandLine('Promotiom')
                    employee = 'main'
                elif employee == 'e':
                    commandLine('Resignation')
                    employee = 'main'
                elif employee == 'home':
                    result = 'home'
                else:
                    employee = 'main'
        else:
            os.system('clear')
            login = commandLine(
                "\n\t\tEmployee Login \n\n\tUsername or password not correct\n\tTry again or back to main?\n")
            if login == 'try':
                result = 'e'
            else:
                result = 'home'
    return result
