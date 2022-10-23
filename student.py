
from atexit import register


from courses import courses 
c=courses()

class student:
    

    student_info=[]

    def __init__(self, name : str , id : str, ph_num : str ) -> None:
      
        self.name=name 
        self.id=id
        self.ph_num = ph_num
        self.student_info.append(self.name)
        self.student_info.append(self.id)
        self.student_info.append(self.ph_num)
       
    def course_registration (self):
        customer_name =input("enter your name : ")
        phone_number=input("enter your phone number : ")
        print("choose from the following courses : ")
        for n in c.avalible_courses():
            print(n)
        try: 
            course_name=input("write down the wanted course  : ")
            x=c.avalible_courses()
            if course_name in x :
                self.student_info.append(course_name)
                print("you are in :) ")
       
        except:
            print(" this course doesn't exsit ")






