
field = {"Finance & accounting" : "FinanceAccounting.txt" , "IT" : "ITCourse.txt" , "Business":"Business.txt"  , "Design": "Design.txt"}

def Register(student):

 while True:
   if student == 'Design':
    student = input("Do you want to register for one of the courses or check the times ? please entre the 'r' to register or 'c'to check :")
    if student =='c':
     print("Avalible Courses:")
     AllCourses = open("Design.txt" , "r" ,encoding="utf-8")
     courses = list(AllCourses.readlines())
    for index,note in enumerate(courses):
        print(f"{index} - {note}")

    student = input("Do you want to register for one of the courses , please entre the 'r' to register :")
    if student == 'r':
        return Check(student)
    break

   elif student == "IT":
    pass

   elif student == "Business":
    pass

   elif student == "Finance & accounting":
    print("acc")
    break

   elif student == "Exit":
    pass

   else :
     ValueError 
     print("please enter Correct vlaue !!!  \n")
     break
 





def Check(user_information):
  user_information = input("please entre your name and the course you want :")
  add_info = open("Registeredinfo.txt" ,"a", encoding="utf-8")
  add_info.write(user_information + "\n")
  add_info.close()
  print("Registration Succesfully \nSee you Soon :)")

