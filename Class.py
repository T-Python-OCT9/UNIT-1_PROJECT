class Employee:
    def __init__(self, name, Salary, officer, years_of_service) :
        self.name = name
        self.Salary = Salary
        self.officer = officer
        self.years_of_service = years_of_service


    def setName(self, Name):
        self.name = Name

    def setSalary(self, Salary):
        self.Salary = Salary

    def setofficer(self, office):
        self.officer = office
    
    def setyears_of_service(self, years):
        self.years_of_service = years

    def getName(self):
        return self.name
        
    def getSalary(self):
        return self.Salary

    def getofficere(self):
        return self.office

    def getyears_of_service(self):
        return self.years

        '''m1 = Employee("ahmad","15000","yes","8")
        m2 = Employee("mohamad","13000","yes","6")'''
        
'''    print ("*************************************************")

    print("Name : ",m1.name,"officer : ",m1.officer,"Salary : ",m1.Salary,"years_of_service",m1.years_of_service)

    print("Name : ",m1.name,"officer : ",m1.officer,"Salary : ",m1.Salary,"years_of_service",m1.years_of_service)
    '''