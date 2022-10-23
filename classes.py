class consultent:
    def __init__(self, name,age:int,phone_num:int,address,email,field):
        self.name = name
        self.age = age
        self.phone_num=phone_num
        self.address=address
        self.email=email
        self.field=field

    def new_reg(self):
        nam_in =input("please enter your name:\n->")
        age_in =input("please enter your age:\n->")
        phone_num_in =input("please enter your phone number:\n")
        address_in =input("please enter your address:\n")
        email_in =input("please enter your email:\n")
        client1_in =consultent (nam_in,age_in,phone_num_in,address_in,email_in)
        return client1_in()

