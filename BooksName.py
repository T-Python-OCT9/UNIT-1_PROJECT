
class BooksName:
    Books = ["Do not give up","History remains open","Les Misérables","Night train to Lisbon"]

    book = input("Enter the name of the book you want: ")

    for i in Books:
        
        if book in Books:
           print("yes this book is in the library.",book)           
        elif not(book in Books):
            print("sorry this book is not in the librari.")
        break 
    #باقي انا اقترح عليه كتاب عشوائي

    def RandomBook():
        print("Do you want to suggest a random book to you? ")
    

    writers = {"Turki Alhamad" : "History remains open", "Victor" : "Les Misérables","Pascal" : "Night train to Lisbon","Dr. Ayed Al-Qarni" : "Do not give up"}
    
    authors = input("Enter the author's name to view his existing books: ")

    for j in writers.values():

        if authors in writers:
           print(writers[authors]) 
        break
        






       
        
        
