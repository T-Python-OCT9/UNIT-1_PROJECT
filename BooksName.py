from numbers import Number
import random
from unicodedata import numeric
import BooksPrice


class BooksName:
    #البحث عن كتاب في المكتبة
    Books = ["Do not give up","History remains open","Les Misérables","Night train to Lisbon"]
    book = input("Enter the name of the book you want: ")

    for i in Books:
        
        if book in Books:
           print("yes this book is in the library. ")           
        elif not(book in Books):
           print("sorry this book is not in the librari. ")
        break 




    #عرض كتب لكاتب معين
    '''writers =  [
            {'Turki Alhamad': [ 'History remains open','East valley','Memory wounds']},
            {"Victor":[ "Les Misérables"]},
            {"Pascal": [ "Night train to Lisbon"]},
            {"Dr.Ayed Al-Qarni": ["Do not give up"]}
            ]'''


    writers = {'Turki Alhamad': 'History remains open',"Victor":"Les Misérables","Pascal":"Night train to Lisbon","Dr. Ayed Al-Qarni": "Do not give up"}
    writers["Turki Alhamad"] = ['East valley','Memory wounds','History remains open']
    #print(writers["Turki Alhamad"])

     
    authors = input("Enter the author name to view his existing books: ")

    for j in writers.values():

        if authors in writers:
           print(writers[authors])
        else:
           print("sorry,Ther are no books for this author in the library. ")    
        break




 #اقتراح كتاب عشوائي للمستخدم
    def RandomBook(Books):
     
        randomly = input("Do you want to suggest a random book to you? yes or no? ")

        if randomly == 'yes':
           return f'We have suggested book {random.choice(Books)} for you'
            
        elif randomly == 'no' :
           print("OK,Thank you ")

        else:
            if randomly.isnumeric() and randomly.isnumeric():
                raise Exception("pleas enter yes or no. ") 
                 
                         
    book_random = print(RandomBook(Books))  




    #lambda
    def FunctionPrice1(): 

       p = input("to view books prices last more than 50 you shoud write 1 pleas. ")
       int(p)

       if(p == 1):
           BooksPrice.FunctionPrice2()


    FunctionPrice1()


     
        






       
        
        
