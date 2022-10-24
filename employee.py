from cli_view import commandLine
import os
from login import loginEmployee
from getpass import getpass


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
                     921183, 'khaled', '1234', [['OPEN','I would like to request a promotion since i joined the company as a senior.']])
employee2 = Employee('Yasser Ali', 'CFO', 3.2,
                     921184, 'Yasser', '1234', [['CLOSE','I have some issues.']])
employees_list: list = [employee1, employee2]


def employeeView(result: str) -> str:
    while result == 'e':
        os.system('clear')
        print(f"\n\t\tEmployee Login \n\n")
        employee_login = loginEmployee(employees_list)
        if employee_login[0] == True:
            the_employee = employee_login[1]
            employee = 'main'
            while employee == 'main':
                name_decoration: str = ((len(the_employee.name) + 12) * '-')
                employee = commandLine(f'# Welcome, {the_employee.name}.\n\t{name_decoration}\n\n\tType one of these commands:\n \t\t (I)    - Show your information\n \t\t (E)    - Show Evaluation\n\t\t (P)    - Change Passowrd\n \t\t (C)    - Make new complaint\n \t\t (HOME) - Logout')
                if employee == 'i':
                    information_view: str = 'information_view'
                    while information_view == 'information_view':
                        os.system('clear')
                        print('\n\t# Your Information\n\t------------------\n\n\tNAME                Employee Role    Employee ID\n\t----                -------------    -----------\n')
                        name_decorator: str = (" " * (20 - len(the_employee.name)))
                        role_decorator: str = (" " * (15 - len(the_employee.role)))
                        print(f'\t{the_employee.name}{name_decorator}{the_employee.role}{role_decorator}  {the_employee.employee_id}')
                        information_view = input('\n\tType (BACK) to return to manager window\n > ')
                        if information_view == 'back':
                            employee = 'main'
                        else:
                            information_view = 'information_view'
                    employee = 'main'
                elif employee == 'e':
                    information_view: str = 'information_view'
                    while information_view == 'information_view':
                        os.system('clear')
                        print(f'\n\t# Your Evaluation: {the_employee.evaluate}\n\t----------------------\n\n')
                        information_view = input('\n\tType (BACK) to return to manager window\n > ')
                        if information_view == 'back':
                            employee = 'main'
                        else:
                            information_view = 'information_view'
                    employee = 'main'
                elif employee == 'p':
                    information_view: str = 'information_view'
                    changed = ' '
                    while information_view == 'information_view':
                        os.system('clear')
                        print('\n\t# Change Your Password\n\t----------------------\n\n')
                        if len(changed) == 1:
                            the_employee.password = getpass(' > New Password: ')
                            changed='yes'
                            os.system('clear')
                            print('\n\t# Change Your Password\n\t----------------------\n\n')
                            print('\tYour password has been changed.')
                        elif changed == 'yes':
                            os.system('clear')
                            print('\n\t# Change Your Password\n\t----------------------\n\n')
                            print('\tYou already changed your password.')
                        information_view = input('\n\tType (BACK) to return to manager window\n > ')
                        if information_view == 'back':
                            employee = 'main'
                        else:
                            information_view = 'information_view'
                    employee = 'main'
                elif employee == 'c':
                    complaint_view: str = 'complaint_view'
                    while complaint_view == 'complaint_view':
                        os.system('clear')
                        print(f'\n\t# Complaints\n\t------------\n\n\t#     STATE     Complaint\n\t-     -----     ---------\n')
                        the_number: int = 0
                        for i in the_employee.complaints:
                            the_number += 1
                            state_decorator: str = (5 - len(i[0])) * ' '
                            print(f'\t{the_number}     {i[0]}{state_decorator}     {i[1][:25]}...')
                        complaint_view = input('\n\t(NEW)  - New complaint.\n\t(BACK) - Return to manager window.\n > ')
                        if complaint_view == 'back':
                            employee = 'main'
                        elif complaint_view == 'new':
                            os.system('clear')
                            print(f'\n\t# New Complaint\n\t---------------\n\n')
                            the_complaint: str = input(' Your Complaint: ')
                            the_employee.complaints.append(['OPEN', the_complaint])
                            employee = 'main'
                        else:
                            complaint_view = 'complaint_view'
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
