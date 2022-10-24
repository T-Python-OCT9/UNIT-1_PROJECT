
#from cinmea import *
#This function to choose the city 
def city()  -> int:
    
        print("Hi welcome to movie ticket booking: ")
        print("witch City do u live in :")
        print("1,Riyadh ")
        print("2,jeddah ")
        print("3,Dammam ")
        place = int(input("choose you'r options: ")) 
        if place == 1:
           Riyadh_Malls()
        elif place == 2:
            Jeddah_Malls()
        elif place == 3:
            Dammam_Malls()
            
        else:
            print("wrong choice!!")

def Riyadh_Malls () -> int:
    
        print ("1.riyadh Park","2.riyadh Front","3.boulevard Riyadh" )
        print ()
        r = int (input("Choose the cinema u want to attend:"))
        if r == 1:
            Riyadh_Park()
        elif r == 2 :
            Riyadh_Front()
        elif r == 3 :
            Boulevard_Riyadh()
            
        else:
            print("wrong choice!!")

def Riyadh_Park () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        s = int(input("choose from you'r options: "))
        if  s == 1 :
            Time_Red_Movie()
        elif s == 2:
            Time_LOTR_Movie()
        elif s == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice!!")

def Riyadh_Front () -> int  :

        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        q = int(input("choose from you'r options: "))
        if  q == 1 :
            Time_Red_Movie()
        elif q == 2:
            Time_LOTR_Movie()
        elif q == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")

def Boulevard_Riyadh () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        d = int(input("choose from you'r options: "))
        if  d == 1 :
            Time_Red_Movie()
        elif d == 2:
            Time_LOTR_Movie()
        elif d == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")  

def Jeddah_Malls () -> int:
    
        print ("1.Redsea","2.Arabia Mall","3.Aziz Mall" )
        print ()
        f = int (input("Choose the cinema u want to attend:"))
        if f == 1:
            RedSea()
        elif f == 2 :
            Arabia_Mall()
        elif f == 3 :
            Aziz_Mall()
            
        else:
            print("wrong choice!!")

def RedSea () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        g = int(input("choose from you'r options: "))
        if  g == 1 :
            Time_Red_Movie()
        elif g == 2:
            Time_LOTR_Movie()
        elif g == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice!!")

def Arabia_Mall () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        h = int(input("choose from you'r options: "))
        if  h == 1 :
            Time_Red_Movie()
        elif h == 2:
            Time_LOTR_Movie()
        elif h == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")

def Aziz_Mall () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        j = int(input("choose from you'r options: "))
        if  j == 1 :
            Time_Red_Movie()
        elif j == 2:
            Time_LOTR_Movie()
        elif j == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice!!")                                  

def Dammam_Malls   () -> int:
    
        print ("1.West Avenue","2.Dahran Mall","3.Nakhell Mall" )
        print ()
        k = int (input("Choose the cinema u want to attend:"))
        if k == 1:
            West_Avenue()
        elif k == 2 :
            Dahran_Mall()
        elif k == 3 :
            Nakhell_Mall()
            
        else:
            print("wrong choice!!")

def West_Avenue () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        L = int(input("choose from you'r options: "))
        if  L == 1 :
            Time_Red_Movie()
        elif L == 2:
            Time_LOTR_Movie()
        elif L == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")

def Dahran_Mall () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        z = int(input("choose from you'r options: "))
        if  z == 1 :
            Time_Red_Movie()
        elif z == 2:
            Time_LOTR_Movie()
        elif z == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")

def Nakhell_Mall () -> int  :
    
        print ("what movie u want to watch")
        print ("1.Red","2.Lord of the Rings","3.Harry potter")
        c = int(input("choose from you'r options: "))
        if  c == 1 :
            Time_Red_Movie()
        elif c == 2:
            Time_LOTR_Movie()
        elif c == 3:
            Time_Harrypotter_Movie()
            
        else :
              print ("wrong choice")

def  Time_Red_Movie() -> int :
        time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
        }
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
    

        tickets = int(input("how many tickets do u need: "))
        print ("where do u want to sit")
        seats1 ={
        "1": "front",
        "2": "Middel",
        "3": "Back",
        "4": "Left side",
        "5": "right side"
        }
        print(seats1)
        seats =  input("Choose ur seats:")
        Seats2 = seats1[seats]
        
        print (f"enjoy The Movie at {x} {tickets}- Tickets  {Seats2} Seats")

def  Time_LOTR_Movie() -> int :
        time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
        }
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        

        tickets = int(input("how many tickets do u need: "))
        print ("where do u want to sit")
        seats1 ={
        "1": "front",
        "2": "Middel",
        "3": "Back",
        "4": "Left side",
        "5": "right side"
        }
        print(seats1)
        seats =  input("Choose ur seats:")
        Seats2 = seats1[seats]
        
        print (f"enjoy The Movie at {x} {tickets}- Tickets  {Seats2} Seats")
def  Time_Harrypotter_Movie() -> int :
        time1 = {
        "1": "10.00-1.00",
        "2": "1.10-4.10",
        "3": "4.20-7.20",
        "4": "7.30-10.30"
        }
        print("choose your time:")
        print(time1)
        t = input("select your time:")
        x = time1[t]
        
        tickets = int(input("how many tickets do u need: "))
        print ("where do u want to sit")
        seats1 ={
        "1": "front",
        "2": "Middel",
        "3": "Back",
        "4": "Left side",
        "5": "right side"
        }
        print(seats1)
        seats =  input("Choose ur seats :")
        Seats2 = seats1[seats]
        
        print (f"enjoy The Movie at {x} {tickets}- Tickets  {Seats2} Seats")
        
city()