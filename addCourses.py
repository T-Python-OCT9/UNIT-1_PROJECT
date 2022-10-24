
field_List =["Finance & accounting" , "IT" ,"Business" , "Design"]
field = {"Finance & accounting" : "FinanceAccounting.txt" , "IT" : "ITCourses.txt" , "Business":"Business.txt"  , "Design": "Design.txt"}

def add_Courses(company):
    
 while True:
  company = input("Do you want to Browse the students name registered in the courses? or add a courses? , if you want browse entre 'b' and if you want add course entre 'a' :")
  if company =='b':
     print("Names :")
     Registerd_Names = open("Registeredinfo.txt" , "r" ,encoding="utf-8")
     Names = Registerd_Names.readlines()
     for index,note in enumerate(Names):
        print(f"{index} - {note}")

  elif company == 'a':
     print(field_List)
     print("-"*10)

     comapy_Chose = input("what the field you want added the course in ?")

     if comapy_Chose == 'Design':
        Add(comapy_Chose)
        break
      

     elif comapy_Chose == 'Finance & accounting':
       Add(comapy_Chose)
       break
      
     elif comapy_Chose == 'IT':
        Add(comapy_Chose)
        break
      
     elif comapy_Chose == 'Business':
        Add(comapy_Chose)
        break

     elif comapy_Chose =='Exit':
      print("Thank you :)")
      break

     elif ValueError :
      print("please enter Correct vlaue !!!  \n")

  elif company == 'Exit':
     print("Thank you :)")
     break     

  elif ValueError :
   print("please enter Correct vlaue !!!  \n")
  

def Add(comapy_Chose ):
    add_Course = input("please entre the course and the time :")
    add_New_Course = open(field[comapy_Chose] ,"a", encoding="utf-8")
    add_New_Course.write("\n"+add_Course  )
    add_New_Course.close()
    print("Added the Course Successfully \nThank you:)")

