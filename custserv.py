import statistics


class custserv:

    rating_list=list()

    def most_asked_QI(self):

        file1= open("most_asked.txt", 'r', encoding="utf-8")
        lines=file1.readlines()
        for l in lines:
                print(l)
                 

    def omplaints_suggestions(self):
        file= open( "omplaints and suggestions.txt", 'a+', encoding="utf-8")
        user_opinion=input("please enter you opinion : \n")
        file.writelines(user_opinion + "\n" )
        print("thank you !!")
        file.close()
    
    def service_rating(self , rating : int ):
        self.rating_list.append(rating)


    def get_rating(self):
       x=lambda  rating_list : sum(rating_list) / len(rating_list)
       return x(self.rating_list)
'''
c=custserv()
c.service_rating(5)
c.service_rating(4)
c.service_rating(5)
print(c.get_rating())
'''


        #return statistics.mean(self.rating_list)
    







