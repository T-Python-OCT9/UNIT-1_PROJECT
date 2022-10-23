class courses:

    courses_list=['security', 'SQL','C++']
    courses_dict={}

    def __init__(self) -> None:
        pass
    
    def addcourse (self ,teacher_name : str , subject : str , amount: int):

        self.teacher_name =teacher_name 
        self.subject=subject
        self.amount=amount
        self.courses_list.append(self.subject)
        self.courses_dict[self.subject]= self.amount

    def  avalible_courses(self):

        return self.courses_list
    
    def courses_price(self, name : str):
        if name in self.courses_dict.keys():
            print (self.courses_dict[name])

'''
    def course_registration (self):
        customer_name =input("enter your name : ")
        phone_number=input("enter your phone number : ")
        print("choose from the following courses : ")
        print(self.avalible_courses())
        
        try: 
            course_name=input("write down the wanted course  : ")
            if course_name in self.avalible_courses():
                    print("you are in :) ")
       
        except:
            print(" this course doesn't exsit ")
    '''

