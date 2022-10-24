
''' import datetime
dt = '21/03/2012'
day, month, year = (int(x) for x in dt.split('/'))    
ans = datetime.date(year, month, day)
print (ans.strftime("%A"))

ليست تدخل كل التواريخ وتشيك على كل واحد اذا فيه او لا 
'''
from datetime import datetime 
import time
'''
import datetime
NextDay_Date = datetime.datetime.today() + datetime.timedelta(days=1)
print (NextDay_Date)
+++++++++++++++++++
The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)

  countdown = PYCON_DATE - datetime.now()

'''

#datetime(year, month, day , [hour , [ minute , [ second ,[ microsecond,[ tzinfo]]]]])

# datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])

#op = datetime(2022, 8, 4 , [ 5 [ 30 , [ 00 ,[ 00,[ 00]]]]])



'''
dateTime = {"2022-10-22": "p2" ,"2022-10-23 5:40 ":"p3" , "2022-10-20 5:30 ":"p4"  }
dateTime2 = input("the date : ")
if len( dateTime2 ) == dateTime2.isnumeric():
    if dateTime2 in  dateTime :
       print("no")

''' 
op = datetime( year=2021 , month=10 , day= 20 , hour=13 , minute=14, second=00) 
op2 = datetime( year=2021 , month=10 , day= 23 , hour=13 , minute=14, second=00) 
'''
year = 2022
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
hours = int(input('Enter the hour: '))
minutes = int(input('Enter the minutes: '))
seconds = 00
'''
'''
#dt = datetime(year, month, day, hours, minutes, seconds)
date_list = [ op , op2 ] 


for d in date_list :
    print(f"date : {d} ")
    


dt = datetime(year = 2022
, month = int(input('Enter a month: '))
, day = int(input('Enter a day: ')))
'''
'''
if len(dt) in date_list:
    print("noo")
else:
    print("yy")'''
'''
for d in date_list :
    if  d in len(dt) :
         print("no ")
    else:
        print("yaa")
    
'''
    

#op3 = datetime ( year=2021 , month=input("monthe ") , day=input("monthe _ daay "), hour=00 , minute=00, second=00) 
'''
if dt.datetime in len (str (date_list)):
        print("no ")
else:
    print("ya")
 
'''

'''
 
print("Checking if days  exists in list")
x=list(map(str,date_list))
y="-".join(x)
 
if dt in x :
    print("Yes, 15 exists in list")

else:
    date_list.__add__(dt)
    print("No,  does not exists in list")


for d in date_list :
    print(f"date : {d} ")
'''


dt = datetime(year = 2022
, month = int(input('Enter a month: '))
, day = int(input('Enter a day: ')))

dates = [ "2022-09-03",
"2012-10-08",
"2012-10-09",
"2012-11-12",
# .. more values snipped for brevity
"2013-04-19",
"2013-05-27", ]

if dt in dates:
    print ("true")
elif dt not in dates:
    print ("false")