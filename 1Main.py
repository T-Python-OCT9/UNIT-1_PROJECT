
from Class import Employee

print ("*************************************************")
print ("Welcome to the Retirees Wages Calculation Section")
print ("*************************************************")

def first():
    n=input ("Do you want to view registered employees? ")
    n = str(n)
    if n == "yes":

        m1 = Employee("ahmad","15000","yes","8")
        m2 = Employee("mohamad","13000","yes","6")

        m1.name()
        m1.officer()
        m1.Salary()
        m1.years_of_service()

        m2.name()
        m2.officer()
        m2.Salary()
        m2.years_of_service()
        
    print ("*************************************************")

    print("Name : ",m1.name,"officer : ",m1.officer,"Salary : ",m1.Salary,"years_of_service"
,m1.years_of_service)

    print("Name : ",m1.name,"officer : ",m1.officer,"Salary : ",m1.Salary,"years_of_service"
,m1.years_of_service)

first()      

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

