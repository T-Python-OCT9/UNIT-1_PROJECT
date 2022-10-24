
from Register import Register
from addCourses import add_Courses

field_List =["Finance & accounting" , "IT" ,"Business" , "Design"]

class Courese_Website():
 print("... Welcome to courses Website ...")
 user_Question = input("Are you Student or Compny? please entre 's' if you student and 'c' if you company :")
 while True:
  
  print("-"*10)

  if user_Question == 's':
        print(field_List)
        field_chose = input("What the field you want? please choose and entre from the list : " )
        Register(field_chose)
        break
        

  elif user_Question == 'c':
        add_Courses(user_Question)
        break


  elif user_Question == 'Exit':
   print("Thank you :)")
   break     

  elif ValueError :
     print("please enter Correct vlaue !!!  \n")
     break
