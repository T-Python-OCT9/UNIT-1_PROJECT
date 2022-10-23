def new_cons():
    
        nam_in =input("please enter your name:\n->")
        age_in=input("please enter your age:\n->")
        phone_num_in =input("please enter your phone number:\n")
        address_in =input("please enter your address:\n")
        email_in =input("please enter your email:\n")
        if not(len(nam_in)<3 or len(nam_in)>20 or int(age_in)>=99 or int(age_in)<=8 or len(str (phone_num_in))!=10 or len(address_in)>50 or len(email_in)>50) :
            services=("[0] exit","[1]Technical consultation","[2] Legal consultation","[3]Scientific consultation","[4] Medical consultation","[5] Psychological consultation","[6] Financial consultation","[7] Educational consultation")
            print(services)
            type=int(input("please chose the consulation type:"))
            consulation=input("please enter your question:\n->")
            file = open(f"{nam_in} {services[type]}.txt", "a", encoding="utf-8")
            file.write(f"--{services[type]}\t{nam_in}\t{age_in}\t{phone_num_in}\t{address_in}\t{email_in}\n \t{consulation} \n\t\t\status:waiting for answer\n")
            file.close()
            file = open(f"{nam_in} {services[type]}.txt", "r", encoding="utf-8")
            content = file.read()
            print(content)
            file.close()
            re=input("your consulation is complete ..To go back enter [1].for exit press[0]")
            if re =='0':
                return'0'
            else:
                return '1'

        else :
            print("\n\nunvalid input, try again.\n")

   
def home():

    
   
    while(True):
        print("_______________________________________________________\n")
        print("            Welcome To Consulting Website           ")
        print("_______________________________________________________\n")
        print("\t 1 New consultation\n")
        print("\t 2 my consulations\n")
        print("\t 0 exit\n")
        print("_______________________________________________________")
        print("                                                                      8 consultants")
        print("                                                                      9 admins")
        user_input=input("->")
        if user_input=='1':
            print("")
            y=new_cons()
            if y=='0':
                print("thank you for visiting ..see you soon -_^")
                break
        elif user_input=='2':
            pass
            
        elif user_input=='3':
            print("")
            print("my_cons()")
        elif user_input=='0':
            print("thank you for visiting ..see you soon -_^")
            break
        elif user_input=='8':
            print("")
            print("consultants()")
        elif user_input=='9':
            print("")
            print("admins_home()")
        else:
            print("please inter valid input")
home()

def client_home():
    pass
