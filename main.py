from dataclasses import field
from logging import exception
from xml.dom import NotFoundErr
import os
from pathlib import Path
from xml.dom.minidom import Identified
from classes import *

consult_ids=set()
id_fielld ={}
services=["exit","Technical consultation","Legal consultation","Scientific consultation"," Medical consultation","Psychological consultation","Financial consultation","Educational consultation"]

def consult_menu():
    global id_fielld
    while(True):
            print("_______________________________________________________\n")
            print("\t 1 Reply to a consultation\n")
            print("\t 2 my consulations\n")
            print("\t 0 exit\n")
            print("_______________________________________________________")
            user_input=input("->")
            k=input("please enter your consultation ID:\n->")
            with open(r'consultants.txt', 'r') as file:
        # read all content from a file using read()
                content = file.read()
        # check if string present or not
                if k in content:
                    print()
                else:
                    print('id does not exist')
                    break
        
                if user_input=='1':                   
                    
                    print(" ")                
                    i=0
                    for x in services:
                        print(f"[{i}]  {x}")
                        i+=1
                    choice=int(input("choose field on cosultation:\n->"))
                    y= 'C:\\Users\\wijda\\Documents\\python-camp\\UNIT-1_PROJECT\\consultations\\'
                    word=services[choice]
                    print(word)
                    file_lis=search_in_dir(y,word)
                    answer=''
                    for ser in file_lis:
                        f = open(file_lis[ser], "a", encoding="utf-8")
                        print(f.read())
                        answer=f.readlines()+input("please write your answer:\n")
                        f.write(answer)
                        f.close()
                    

                elif user_input=='2':
                    y= 'C:\\Users\\wijda\\Documents\\python-camp\\UNIT-1_PROJECT\\consultations\\'
                    word=k
                    search_in_dir(y,k)
                elif user_input==0:
                    print("thank you for visiting ..see you soon -_^")
                    break

def save_reg():
    global id_fielld
    name=input("please enter your name:\n->")
    age =input("please enter your age:\n->")
    phone_num =input("please enter your phone number:\n")
    email =input("please enter your email:\n")
    id=input("please inter ID number:\n->")

    #id_fielld.append(id)
    
    i=0
    for x in services:
        print(f"[{i}]  {x}")
        i+=1
    in_type =int(input("please chose the consulation type:"))
    if in_type != '0':
        type=services[in_type]
        id_fielld[id]=type
        print(id_fielld)
        con1=consultent(name,age,phone_num,email,services[in_type],id)
        os.chdir('C:/Users/wijda/Documents/python-camp/UNIT-1_PROJECT/')
    #print("Current working directorttty: {0}".format(os.getcwd()))
        file = open(f"consultants.txt", "a", encoding="utf-8")
        file.write(f"\t {name}\t{age}\t{phone_num}\t{email}\t{type}\t{id}\n \n")
        file.close()
        id_fielld[id]=type
        file = open(f"consultants.txt", "r", encoding="utf-8")
        content = file.read()
        print(content)
        file.close()
        print(id_fielld)
    else:
        return 0
def search_in_dir(path,word):
    
    #dir_path = Path('C:\\Users\\wijda\\Documents\\python-camp\\UNIT-1_PROJECT\\consultations\\')
    search_path = path
    file_type ='.txt'
    search_str =word
    file_lis=list()

# Append a directory separator if not already present
    if not (search_path.endswith("/") or search_path.endswith("\\") ): 
        search_path = search_path + "/"
                                                          
# If path does not exist, set search path to current directory
    if not os.path.exists(search_path):
        search_path ="."

