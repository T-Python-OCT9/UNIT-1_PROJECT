print ("welcome to your grades calculater ,,")
choice = print (input ("do you want to try it now ? y stand for yes and n stand for no."))

if choice == "y" or "Y" :

 Razan = { "name":"Razan Alshehri","assignment" : [88, 78, 40, 70],"test" : [80, 89],"project" : [98]}
 Maha = { "name":"Maha Khalid","assignment" : [82, 56, 44, 30],"test" : [80, 80],"project" : [88] }
 Noor = { "name" : "Noor Alqahtani","assignment" : [77, 82, 23, 39], "test" : [78, 77], "project" : [80]}
 Jana = { "name" : "Jana Almurshid","assignment" : [67, 55, 77, 21],"test" : [40, 50],"project" : [69]}
        

 
 
 def grades_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)
 

 def calculate_total_average(students):
    assignment = grades_average(students["assignment"])
    test = grades_average(students["test"])
    Project = grades_average(students["project"])
 
  
    return (0.1 * assignment +
            0.7 * test + 0.2 * Project)
 
 

 def grade_letter(score):
  if score>=95 and score<=100:
    print("Grade = A+")
  elif score>=90 and score<95:
    print("Grade = A")
  elif score>=85 and score<90:
    print("Grade = B+")
  elif score>=80 and score<85:
    print("Grade = B")
  elif score>=75 and score<80:
    print("Grade = C+")
  elif score>=70 and score<75:
    print("Grade = C")
  elif score>=65 and score<70:
    print("Grade = D+")
  elif score>=60 and score<65:
    print("Grade = D")
  elif score>=0 and score<60:
    print("Grade = F")

  else:
    print("Invalid Input!")
 
 

 students = [Razan, Maha, Noor, Jana]
 

 for i in students :
    print(i["name"])
    print("* * * *")
    print("Average marks for %s is : %s " %(i["name"],calculate_total_average(i)))
                          
    print("Letter Grade of %s is : %s" %(i["name"],grade_letter(calculate_total_average(i))))
     
    print()
else :
 print ("Thanks for stand by..")
 

