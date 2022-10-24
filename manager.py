from getpass import getpass
import os
from cli_view import commandLine
from login import loginManager
from employee import employees_list, Employee


class Manager:
    def __init__(self, user: str, password: str) -> None:
        self.__user = user
        self.__password = password

    def getUser(self):
        return self.__user

    def getPassword(self):
        return self.__password


manager1 = Manager('ahmed', '1234')


def managerView(result: str) -> str:
    while result == 'm':
        os.system('clear')
        print(f"\n\t# Manager Login\n\t---------------\n\n")
        manager_login = loginManager(
            manager1.getUser(), manager1.getPassword())
        if manager_login == True:
            manager = 'main'
            while manager == 'main':
                manager = commandLine(f'# Welcome Manager, {manager1.getUser().upper()}\n\t------------------------\n\n\tType one of these commands:\n \t\t (LIST) - List employees\n \t\t (ADD)  - Add new employee\n\t\t (EDIT) - Edit an employee\n \t\t (E)    - Evaluate an employee\n \t\t (C)    - Employees Complaints.\n \t\t (HOME) - Logout')
                if manager == 'list':
                    list_view: str = 'list_view'
                    while list_view == 'list_view':
                        os.system('clear')
                        print('\n\t# Employees List\n\t----------------\n\n\t#   NAME                Evaluate    Employee Role    Employee ID\n\t-   ----                --------    -------------    -----------\n')
                        the_number: int = 0
                        for employee in employees_list:
                            the_number += 1
                            name_decorator: str = (" " * (20 - len(employee.name)))
                            role_decorator: str = (" " * (15 - len(employee.role)))
                            print(f'\t{the_number}   {employee.name}{name_decorator}{employee.evaluate}         {employee.role}{role_decorator}  {employee.employee_id}')
                        list_view = input('\n\tType (BACK) to return to manager window\n > ')
                        if list_view == 'back':
                            manager = 'main'
                        else:
                            list_view = 'list_view'
                    manager = 'main'
                elif manager == 'edit':
                    edit_view: str = 'edit_view'
                    while edit_view == 'edit_view':
                        os.system('clear')
                        print('\n\t# Edit Employee\n\t---------------\n\n\t#   NAME                          Employee Role\n\t-   ----                          -------------\n')
                        the_number: int = 0
                        for employee in employees_list:
                            the_number += 1
                            name_decorator: str = (" " * (30 - len(employee.name)))
                            print(f'\t{the_number}   {employee.name}{name_decorator}{employee.role}')
                        the_employee_number = input('\n\t(#)    - Insert employee number to edit.\n\t(BACK) - Return to manager window.\n > ')
                        if isinstance(the_employee_number, str) and the_employee_number == 'back':
                            edit_view = 'back'
                        elif the_employee_number <= str(len(employees_list)):
                            the_employee_number = int(the_employee_number)
                            os.system('clear')
                            name_decorator = len(employees_list[the_employee_number - 1].name) * '-'
                            print(f'\n\t# Edit {employees_list[the_employee_number - 1].name} profile\n\t-------{name_decorator}--------\n\n\n\t#   NAME                          Employee Role\n\t-   ----                          -------------\n')
                            name_decorator = ((30 - len(employees_list[the_employee_number - 1].name)) * ' ')
                            print(f'\t{the_employee_number}   {employees_list[the_employee_number - 1].name}{name_decorator}{employees_list[the_employee_number - 1].role}')
                            edit_command = input('\n\tType one of these commands: \n\t(N) - Edit name.\n\t(R) - Edit role.\n > ')
                            name_decorator = (len(employees_list[the_employee_number - 1].name) * '-')
                            if edit_command == 'n':
                                os.system('clear')
                                name_decorator = (len(employees_list[the_employee_number - 1].name) * '-')
                                print(f'\n\t# Edit {employees_list[the_employee_number - 1].name} Name\n\t-------{name_decorator}-----\n')
                                employees_list[the_employee_number - 1].name = input(' > New Name: ')
                            elif edit_command == 'r':
                                os.system('clear')
                                print(f'\n\t# Edit {employees_list[the_employee_number - 1].name} Role\n\t-------{name_decorator}-----\n')
                                employees_list[the_employee_number - 1].role = input(' New Role: ')
                            else:
                                edit_view = 'edit_view'
                        else:
                            edit_view = 'edit_view'

                        if edit_view == 'back':
                            manager = 'main'
                        else:
                            edit_view = 'edit_view'
                elif manager == 'add':
                    add_view: str = 'add_view'
                    while add_view == 'add_view':
                        os.system('clear')
                        print('\n\t# Add New Employee\n\t------------------')
                        name: str = input('\n > Employee Name:     ')
                        role: str = input('\n > Employee Role:     ')
                        evaluate: float = 0.0
                        employee_id = employees_list[-1].employee_id + 1
                        user: str = input('\n > Employee Username: ')
                        password: str = getpass(prompt='\n > Employee Password: ')
                        complaints = list()
                        new_employee = Employee(
                            name, role, evaluate, employee_id, user, password, complaints)
                        employees_list.append(new_employee)
                        break
                    manager = 'main'
                elif manager == 'e':
                    evaluate_view: str = 'evaluate_view'
                    while evaluate_view == 'evaluate_view':
                        os.system('clear')
                        print('\n\t# Evaluate Employee\n\t-------------------\n\n\t#   NAME                          Employee Evalaute\n\t-   ----                          -----------------\n')
                        the_number: int = 0
                        for employee in employees_list:
                            the_number += 1
                            name_decorator: str = (" " * (30 - len(employee.name)))
                            print(f'\t{the_number}   {employee.name}{name_decorator}{employee.evaluate}')
                        the_employee_number = input('\n\t(#)    - Insert employee number to evaluate.\n\t(BACK) - Return to manager window.\n > ')
                        if isinstance(the_employee_number, str) and the_employee_number == 'back':
                            evaluate_view = 'back'
                        elif the_employee_number <= str(len(employees_list)):
                            the_employee_number = int(the_employee_number)
                            os.system('clear')
                            name_decorator = len(employees_list[the_employee_number - 1].name) * '-'
                            print(f'\n\t# Evalute {employees_list[the_employee_number - 1].name}\n\t-----------{name_decorator}\n\n\n\t#   NAME                          Employee Evaluate\n\t-   ----                          -----------------\n')
                            name_decorator = ((30 - len(employees_list[the_employee_number - 1].name)) * ' ')
                            print(f'\t{the_employee_number}   {employees_list[the_employee_number - 1].name}{name_decorator}{employees_list[the_employee_number - 1].evaluate}')
                            evaluate_value = input('\n\tInsert the evaluate value out of 5.0: \n\t\n > ')
                            try:
                                employees_list[the_employee_number - 1].evaluate = float(evaluate_value)
                            except:
                                evaluate_view = 'evaluate_view'
                        else:
                            evaluate_view = 'evaluate_view'

                        if evaluate_view == 'back':
                            manager = 'main'
                        else:
                            evaluate_view = 'evaluate_view'
                    manager = 'main'
                elif manager == 'c':
                    complaints_view: str = 'complaints_view'
                    while complaints_view == 'complaints_view':
                        os.system('clear')
                        print('\n\t# Employees Complaints\n\t----------------------\n\n\t#   NAME                STATE   COMPLAINT\n\t-   ----                -----   ---------\n')
                        the_number = 0
                        for employee in employees_list:
                            if len(employee.complaints) >= 1:
                                name_decorator = (20 - len(employee.name)) * ' '
                                state_decorator: str = ''
                                for complaint in employee.complaints:
                                    the_number += 1
                                    the_state: str = complaint[0]
                                    state_decorator = ((8 - len(complaint[0])) * ' ')
                                    the_complaint: str = complaint[1]
                                    print(f'\t{the_number}   {employee.name}{name_decorator}{the_state}{state_decorator}{the_complaint[:15]}...\n')
                        complaints_command = input('\n\tType (BACK) to return to manager window\n > ')
                        if complaints_command == 'back':
                            complaints_view = 'back'
                            manager = 'main'
                        else:
                            complaints_view == 'complaints_view'
                elif manager == 'home':
                    result = 'home'
                else:
                    manager = 'main'
        else:
            os.system('clear')
            login = commandLine("\n\t\tManager Login \n\n\tUsername or password not correct\n\tTry again or back to main?\n")
            if login == 'try':
                result = 'm'
            else:
                result = 'home'
    return result
