

class courses:
    
    courses_list=['security', 'SQL','C++']
    courses_dict={'security':300, 'SQL':400, 'c++': 200}
    

    def __init__(self , teacher_name : str,subject :str,amount : int   ) -> None:
        self.teacher_name =teacher_name 
        self.subject=subject
        self.amount=amount
        self.courses_list.append(self.subject)
        self.courses_dict[self.subject]= self.amount


      
    def  avalible_courses(self):

        return self.courses_list
    
    def courses_price(self, name : str):
        if name in self.courses_dict.keys():
            print (f'the course with the name {name} worth = ',self.courses_dict[name])
        else:
            print("this course dos'not exsit ")

    
    


