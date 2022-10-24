import os
global services
global id_fielld
class consultent:
    def __init__(self, name,age:int,phone_num:int,email,field,id):
        self.name = name
        self.age = age
        self.phone_num=phone_num
        self.email=email
        self.field=field
        self.id=id

    def save_reg(self):
        
        os.chdir('C:/Users/wijda/Documents/python-camp/UNIT-1_PROJECT/')
        #print("Current working directorttty: {0}".format(os.getcwd()))
        file = open(f"{name} {type}.txt", "a", encoding="utf-8")
        file.write(f"\t {name}\t{type}\t{age}\t{phone_num}\t{email}\n \n")
        file.close()
        file = open(f"{name} {type}.txt", "r", encoding="utf-8")
        content = file.read()
        print(content)
        file.close()


