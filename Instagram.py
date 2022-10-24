class Instagram:
    def __init__(self, userName : str ): 
        self.userName=userName
        #List Instagram:
        self.Posts = ["Python_Post","Lab_Post","Unit_Post","Python12_Post"]

        #Command List:
        self.Comment = ["Post","Post","Post"]

        #Likes List:---------------
        self.Likes = []

        #MyPost List:--------------
        self.Mypost = []

        #MyComment List:-----------
        self.Mycomment = []
     #_____________________________
    def TimeLine(self):
        for post in self.Posts:
            print(post)

    #______________________________
    def addPost(self):
        _addPost = input("Add Your Post: ")
        self.Posts.append(_addPost)
        self.Mypost.append(_addPost)

    #_____________________________________________________________
    def addComment(self):
        _addcomment = input("Add Your Comment: ")
        self.Comment.append(_addcomment)
        self.Mycomment.append(_addcomment)

    #______________________________________________________________
    def Liked(self):
        for i in range(len(self.Posts)):
            print(i, self.Posts[i])
        indexPost = input("Which Post Would You Like? ")
        self.Likes.append(self.Posts[int(indexPost)])
        
    #__________________________________________________________________
    def ListLikes(self):
        for post in self.Likes:
            print(post)

    #__________________________________________________________________
    def MyPost(self):
        for post in self.Posts:
            print(post)

     #_________________________________________________________________
   
    def ListComment(self):
        for post in self.Comment:
            print(post)
    #__________________________________________________________________

    def startInstagram(self):
         #User1 =Instagram("Najd")
        print("         WELCOME To Instagram      ")
        #print("   Choose what you want   ")
        UserOptions = ""
        print(" Lets choose a number from the list  ")
        ##############################################
        #Using while loop
        while UserOptions != "e" :
            print("     1) To Add Post\n"+
                    "     2) To Like Post from Posts\n"+
                    "     3) To Add Comment\n"
                    "     4) To List all my liked posts\n"
                    "     5) To List all my comment\n"
                    "     6) To List all my posts\n"
                    "     7) To View Time Line Posts \n")

            UserOptions=input("What Would You Like To Do? press the number to choose or 'e' to exit ")  
            if UserOptions == '1' :
                self.addPost()
            elif UserOptions == '2' :
                self.Liked()
            elif UserOptions == '3' :
                self.addComment()
            elif UserOptions == '4' :
                self.ListLikes()
            elif UserOptions == '5' :
                self.ListComment()
            elif UserOptions == '6' :
                self.MyPost()
            elif UserOptions == '7' :
                self.TimeLine()
        else:
          print("Thank you for using the Instagram program, Come back again soon")