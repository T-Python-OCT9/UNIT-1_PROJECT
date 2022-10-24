
from appointment import * 
from datetime import datetime 
import time


print(" ---------ALL THE DOCTORS-------- ")
print(dr1.DRinfo() )
print(dr2.DRinfo() )
print(dr3.DRinfo() )
print(dr4.DRinfo() )
print(dr5.DRinfo() )
print(dr6.DRinfo() )

print("  ")

inputuser  = str(input(" Choose Doctor : "))
the_Choose = inputuser 

ch1 = " "
def Chooseـdoctor ( the_Choose :str ):

    if the_Choose == "dr1":
        ch1 = dr1.name
        return ch1
    if the_Choose == "dr2":
        ch1 = dr2.name
        return ch1
    if the_Choose == "dr3":
        ch1 = dr3.name
        return ch1
    if the_Choose == "dr4":
        ch1 = dr4.name
        return ch1
    if the_Choose == "dr5":
        ch1 = dr5.name
        return ch1
    if the_Choose == "dr6":
        ch1 = dr6.name
        return ch1
    
Chooseـdoctor(the_Choose)
theDR = Chooseـdoctor(the_Choose)

#print(theDR)

print("Patients INFO : ")

'''
Patients_name = input(" your name ")
Patients_ID = input(" your Id ")
Patients_age = int(input(" your age  "))
Patients_gender = input(" your gender ")
'''

thePatient = patients( input(" your Id ") , input(" your name ") , input(" your gender "), int(input(" your age  ") ))

print(thePatient.PatientsInfo()) 

print("  ") 

print("These dates are not available")
dates = [ "2022-10-20",
"2022-10-21",
"2022-10-09",
"2022-11-01",
"2022-10-22",
"2022-10-23", ]
for d in dates :
    print(f"date : {d} ")

print("  ")
'''
while True :
   dt = datetime(year = 2022 , 
   month = int(input('Enter a month: ')) , day = int(input('Enter a day: ')))
   if dt in dates:
       print ("This date is reserved, try again ..")
       continue
   elif dt not in dates:
        print ("Your appointment has been booked")  
        dates.append(dt)
        break
'''

while True :
    #dt = datetime(year = 2022 , day = int(input('Enter a day: ')) , month = int(input('Enter a month: ')) )
    daystr = "2022-"+input('Enter a month: ')+"-"+input('Enter a day: ')
    #print(daystr)
    if daystr in dates:
        print ("This date is reserved, try again ..")
        continue
    else:
            print ("Your appointment has been booked")  
            dates.append(daystr)
            break

print("  ")

for d in dates :
    print(f"date : {d} ")


print("  ")



bill1 = Bill(thePatient.idd  , thePatient.name ,  thePatient.gender, thePatient.age , daystr , theDR)
print(" --------- THE BILL -------- ")
print(bill1.printBill())


















