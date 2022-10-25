from Class import *

m1 = Employee("ahmad","15000","yes","8")
m2 = Employee("mohamad","13000","yes","6")

print ("*************************************************")
print ("Welcome to the Retirees Wages Calculation Section")
print ("*************************************************")
n=input ("Do you want to view registered employees? ")
if n == "yes":
    m1.setName("Ahmed")
    print(m1.getName())

    m1.setSalary("15000")
    print(m1.getSalary())

    m1.setofficer("yes")
    print(m1.getofficere())

    m1.setyears_of_service("8")
    print(m1.getyears_of_service())

    m2.setName("mohamd")
    print(m2.getName())

    m2.setSalary("13000")
    print(m2.getSalary())

    m2.setofficer("yes")
    print(m2.getofficere())

    m2.setyears_of_service("6")
    print(m2.getyears_of_service())

      
print ("*************************************************")

m= input("Do you want to calculate the dues of a new employee? ")
print ("*************************************************")

name=  input("Please write the employee's name ")
print ("*************************************************")

officer=  input("Is the employee an officer? ")
print ("*************************************************")

Salary=  input("How much salary is owed to the employee? ")

while True:
    try:
        Salary= int(Salary)
        if Salary >= 99999 :
            print("you need at least 5 characters")
            Salary= input("How much salary is owed to the employee? ")
        else:
            break
    except:
        print("please enter numbers only")
        Salary= input("How much salary is owed to the employee? ")

print ("*************************************************")

years_of_service= input("How many years of service? ")

while True:
    try:
        years_of_service= int(years_of_service)
        if years_of_service >= 100 :
            print("you need at least 2 characters")
            years_of_service= input("How many years of service? ")
        else:
            break
    except:
        print("please enter numbers only")
        years_of_service= input("How many years of service? ")

Amounts_due=lambda years_of_service , Salary :  years_of_service * ( Salary * 1.5)
r = Amounts_due(years_of_service,Salary)

print ("*************************************************")

print("Name : ",name,"officer : ",officer,"Salary : ",Salary,"years_of_service"
,years_of_service,"Amounts due = ",r)

