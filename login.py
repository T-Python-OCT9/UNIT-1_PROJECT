from getpass import getpass
from unittest import result


def loginEmployee(employees_list: list):
    username = input(' Username: ')
    password = getpass(prompt=' Password: ')
    result = [False, '']
    for employee in employees_list:
        if username == employee.user:
            employee_user = employee.user
            employee_password = employee.password
            the_emplyee = employee
    try:
        if (username == employee_user and password == employee_password):
            login = True
            result = [login, the_emplyee]
    except:
        login = False
        result = [login, '']
    return result


def loginManager(manager_user: str, manager_password: str):
    username = input(' > Username: ')
    password = getpass(prompt=' > Password: ')
    if (username == manager_user and password == manager_password):
        login = True
    else:
        login = False
    return login
