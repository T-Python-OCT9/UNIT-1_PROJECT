# project 1 for the first 

from custserv import *
from courses import *



customer_service1 = custserv ()
c= courses('ghadah','course2', 800)

def user_servces():

    
    
    while True:
        
     try:

        user_answare=input( f"Welcome to IT_courses website , we are here to help you " +
         "\n"+"please type 1 : to list most asked questions" + "\n"+"please type : 2 if you want to list the avalible courses for the next month "
         + "\n"+"please type 3: هf you want to complain or suggest your opinion "  + "\n"+"please type 4 : if you want to rigster in any course  ")

        if user_answare == '1':

            print(customer_service1.most_asked_QI())
            
      
        elif user_answare== '2': 

             print(c.avalible_courses())
            
          
        elif user_answare == '3':

            customer_service1.omplaints_suggestions()

    
        elif user_answare == '4':

            c.course_registration()
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
     
         