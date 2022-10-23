# project 1 for the first 

from custserv import custserv
from courses import courses
from student import student


s=student('ghadah', '11','060999')
customer_service1 = custserv ()
c= courses('ghadah','course2', 800)

def user_servces():
    while True:
        
     try:

        user_answare=input( f"Welcome to IT_courses website , we are here to help you " +
         "\n"+"please type 1 : to list most asked questions" + "\n"+"please type : 2 if you want to list the avalible courses for the next month "
         + "\n"+"please type 3: If you want to complain or suggest your opinion "  + "\n"+"please type 4 : if you want to rigster in any course  "  + "\n"+"please type 5 : if you want to view a course price ")

        if user_answare == '1':

            print(customer_service1.most_asked_QI())
            
      
        elif user_answare== '2': 

             print(c.avalible_courses())
            
          
        elif user_answare == '3':

            customer_service1.omplaints_suggestions()

    
        elif user_answare == '4':

            s.course_registration()

        elif user_answare=='5':
            c.courses_price(input("Enter the course name : "))

        elif user_answare =='exit':
            
            customer_service1.service_rating(input("please rate us from 1 to 5 ! "))
            
            print("thank you for using our system :)  ")

            break

        else:
            raise ValueError

     except ValueError:

        print(" you didn't enter a valid value  ")

        break

user_servces()
     
         