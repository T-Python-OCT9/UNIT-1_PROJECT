class doctor :


    

    def __init__(self , idd : str , name :str  , departments :str  ):
        # 4 Attributes
        self.idd = idd
        self.name = name
        self.departments = departments
        

    # 1 Methods
    def DRinfo(self) :
        return f"Doctor's name is {self.name} , has an ID number {self.idd} In section {self.departments} "


dr1 = doctor("1045678945"," Ahmad   ", "Ophthalmology")
dr2 = doctor("1108764579"," Hamad   ", "Pediatrics")
dr3 = doctor("1108764579"," khaled  ", "Dermatology")
dr4 = doctor("1108764579"," Mohammed", "General Practitioner")
dr5 = doctor("1108764579"," Amera   ", "ENT")
dr6 = doctor("1108764579"," Huda    ", "Emergency medicine")


class  patients :


    

    def __init__(self , idd : str , name :str  , gender :str , age : int ):
        # 4 Attributes
        self.idd = idd
        self.name = name
        self.gender = gender
        self.age = age 
    

    #  Methods
    def PatientsInfo(self) :
        return f" your name is {self.name} , Your ID number {self.idd}  your gender is  {self.gender}  Your age   {self.age}"



class Bill( patients ):

    def __init__(self , idd : str , name :str  , gender :str , age : int , dateAPP , drName ):
        super().__init__(idd, name, gender, age) 
        self.dateAPP = dateAPP
        self.drName = drName
    

    def printBill (self):
        return f"your name is {self.name} \nYour ID number {self.idd} \n  your gender is  {self.gender} |  Your age   {self.age} \nwith a doctor {self.drName} |  on date  {self.dateAPP}"


        

    