# Repeat for each file in the directory 
    i=0
    for fname in os.listdir(path=search_path) :
        
   # Apply file type filter   
        if fname.endswith(file_type):
            file_n=search_path + fname
        # Open file for reading
            fo = open(file_n, 'r',encoding='utf-8')

        # Read the first line from the file
            line = fo.read()

        # Initialize counter for line number
            line_no = 1
        # Loop until EOF
        
        if line != '' :
                # Search for string in line
                
                index = line.find(search_str)
                if ( index != -1) :
                    print(f"[{i}] ",end=' ')
                    print(fname)
                    file_lis.append(fname)
                    all=open(file_n,'r',encoding="utf-8")
                    cont=all.read()
                    print(cont)
                    all.close()

                    i+=1
                    
                # Increment line counter
                line_no += 1
        else:
            print("no consultations")       
        # Close the files
        fo.close() 
    return file_lis
        
    
    
    
def new_cons():
    nam_in =input("please enter your name:\n->")
    age_in=input("please enter your age:\n->")
    phone_num_in =input("please enter your phone number:\n")
    address_in =input("please enter your address:\n")
    email_in =input("please enter your email:\n")
    if not(len(nam_in)<3 or len(nam_in)>20 or int(age_in)>=99 or int(age_in)<=8 or len(str (phone_num_in))!=10 or len(address_in)>50 or len(email_in)>50) :
        i=0
        for x in services:
            print(f"[{i}]  {x}")
            i+=1
        in_type =int(input("please chose the consulation type:"))
        type=services[in_type]
        if in_type!=0:
            consulation=input("please enter your question:\n->")
            os.chdir('C:/Users/wijda/Documents/python-camp/UNIT-1_PROJECT/consultations/')
        #print("Current working directorttty: {0}".format(os.getcwd()))
            file = open(f"{nam_in} {type} .txt", "a", encoding="utf-8")
            file.write(f"--\t{nam_in}\t{age_in}\t{phone_num_in}\t{address_in}\t{email_in}\n \t{consulation}{type} \n\t\tstatus:waiting for answer\n")
            file.close()
            file = open(f"{nam_in} {type} .txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
            re=input("your consulation is complete ..To go back enter [1].for exit press[0]")
            if re =='0':
                return'0'
            else:
                return '1'
        else:
            return '0'
    else:
        raise exception ("please enter valid number\n")



def home():
    os.chdir('C:/Users/wijda/Documents/python-camp/UNIT-1_PROJECT/')
    while(True):
        print("_______________________________________________________\n")
        print("            Welcome To Consulting Website           ")
        print("_______________________________________________________\n")
        print("\t 1 New consultation\n")
        print("\t 2 my consulations\n")        
        print("\t 8 consultants\n")
        print("\t 9 admins\n")
        print("\t 0 exit\n")
        print("                                                                      ")
        user_input=input("->")
        if user_input=='1':
            print("")
            y=new_cons()
            if y=='0':
                print("thank you for visiting ..see you soon -_^")
                break
            else:
                print("")
            
        elif user_input=='2':
            y= 'C:\\Users\\wijda\\Documents\\python-camp\\UNIT-1_PROJECT\\consultations\\'
            x= input("please enter your phone number or your email to show your consulation\s.\n->")

            print(" ")
            search_in_dir (y,x)
            re=input("your consulation is complete ..To go back enter [1].for exit press[0]")
            if re =='0':
                print("thank you for visiting ..see you soon -_^")
                break
            else:
                print('')
            
        elif user_input=='3':
            print("")
            pass #my_cons()
        elif user_input=='0':
            print("thank you for visiting ..see you soon -_^")
            break
        elif user_input=='9':
            print("\t 1 Add new consultent\n")
            print("\t 2 show all consultants\n")
            print("\t 0 exit")
            val=input("\n->")
            if val=='1':
                save_reg()
            elif val=='2':
                file = open("consultants.txt", "r", encoding="utf-8")
                content = file.read()
                print(content)
                file.close()
            elif val=='0':
                print("thank you for visiting ..see you soon -_^")
                break
        elif user_input=='8':
            print("")
            consult_menu()
        else:
            print("please inter valid input")
home()
print(id_fielld)

