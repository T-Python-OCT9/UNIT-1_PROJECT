


field = {"Finance & accounting" : "FinanceAccounting.txt" , "IT" : "ITCourses.txt" , "Business":"Business.txt"  , "Design": "Design.txt"}

def Register(Student):

 while True:
   if Student == 'Design':
    available_Courses(Student)
    break
 

   elif Student == "IT":
    available_Courses(Student)
    break


   elif Student == "Business":
    available_Courses(Student)
    break

   elif Student == "Finance & accounting":
    available_Courses(Student)
    break

   elif Student == "Exit":
    print("Thank you :)")
    break  

   else : ValueError 
   print("please enter Correct vlaue !!!  \n")
   break
   


def student_Registration(user_information):
  user_information = input("please entre your full name and the course you want :")
  add_info = open("Registeredinfo.txt" ,"a", encoding="utf-8")
  add_info.write("\n"+user_information )
  add_info.close()
  print("Registration Succesfully \nSee you Soon :)")


def available_Courses(Student):
 while True:
  student_input = input("Do you want to register one of the courses or check courses and times ? please entre the 'r' to register or 'c'to check :")
  if student_input =='c':
    avalible_Courses = lambda x:x 
    print(avalible_Courses("Avalible Courses:"))
    AllCourses = open(field[Student], "r" ,encoding="utf-8")
    courses = list(AllCourses.readlines())
    for index,note in enumerate(courses):
        print(f"{index} - {note}")
    
  elif student_input =='r':
   return student_Registration(Student)
   break

  elif student_input =='Exit':
   print("Thank you :)")
   break

  elif ValueError :
   print("please enter Correct vlaue !!!  \n")
  

  