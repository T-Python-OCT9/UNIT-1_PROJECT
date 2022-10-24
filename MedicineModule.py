class Medicine:
    medicine_dic = {}

    def __init__(self,name,quantity,date):
        self.name = name
        self.quantity = quantity
        self.date = date
        
    def add_medicine(self):
        Medicine.medicine_dic[self.name] = (self.quantity,self.date)
    
    def display_medicine(self):
        for key, value in Medicine.medicine_dic.items():
            print(f"Name: {key} ,Quantity: {value[0]} ,Expire Date: {value[1]}")
    
    def search_medicine(self, medicine_name):
        if(medicine_name in Medicine.medicine_dic):
            medicine_value = Medicine.medicine_dic[medicine_name]
            print(f"Name: {medicine_name} ,Quantity: {medicine_value[0]} ,Expire Date: {medicine_value[1]}")
        else:
            print("Medicine is not existed")
       

    def delete_medicine(self,medicine_name):
        if(medicine_name in Medicine.medicine_dic):
            del Medicine.medicine_dic[medicine_name]
            print("Medicine is deleted...")
        else:
            print("Medicine is not existed")
    
    def statistic_medicine(self):
        total_qunatity = 0
        quantity_value = lambda value:int(value[0])
        for key, value in Medicine.medicine_dic.items():
            total_qunatity += quantity_value(value)

        return total_qunatity, len(Medicine.medicine_dic)