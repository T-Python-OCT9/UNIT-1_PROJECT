import random
import BooksPrice
class BooksName:
    Books = ["Do not give up","History remains open","Les Misérables","Night train to Lisbon"]

    book = input("Enter the name of the book you want: ")

    for i in Books:
        
        if book in Books:
           print("yes this book is in the library.",book)           
        elif not(book in Books):
            print("sorry this book is not in the librari.")
        break 

    
    '''writers =  [
            {'Turki Alhamad': [ 'History remains open','East valley','Memory wounds']},
            {"Victor":[ "Les Misérables"]},
            {"Pascal": [ "Night train to Lisbon"]},
            {"Dr. Ayed Al-Qarni": ["Do not give up"]}
            ]'''


    writers = {'Turki Alhamad': 'History remains open',"Victor":"Les Misérables","Pascal":"Night train to Lisbon","Dr. Ayed Al-Qarni": "Do not give up"}
    writers["Turki Alhamad"] = ['East valley','Memory wounds','History remains open']
     #print(writers["Turki Alhamad"])

     #ممكن اسوي الاكسبشن هنا لو دخل اليوزر اسم الكاتب غلط
    authors = input("Enter the author name to view his existing books: ")

    for j in writers.values():

        if authors in writers:
           print(writers[authors])
        else:
           print("sorry")    
        break


 #اقتراح كتاب عشوائي للمستخدم
    def RandomBook(Books):

        randomly = input("Do you want to suggest a random book to you? yes or no ")

        if randomly == 'yes':
            return random.choice(Books)
            
        if randomly == 'no' :
           #print("OK,Thank you")
            return 

    book_random = print("We have suggested book",RandomBook(Books),"for you")  

    #lambda
    def FunctionPrice1(): 
       p = int(print("to view books prices last more than 50 you shoud write 1 pleas."))
       #if(p == 1):
           #FunctionPrice2()

    


     
        






       
        
        
